import json
from flask import Blueprint, render_template, current_app

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/modify/<int:product_id>')
def modify_item(product_id):
    product = current_app.product_repository.get(product_id)
    existing_images = []
    for image in current_app.product_repository.get_images(product_id):
        existing_images.append({
            'id': image[0],
            'url': f"/imgs/{image[1]}"
        })
    tags = ' '.join(current_app.product_repository.get_tags(product_id))
    vue = render_template('views/modify.vue',
                          product_id=product_id,
                          name=product['name'],
                          tags=tags,
                          existingImages=json.dumps(existing_images),
                          description=product['description'])
    return render_template('main.html',
                           title="Test",
                           content=vue,
                           footer="Test Website")
