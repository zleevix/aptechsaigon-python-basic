from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import logger
from models import LibrariesManagementBase, ModelAuthor, ModelBook
engine = create_engine('sqlite:///libraries-management.db')
LibrariesManagementBase.metadata.bind = engine

db_session = sessionmaker()
db_session.bind = engine
session = db_session()

def list_book():
    result = []
    all_books = session.query(ModelBook).all()
    for book in all_books:
        author = session.query(ModelAuthor).filter_by(id = book.author_id).first()
        result.append({
            'id': book.id,
            'name': book.name,
            'category': book.category,
            'price': book.price,
            'author': author.name
        })
    logger.write_file("DS Sach", result)
    return result

def list_author():
    result = []
    all_authors = session.query(ModelAuthor).all()
    for author in all_authors:
        result.append({
            'id': author.id,
            'name': author.name
        })
    logger.write_file("DS Tác giả", result)
    return result

def list_author_and_count_book():
    result = []
    all_authors = session.query(ModelAuthor).all()
    for author in all_authors:
        result.append({
            'id': author.id,
            'name': author.name,
            'count_book': author.books.count()
        })
    logger.write_file("DS Tác giả với số Sách", result)
    return result

def add_new_book(new_book):
    print(f"Chọn tác giả cho sách {new_book.name}")
    for item in list_author():
        print(f"\t {item['id']}: {item['name']}")
    author_id = int(input("Select: "))
    new_book.author_id = author_id
    logger.write_file("Thêm Sách", new_book)
    session.add(new_book)
    session.commit()

def add_new_author(new_author):
    logger.write_file("Thêm Tác giả", new_author)
    session.add(new_author)
    session.commit()

def find_book(field, value):
    logger.write_file("Tìm sách", f"Theo '{field}' với giá trị '{value}''")
    result = []
    # ['name', 'category', 'id']
    if field == 'name':
        found_book = session.query(ModelBook).filter(ModelBook.name.like(f'%{value}%')).all()
    elif field == 'category':
        found_book = session.query(ModelBook).filter_by(category=value).all()
    elif field == 'id':
        found_book = session.query(ModelBook).filter_by(id=value).all()
    for book in found_book:
        author = session.query(ModelAuthor).filter_by(id = book.author_id).first()
        result.append({
            'id': book.id,
            'name': book.name,
            'category': book.category,
            'price': book.price,
            'author': author.name
        })
    return result