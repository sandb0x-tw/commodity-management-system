from sqlalchemy.orm import sessionmaker, scoped_session
from ..models import Product, Image


class ImageRepository:
    def __init__(self, sql_engine):
        self.db_session = scoped_session(sessionmaker(bind=sql_engine))

    def add_image(self, name, product_id):
        new_image = Image(name=name)
        product = self.db_session.query(Product).get(product_id)
        if product:
            product.images.append(new_image)
            self.db_session.add(new_image)
            self.db_session.commit()
            return product.id
        return False

    def delete_image(self, image_id):
        image = self.db_session.query(Image).get(image_id)
        if not image:
            return False
        for product in image.products:
            product.images.remove(image)
        self.db_session.delete(image)
        self.db_session.commit()
        return True
