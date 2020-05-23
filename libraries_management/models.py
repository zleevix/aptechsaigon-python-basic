from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

LibrariesManagementBase = declarative_base()

class ModelBook(LibrariesManagementBase):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    category = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    author_id = Column(Integer, ForeignKey('author.id'))

    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def __str__(self): 
        return f"""
            Tên: {self.name}
            Thể loại: {self.category}
            Giá: {self.price}
        """

    @classmethod
    def input_book(cls):
        name = input('Tên: ')
        category = input('Thể loại: ')
        price = input('Giá: ')
        return cls(name, category, price)

class ModelAuthor(LibrariesManagementBase):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    books = relationship(ModelBook, backref='book',lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Tên: {self.name}"

    @classmethod
    def input_author(cls):
        name = input('Tên: ')
        return cls(name)


from sqlalchemy import create_engine
engine = create_engine('sqlite:///libraries-management.db')
LibrariesManagementBase.metadata.create_all(engine) 