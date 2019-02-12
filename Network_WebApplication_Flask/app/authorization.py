# wraps tool to create decorators
from functools import wraps

from flask import request, jsonify

USER = 'admin'
PASSWORD = 'secret'


def check_auth(username, password):
    return username == USER and password == PASSWORD


def authenticate():
    message = {'message': 'Authenticate, please'}
    resp = jsonify(message)

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'

    return resp


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization  # It's a dictionary like
        # {'username': '', 'password': ''}
        if not auth:
            return authenticate()

        elif not check_auth(auth.username, auth.password):
            return authenticate()

        return f(*args, **kwargs)

    return decorated
