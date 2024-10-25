from sqlalchemy.orm import sessionmaker, scoped_session
from ..models import Product


class ProductRepository:
    def __init__(self, sql_engine):
        self.db_session = scoped_session(sessionmaker(bind=sql_engine))

    def create(self, name, description):
        new_product = Product(name=name, description=description)
        self.db_session.add(new_product)
        self.db_session.commit()
        return new_product.id

    def update(self, product_id, name=None, description=None):
        product = self.db_session.query(Product).get(product_id)
        if not product:
            return False
        if name:
            product.name = name
        if description:
            product.description = description
        self.db_session.commit()
        return True

    def delete(self, product_id):
        product = self.db_session.query(Product).get(product_id)
        if not product:
            return False
        self.db_session.delete(product)
        self.db_session.commit()
        return True

    def get_images(self, product_id):
        product = self.db_session.query(Product).get(product_id)
        if not product:
            return []
        return [(image.id, image.name) for image in product.images]

    def get_tags(self, product_id):
        product = self.db_session.query(Product).get(product_id)
        if not product:
            return []
        return [tag.name for tag in product.tags]

    def __product_to_dict(self, product):
        return {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'visible': product.visible
        }

    def get(self, product_id):
        product = self.db_session.query(Product).get(product_id)
        if not product:
            return None
        return self.__product_to_dict(product)

    def list_all_products(self):
        products = self.db_session.query(Product).all()
        return [self.__product_to_dict(product) for product in products]

    def list_visible_products(self):
        products = self.db_session.query(Product).filter_by(visible=True).all()
        return [self.__product_to_dict(product) for product in products]
