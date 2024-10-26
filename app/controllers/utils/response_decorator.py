from functools import wraps
from flask import render_template, current_app


def response_decorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        content = f(*args, **kwargs)
        return render_template('main.html',
                               title=current_app.json_config['title'],
                               footer=current_app.json_config['footer'],
							   content=content)
    return decorated_function
