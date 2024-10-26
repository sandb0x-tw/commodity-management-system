from functools import wraps
from flask import request, abort, g, current_app

def authenticate(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        g.login = False
        token = request.cookies.get("jwt")
        if token:
            g.login = current_app.authenticate_service.authenticate_token(token) is not None
        return f(*args, **kwargs)
    return decorated_function

def require_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not hasattr(g, 'login'):
            abort(401)
        return f(*args, **kwargs)
    return decorated_function
