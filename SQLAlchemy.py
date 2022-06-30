import os
import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from homework_models import create_tables, Publisher, Book, Shop, Stock, Sale


def data_load():
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASS')
    db_name = os.environ.get('DB_NAME')
    DNS = f'postgresql://{db_user}:{db_pass}@localhost:5432/{db_name}'
    engine = sqlalchemy.create_engine(DNS)
    Session = sessionmaker(bind=engine)
    session = Session()
    create_tables(engine)
    with open('tables_data.json', 'r') as f:
        data = json.load(f)
    for mod in data:
        if mod['model'] == 'publisher':
            info = Publisher(name=mod['fields']['name'])
            session.add(info)
            session.commit()
        if mod['model'] == 'book':
            info = Book(title=mod['fields']['title'], id_publisher=mod['fields']['id_publisher'])
            session.add(info)
            session.commit()
        if mod['model'] == 'shop':
            info = Shop(name=mod['fields']['name'])
            session.add(info)
            session.commit()
        if mod['model'] == 'stock':
            info = Stock(id_shop=mod['fields']['id_shop'], id_book=mod['fields']['id_book'],
                         count=mod['fields']['count'])
            session.add(info)
            session.commit()
        if mod['model'] == 'sale':
            info = Sale(price=mod['fields']['price'], date_sale=mod['fields']['date_sale'],
                        count=mod['fields']['count'], id_stock=mod['fields']['id_stock'])
            session.add(info)
            session.commit()
    session.close()


def select_db():
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASS')
    db_name = os.environ.get('DB_NAME')
    DNS = f'postgresql://{db_user}:{db_pass}@localhost:5432/{db_name}'
    engine = sqlalchemy.create_engine(DNS)
    Session = sessionmaker(bind=engine)
    session = Session()
    name_or_id = input('Введите имя или id издателя: ')
    if name_or_id.isdigit():
        for inf in session.query(Publisher).filter(Publisher.id == name_or_id).all():
            return print(inf)
    for inf in session.query(Publisher).filter(Publisher.name == name_or_id).all():
        return print(inf)
    session.close()


data_load()
select_db()

