import webapp2

from lib.handlers import (
    Hello,
    Message,
    Session,
    User
)

routes = [
    webapp2.Route(
        '/api',
        handler=Hello.Handler,
        methods=['GET']
    ),
    webapp2.Route(
        '/api/message/<userid>',
        handler=Message.Handler,
        methods=['GET', 'POST']
    ),
    webapp2.Route(
        '/api/session',
        handler=Session.Handler,
        methods=['POST']
    ),
    webapp2.Route(
        '/api/session/<userid>',
        handler=Session.Handler,
        methods=['DELETE']
    ),
    webapp2.Route(
        '/api/user',
        handler=User.Handler,
        methods=['GET', 'POST']
    )
]

config = {
    'webapp2_extras.sessions': {
        'secret_key': 'The_Truth_Is_Out_There'
    }
}

app = webapp2.WSGIApplication(routes=routes, debug=True, config=config)
