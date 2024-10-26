from sqlalchemy.orm import sessionmaker, scoped_session
from .utils import product_to_dict
from ..models import Product, Tag


class TagRepository:
    def __init__(self, sql_engine):
        self.db_session = scoped_session(sessionmaker(bind=sql_engine))

    def get_and_set(self, tag_name):

        tag = self.db_session.query(Tag).filter_by(name=tag_name).first()

        if tag:
            return tag.id

        new_tag = Tag(name=tag_name)
        self.db_session.add(new_tag)
        self.db_session.commit()
        return new_tag.id

    def add_tag_for_product(self, product_id, tag_id):
        product = self.db_session.query(Product).get(product_id)
        tag = self.db_session.query(Tag).get(tag_id)
        if product and tag:
            product.tags.append(tag)
            self.db_session.commit()
            return True
        return False

    def get_products_by_tag(self, tag_id):
        tag = self.db_session.query(Tag).get(tag_id)
        if not tag:
            return []
        return [product_to_dict(product) for product in tag.products if product.visible]

    def clear_product_tags(self, product_id):
        product = self.db_session.query(Product).get(product_id)
        if not product:
            return False
        product.tags.clear()
        self.db_session.commit()
        return True

    def list(self):
        tags = self.db_session.query(Tag).join(Tag.products).distinct().all()
        return [tag.name for tag in tags]
