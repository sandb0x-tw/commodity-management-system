import hashlib
import os
import bcrypt
from flask import Blueprint, request, current_app, redirect, make_response

admin_api_bp = Blueprint('admin_api', __name__)

@admin_api_bp.route('/login/', methods=['POST'])
def login_api():
    response = make_response(redirect('/manage/'))
    user_password = current_app.json_config['password']
    form_password = request.form.get('password')
    if user_password == '' or bcrypt.checkpw(user_password, form_password.encode('utf-8')):
        response.set_cookie(
            'jwt',
            current_app.authenticate_service.issue_token({'admin': True}),
            60 * 60 * 2,
        )
    return response


@admin_api_bp.route('/product/', methods=['POST'])
def create_item_api():
    return {
        "successful": True,
        "id": current_app.product_repository.create("New Product", "")
    }

@admin_api_bp.route('/products/<int:product_id>', methods=['PUT', 'POST'])
def modify_item_api(product_id):

    def hash_file(file):
        hash_sha256 = hashlib.sha256()
        for chunk in iter(lambda: file.read(4096), b""):
            hash_sha256.update(chunk)
        file.seek(0)
        return hash_sha256.hexdigest()

    current_app.product_repository.update(product_id,
                                          request.form.get('name'),
                                          request.form.get('description'),
                                          request.form.get('visible') == 'on')

    for file in request.files.getlist('newImages'):
        if file.filename == '':
            continue
        file_hash = hash_file(file)
        file_ext = os.path.splitext(file.filename)[1]
        hashed_filename = f"{file_hash}{file_ext}"
        file_path = os.path.join('./data/images', hashed_filename)
        file.save(file_path)
        current_app.image_repository.add(hashed_filename, product_id)

    for image_to_remove in request.form.get('removedImageInfo').split(','):
        if image_to_remove:
            current_app.image_repository.delete(int(image_to_remove))

    current_app.tag_repository.clear_product_tags(product_id)
    tags = set()
    for tag in request.form.get('tags').split(' '):
        if tag and tag not in tags:
            tag_id = current_app.tag_repository.get_and_set(tag)
            current_app.tag_repository.add_tag_for_product(product_id, tag_id)
            tags.add(tag)

    return redirect(f'/modify/{product_id}')
