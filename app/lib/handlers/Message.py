import webapp2

from webapp2_extras.auth import Auth
from webapp2_extras.appengine.auth.models import User

from ... import models.Message

class Handler(webapp2.RequestHandler):
    def post(self, userid):
        from_id = self.request.get('from_id')
        token = self.request.headers['Authorization']
        auth = Auth(self.request)
        user, timestamp = User.get_by_auth_token(int(from_id), token)
        if not user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Error')
        elif not user.validate_token(from_id, 'auth', token):
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Error')
        else:
            #DO stuff here
            #Create new message
            #put it
            #return some status code or shit
            

    def get(self, userid):
        token = self.request.headers['Authorization']
        auth = Auth(self.request)
        user, timestamp = User.get_by_auth_token(int(userid), token)
        if not user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Error')
        elif not user.validate_token(from_id, 'auth', token):
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Error')
        else:
            #DO stuff here
            #Query messages that are for this mofo
            #Return that shit
