# pylint: disable=too-few-public-methods

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

PRODUCT_TAG_ASSOCIATION = Table(
    'product_tag', Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)

PRODUCT_IMAGE_ASSOCIATION = Table(
    'product_image', Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id'), primary_key=True),
    Column('image_id', Integer, ForeignKey('images.id'), primary_key=True)
)

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    description = Column(String(8192))
    visible = Column(Boolean, default=False)

    tags = relationship('Tag', secondary=PRODUCT_TAG_ASSOCIATION, back_populates='products')
    images = relationship('Image', secondary=PRODUCT_IMAGE_ASSOCIATION, back_populates='products')

class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)

    products = relationship('Product', secondary=PRODUCT_TAG_ASSOCIATION, back_populates='tags')

class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)

    products = relationship('Product', secondary=PRODUCT_IMAGE_ASSOCIATION, back_populates='images')
