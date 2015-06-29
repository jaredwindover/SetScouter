import webapp2

from webapp2_extras.auth import Auth
from webapp2_extras.appengine.auth.models import User

from ..util import Response as resp
from ..util.Authorization import authenticate

class Handler(webapp2.RequestHandler):
    #Login returns token
    def post(self):
        self.response.headers['Content-Type'] = 'application/json'
        auth = Auth(self.request)
        email = self.request.get('email')
        password = self.request.get('password')
        try:
            user = auth.get_user_by_password(email, password)
        except:
                self.response.write(resp.fail_pass())
                return
        if not user:
            self.response.write(resp.fail_pass())
        else:
            token = User.create_auth_token(user['user_id'])
            self.response.write(resp.success({'Token' : token}))

    #Logout deletes token
    def delete(self, userid):
        self.response.headers['Content-Type'] = 'application/json'
        user =  authenticate(self.request, int(userid))
        if user:
            user.delete_auth_token(userid, token)
            self.response.write(resp.success())
        else:
            self.response.write(resp.fail_auth())

            
        
