from sqlalchemy.orm import sessionmaker, scoped_session
from .utils import product_to_dict
from ..models import Product


class ProductRepository:
    def __init__(self, sql_engine):
        self.db_session = scoped_session(sessionmaker(bind=sql_engine))

    def create(self, name, description):
        new_product = Product(name=name, description=description)
        self.db_session.add(new_product)
        self.db_session.commit()
        return new_product.id

    def update(self, product_id, name=None, description=None, visible=False):
        product = self.db_session.query(Product).get(product_id)
        if not product:
            return False
        product.name = name
        product.description = description
        product.visible = visible
        self.db_session.commit()
        return True

    def delete(self, product_id):
        product = self.db_session.query(Product).get(product_id)
        if not product:
            return False
        self.db_session.delete(product)
        self.db_session.commit()
        return True

    def get(self, product_id):
        product = self.db_session.query(Product).get(product_id)
        if not product:
            return None
        return product_to_dict(product)

    def list_all(self, page=0, per_page=30):
        offset_value = page * per_page
        products = self.db_session.query(Product).limit(per_page).offset(offset_value).all()
        return [product_to_dict(product) for product in products]

    def list_visible(self, page=0, per_page=30):
        offset_value = page * per_page
        products = (
            self.db_session.query(Product)
                .filter_by(visible=True)
                .limit(per_page)
                .offset(offset_value)
                .all()
        )
        return [product_to_dict(product) for product in products]
