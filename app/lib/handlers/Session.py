import webapp2

from webapp2_extras.auth import Auth
from webapp2_extras.appengine.auth.models import User

class Handler(webapp2.RequestHandler):
    #Login returns token
    def post(self):
        auth = Auth(self.request)
        email = self.request.get('email')
        password = self.request.get('password')
        user = auth.get_user_by_password(email, password)
        if not user:
            return
        token = User.create_auth_token(user['user_id'])
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Token : %s' % token)

    #Logout deletes token
    def delete(self, userid):
        token = self.request.headers['Authorization']
        auth = Auth(self.request)
        user, timestamp = User.get_by_auth_token(int(userid), token)
        if not user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Error')
        elif not user.validate_token(userid, 'auth', token):
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Error')
        else:
            user.delete_auth_token(userid, token)
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Success')
            
        
