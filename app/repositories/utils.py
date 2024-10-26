
def product_to_dict(product):
    return {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'visible': product.visible,
        'images': [(image.id, image.name) for image in product.images],
        'tags': [tag.name for tag in product.tags]
    }
