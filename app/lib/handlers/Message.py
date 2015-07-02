import webapp2

from webapp2_extras.auth import Auth
from webapp2_extras.appengine.auth.models import User

from ..models.Message import Message
from ..util import Response as resp
from ..util.Authorization import authenticate

class Handler(webapp2.RequestHandler):
    #post to message sends message
    def post(self, userid):
        user =  authenticate(self.request,
                             int(self.request.get('from_id')))
        if not user:
            self.response.write(resp.fail_auth())
        else:
            content = self.request.get('content')
            message = Message(
                content=content,
                from_firstname=user.firstname,
                from_lastname=user.lastname,
                to_userid=userid
            )
            message.put()
            self.response.write(resp.success())

    #get to message gets list of messages
    def get(self, userid):
        user = authenticate(self.request, int(userid))
        if not user:
            self.response.write(resp.fail_auth())
        else:
            q = Message.query(Message.to_userid == userid)
            def convert(message):
                return {
                    'content' : message.content,
                    'firstname' : message.from_firstname,
                    'lastname' : message.from_lastname
                }
            self.response.write(
                resp.success(
                    q.map(convert)
                )
            )
