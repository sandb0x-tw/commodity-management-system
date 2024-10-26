from functools import wraps
from flask import render_template, current_app, g


def response_decorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        content = f(*args, **kwargs)
        website_title = current_app.json_config['title']
        if hasattr(g, 'title'):
            title = f"{website_title} - {g.title}"
        else:
            title = website_title
        return render_template('main.html',
                               title=title,
                               website_title=website_title,
                               footer=current_app.json_config['footer'],
                               content=content)
    return decorated_function
