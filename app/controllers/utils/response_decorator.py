from functools import wraps
from flask import render_template, current_app, g


def response_decorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        content = f(*args, **kwargs)
        if hasattr(g, 'title'):
            title = f"{current_app.json_config['title']} - {g.title}"
        else:
            title = current_app.json_config['title']
        return render_template('main.html',
                               title=title,
                               footer=current_app.json_config['footer'],
                               content=content)
    return decorated_function
