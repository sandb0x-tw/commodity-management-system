from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError
from ..models import Product, Image

class ImageRepository:
    def __init__(self, sql_engine):
        self.db_session = scoped_session(sessionmaker(bind=sql_engine))

    def add(self, name, product_id):
        try:
            new_image = Image(name=name)
            product = self.db_session.query(Product).get(product_id)
            if not product:
                return False
            product.images.append(new_image)
            self.db_session.add(new_image)
            self.db_session.commit()
            return product.id
        except SQLAlchemyError as e:
            self.db_session.rollback()
            print(f"Error during 'add' operation: {e}")
            return False
        finally:
            self.db_session.remove()

    def delete(self, image_id):
        try:
            image = self.db_session.query(Image).get(image_id)
            if not image:
                return False
            for product in image.products:
                product.images.remove(image)
            self.db_session.delete(image)
            self.db_session.commit()
            return True
        except SQLAlchemyError as e:
            self.db_session.rollback()
            print(f"Error during 'delete' operation: {e}")
            return False
        finally:
            self.db_session.remove()
