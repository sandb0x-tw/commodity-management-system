# pylint: disable=R0801
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError
from .utils import product_to_dict
from ..models import Product


class ProductRepository:
    def __init__(self, sql_engine):
        self.db_session = scoped_session(sessionmaker(bind=sql_engine))

    def create(self, name, description):
        try:
            new_product = Product(name=name, description=description)
            self.db_session.add(new_product)
            self.db_session.commit()
            return new_product.id
        except SQLAlchemyError as e:
            self.db_session.rollback()
            print(f"Error during 'create': {e}")
            return None
        finally:
            self.db_session.remove()

    def update(self, product_id, name=None, description=None, visible=False):
        try:
            product = self.db_session.query(Product).get(product_id)
            if not product:
                return False
            product.name = name
            product.description = description
            product.visible = visible
            self.db_session.commit()
            return True
        except SQLAlchemyError as e:
            self.db_session.rollback()
            print(f"Error during 'update': {e}")
            return False
        finally:
            self.db_session.remove()

    def delete(self, product_id):
        try:
            product = self.db_session.query(Product).get(product_id)
            if not product:
                return False
            self.db_session.delete(product)
            self.db_session.commit()
            return True
        except SQLAlchemyError as e:
            self.db_session.rollback()
            print(f"Error during 'delete': {e}")
            return False
        finally:
            self.db_session.remove()

    def get(self, product_id):
        try:
            product = self.db_session.query(Product).get(product_id)
            if not product:
                return None
            return product_to_dict(product)
        except SQLAlchemyError as e:
            self.db_session.rollback()
            print(f"Error during 'get': {e}")
            return None
        finally:
            self.db_session.remove()

    def list_all(self, page=0, per_page=30):
        try:
            offset_value = page * per_page
            products = self.db_session.query(Product).limit(per_page).offset(offset_value).all()
            return [product_to_dict(product) for product in products]
        except SQLAlchemyError as e:
            self.db_session.rollback()
            print(f"Error during 'list_all': {e}")
            return []
        finally:
            self.db_session.remove()

    def list_visible(self, page=0, per_page=30):
        try:
            offset_value = page * per_page
            products = (self.db_session.query(Product)
                        .filter_by(visible=True)
                        .limit(per_page).offset(offset_value).all())
            return [product_to_dict(product) for product in products]
        except SQLAlchemyError as e:
            self.db_session.rollback()
            print(f"Error during 'list_visible': {e}")
            return []
        finally:
            self.db_session.remove()
