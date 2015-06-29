import webapp2

from webapp2_extras.auth import Auth
from webapp2_extras.appengine.auth.models import User
from google.appengine.ext import db

class Handler(webapp2.RequestHandler):
    def post(self):
        firstname = self.request.get('firstname')
        lastname = self.request.get('lastname')
        email = self.request.get('email')
        password = self.request.get('password')
        work, info = User.create_user(
            email,
            firstname=firstname,
            lastname=lastname,
            password_raw=password
        )
        if not work: #Should actually handle this by returning an error
            print "Failure"
            print info
            return
        user = info
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('User Created');

    def get(self):
        auth = Auth(self.request)
        token = self.request.headers['Authorization']
        userid = int(self.request.get('userid'))
        user, timestamp = User.get_by_auth_token(userid, token)
        if not user.validate_token(userid, 'auth', token):
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Error');
        else:
            q = User.query()
            self.response.headers['Content-Type'] = 'text/plain'
            print q
            for p in q:
                print p.firstname
                self.response.write(p.firstname);
                
            
