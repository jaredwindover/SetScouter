import webapp2

from webapp2_extras.auth import Auth
from webapp2_extras.appengine.auth.models import User

from ..util import Response as resp
from ..util.Authorization import authenticate

class Handler(webapp2.RequestHandler):
    #Login returns token
    def post(self):
        self.response.headers['Content-Type'] = 'application/json'
        email = self.request.get('email')
        password = self.request.get('password')
        try:
            user = User.get_by_auth_password(email, password)
        except:
                self.response.write(resp.fail_pass())
                return
        if not user:
            self.response.write(resp.fail_pass())
        else:
            token = User.create_auth_token(user.key.id())
            self.response.write(resp.success({
                'Token' : token,
                'User' : {
                    'firstname' : user.firstname,
                    'lastname' : user.lastname,
                    'email' : user.auth_ids[0],
                    'id' : user.key.id()
                }
            }))

    #Logout deletes token
    def delete(self, userid):
        self.response.headers['Content-Type'] = 'application/json'
        user =  authenticate(self.request, int(userid))
        if user:
            user.delete_auth_token(userid, self.request.headers['Authorization'])
            self.response.write(resp.success())
        else:
            self.response.write(resp.fail_auth())

            
        
