import json
from flask import Blueprint, render_template, current_app, g
from .utils import authenticate

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/manage/', methods=['GET'])
@authenticate
def dashboard():
    vue = render_template('views/manage.vue',
                          isLogged=str(g.login).lower(),
                          productList=[])
    return render_template('main.html',
                           title="Test",
                           content=vue,
                           footer="Test Website")

@admin_bp.route('/modify/<int:product_id>', methods=['GET'])
def modify_item(product_id):
    product = current_app.product_repository.get(product_id)
    existing_images = []
    for image in product['images']:
        existing_images.append({
            'id': image[0],
            'url': f"/imgs/{image[1]}"
        })
    tags = ' '.join(product['tags'])
    vue = render_template('views/modify.vue',
                          product_id=product_id,
                          name=json.dumps(product['name']),
                          tags=json.dumps(tags),
                          visible=str(product['visible']).lower(),
                          existingImages=json.dumps(existing_images),
                          description=json.dumps(product['description']))
    return render_template('main.html',
                           title="Test",
                           content=vue,
                           footer="Test Website")
