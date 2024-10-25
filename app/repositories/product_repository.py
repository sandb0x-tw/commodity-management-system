from sqlalchemy.orm import sessionmaker, scoped_session
from ..models import Product


class ProductRepository:
    def __init__(self, sql_engine):
        self.db_session = scoped_session(sessionmaker(bind=sql_engine))

    def add_product(self, name, description):
        new_product = Product(name=name, description=description)
        self.db_session.add(new_product)
        self.db_session.commit()

    def update_product(self, product_id, name=None, description=None):
        product = self.db_session.query(Product).get(product_id)
        if not product:
            return False
        if name:
            product.name = name
        if description:
            product.description = description
        self.db_session.commit()
        return True

    def delete_product(self, product_id):
        product = self.db_session.query(Product).get(product_id)
        if not product:
            return False
        self.db_session.delete(product)
        self.db_session.commit()
        return True

    def get_product_images(self, product_id):
        product = self.db_session.query(Product).get(product_id)
        if not product:
            return []
        return [image.name for image in product.images]

    def get_product_tags(self, product_id):
        product = self.db_session.query(Product).get(product_id)
        if not product:
            return []
        return [tag.tag for tag in product.tags]
