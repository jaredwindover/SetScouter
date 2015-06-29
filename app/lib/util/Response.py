import json

def fail(reason, explanation):
    response = {
        'status' : 'fail'
    }
    response[reason] = explanation
    return json.dumps(response)

def fail_auth():
    return fail(
        'Authentication',
        'The session token is invalid or does not match the user'
    )

def fail_pass():
    return fail(
        'password',
        'Password and email address combination is invalid'
    )

def success(data = None):
    return json.dumps({
        'status' : 'success',
        'data' : data
    })
