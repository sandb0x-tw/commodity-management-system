import json
from flask import Blueprint, render_template, current_app, g
from .utils import authenticate, response_decorator

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/manage/', methods=['GET'])
@authenticate
@response_decorator
def dashboard():
    if not g.login:
        return render_template('views/manage.vue',
                               isLogged=str(g.login).lower(),
                               productList=[],
                               title='""',
                               footer='""',
                               description='""')
    products = current_app.product_repository.list_all()
    return render_template('views/manage.vue',
                           isLogged=str(g.login).lower(),
                           productList=json.dumps(products),
                           title=json.dumps(current_app.json_config.get('title')),
                           footer=json.dumps(current_app.json_config.get('footer')),
                           description=json.dumps(current_app.json_config.get('description')))

@admin_bp.route('/modify/<int:product_id>', methods=['GET'])
@response_decorator
def modify_item(product_id):
    product = current_app.product_repository.get(product_id)
    existing_images = []
    for image in product['images']:
        existing_images.append({
            'id': image[0],
            'url': f"/imgs/{image[1]}"
        })
    tags = ' '.join(product['tags'])
    return render_template('views/modify.vue',
                           product_id=product_id,
                           name=json.dumps(product['name']),
                           tags=json.dumps(tags),
                           visible=str(product['visible']).lower(),
                           existingImages=json.dumps(existing_images),
                           description=json.dumps(product['description']))
