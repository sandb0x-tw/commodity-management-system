from flask import Blueprint, render_template

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def home():
    return render_template('main.html',
                           title="Test",
                           content="This is a test content.",
                           footer="Test Website")
