from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

HumanResourceBase = declarative_base()

class ModelEmployee(HumanResourceBase):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    title = Column(String(250), nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String(250))
    department_id = Column(Integer, ForeignKey('department.id'))

    def __init__(self, name, title, age, address):
        self.name = name
        self.title = title
        self.age = age
        self.address = address

    def __str__(self): 
        return f"""
            Tên: {self.name}
            Chức danh: {self.title}
            Tuổi: {self.age}
            Địa chỉ: {self.address}
        """

    @classmethod
    def input_employee(cls):
        name = input('Tên: ')
        title = input('Chức danh: ')
        age = int(input('Tuổi: '))
        address = input('Địa chỉ: ')
        return cls(name,  title, age, address)

class ModelDepartment(HumanResourceBase):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    employees = relationship(ModelEmployee, backref='employee',lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Tên: {self.name}"

    @classmethod
    def input_department(cls):
        name = input('Tên: ')
        return cls(name)


from sqlalchemy import create_engine
engine = create_engine('sqlite:///human-resource.db')
HumanResourceBase.metadata.create_all(engine) 