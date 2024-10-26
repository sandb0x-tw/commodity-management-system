import os
import json
from flask import Blueprint, render_template, send_file, current_app, request, abort, g
from .utils import response_decorator

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
@response_decorator
def list_products():
    page = request.args.get('page', "0")
    if not page.isnumeric():
        abort(400)
    page = int(page)
    products = current_app.product_repository.list_visible(page, 30)

    items = []
    for product in products:
        item = {}
        item.update(product)

        del item['images']
        if 'images' in product and product['images']:
            item['image'] = f'/imgs/{product["images"][0][1]}'

        items.append(item)

    g.title = "主頁"

    return render_template('views/list.vue',
                           items=json.dumps(items))

@user_bp.route('/about')
@response_decorator
def about():
    return render_template('views/about.vue',
                           description=json.dumps(current_app.json_config['description']))

@user_bp.route('/category/')
@response_decorator
def list_products_by_category():
    category = request.args.get('category', None)
    g.title = category if category else "類別篩選"
    page = request.args.get('page', "0")
    items = []
    if category:
        page = request.args.get('page', "0")
        if not page.isnumeric():
            abort(400)
        tag_id = current_app.tag_repository.get_and_set(category)
        products = current_app.tag_repository.get_products_by_tag(tag_id, page, 30)
        for product in products:
            item = {}
            item.update(product)
            if 'images' in product and product['images']:
                item['image'] = f'/imgs/{product["images"][0][1]}'
            del item['images']
            del item['visible']
            items.append(item)
    tags = current_app.tag_repository.list()
    return render_template('views/category.vue',
                           items=items,
                           tags=tags)

@user_bp.route('/product/<int:product_id>')
@response_decorator
def view(product_id):
    product_data = current_app.product_repository.get(product_id)
    if product_data is not None and product_data['visible']:
        for i in range(len(product_data['images'])):
            product_data['images'][i] = f'/imgs/{product_data["images"][i][1]}'
        del product_data['visible']
        g.title = product_data['name']
        return render_template('views/view.vue', product_data=product_data)
    abort(404)

@user_bp.route('/imgs/<string:src>')
def img_download(src):
    path = os.path.join('../data/images', src)
    return send_file(path, as_attachment=False)
