from webapp2_extras.auth import Auth
from webapp2_extras.appengine.auth.models import User

def authenticate(request,id):
    auth = Auth(request)
    token = request.headers['Authorization']
    user, ts = User.get_by_auth_token(id, token)
    if not user:
        return None
    elif not user.validate_token(id, 'auth', token):
        return None
    return user
