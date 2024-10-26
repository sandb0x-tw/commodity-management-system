import hashlib
import json
import os
import bcrypt
from flask import Blueprint, request, current_app, redirect, make_response

admin_api_bp = Blueprint('admin_api', __name__)

@admin_api_bp.route('/login/', methods=['POST'])
def login_api():
    response = make_response(redirect('/manage/'))
    user_password = current_app.json_config['password'].encode('utf-8')
    form_password = request.form.get('password').encode('utf-8')
    if user_password == '' or bcrypt.checkpw(form_password, user_password):
        response.set_cookie(
            'jwt',
            current_app.authenticate_service.issue_token({'admin': True}),
            60 * 60 * 2,
        )
    return response

@admin_api_bp.route('/passwd', methods=['POST', 'PUT'])
def passwd_api():
    form_password = request.form.get('password').encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(form_password, salt).decode('utf-8')
    current_app.json_config['password'] = hashed_password
    with open('./data/config.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(current_app.json_config))
    return redirect('/manage')

@admin_api_bp.route('/products/', methods=['GET', 'POST'])
def create_item_api():
    product_id = current_app.product_repository.create("New Product", "")
    return redirect(f"/modify/{product_id}")

@admin_api_bp.route('/modify_website/', methods=['POST', 'PUT'])
def modify_website_info():
    current_app.json_config['title'] = request.form.get('title')
    current_app.json_config['footer'] = request.form.get('footer')
    current_app.json_config['description'] = request.form.get('description')
    with open('./data/config.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(current_app.json_config))
    return redirect('/manage')

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

@admin_api_bp.route('/products/<int:product_id>/delete/', methods=['GET', 'DELETE'])
def delete_item_api(product_id):
    current_app.product_repository.delete(product_id)
    return redirect(f"/manage")

