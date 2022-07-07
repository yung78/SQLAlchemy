import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.INTEGER, primary_key=True)
    name = sq.Column(sq.VARCHAR(length=50), nullable=False)

    book = relationship('Book', back_populates='publisher')

    def __str__(self):
        return f'id:{self.id}, name:{self.name}'


class Book(Base):
    __tablename__ = 'book'

    id = sq.Column(sq.INTEGER, primary_key=True)
    title = sq.Column(sq.VARCHAR(length=100), nullable=False)
    id_publisher = sq.Column(sq.INTEGER, sq.ForeignKey('publisher.id'), nullable=False)

    publisher = relationship('Publisher', back_populates='book')
    stock = relationship('Stock', back_populates='book')


class Shop(Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.INTEGER, primary_key=True)
    name = sq.Column(sq.VARCHAR(length=100), nullable=False)

    stock = relationship('Stock', back_populates='shop')

    def __str__(self):
        return f'id:{self.id}, name:{self.name}'


class Stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.INTEGER, primary_key=True)
    id_book = sq.Column(sq.INTEGER, sq.ForeignKey('book.id'))
    id_shop = sq.Column(sq.INTEGER, sq.ForeignKey('shop.id'))
    count = sq.Column(sq.INTEGER, nullable=False)

    book = relationship('Book', back_populates='stock')
    shop = relationship('Shop', back_populates='stock')


class Sale(Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.INTEGER, primary_key=True)
    price = sq.Column(sq.VARCHAR, nullable=False)
    date_sale = sq.Column(sq.DateTime, nullable=False)
    id_stock = sq.Column(sq.INTEGER, sq.ForeignKey('stock.id'))
    count = sq.Column(sq.INTEGER, nullable=False)

    stock = relationship('Stock', backref='sale')


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
