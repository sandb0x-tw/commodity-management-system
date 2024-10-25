import os
from flask import Blueprint, render_template, send_file

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def home():
    return render_template('main.html',
                           title="Test",
                           content="This is a test content.",
                           footer="Test Website")

@user_bp.route('/imgs/<string:src>')
def img_download(src):
    path = os.path.join('../data/images', src)
    return send_file(path, as_attachment=False)
