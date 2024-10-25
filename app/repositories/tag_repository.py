from sqlalchemy.orm import sessionmaker, scoped_session
from ..models import Product, Tag


class TagRepository:
    def __init__(self, sql_engine):
        self.db_session = scoped_session(sessionmaker(bind=sql_engine))

    def add_tag(self, tag):
        new_tag = Tag(tag=tag)
        self.db_session.add(new_tag)
        self.db_session.commit()

    def add_product_tag_association(self, product_id, tag_id):
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
        return [product.name for product in tag.products]
