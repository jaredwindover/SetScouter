import webapp2

from webapp2_extras.auth import Auth
from webapp2_extras.appengine.auth.models import User
from google.appengine.ext import db

from ..util import Response as resp
from ..util.Authorization import authenticate

class Handler(webapp2.RequestHandler):
    #post to users registers new user
    def post(self):
        self.response.headers['Content-Type'] = 'application/json'
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
        if not work:
            self.response.write(resp.fail(
                'email',
                'Email address already exists'
            ))
        else:
            user = info
            self.response.write(resp.success())

    #get to users gets list of users
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        user = authenticate(self.request, int(self.request.get('userid')))
        if not user:
            self.response.write(resp.fail_auth())
        else:
            q = User.query()
            def convert(user):
                return {
                    'firstname' : user.firstname,
                    'lastname' : user.lastname,
                    'email' : user.auth_ids[0]
                }
            self.response.write(
                resp.success(
                    q.map(convert)
                )
            )
                
            
