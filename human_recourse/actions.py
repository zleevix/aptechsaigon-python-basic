from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import logger
from models import HumanResourceBase, ModelEmployee, ModelDepartment
engine = create_engine('sqlite:///human-resource.db')
HumanResourceBase.metadata.bind = engine

db_session = sessionmaker()
db_session.bind = engine
session = db_session()

def list_employee():
    result = []
    all_employees = session.query(ModelEmployee).all()
    for employee in all_employees:
        department = session.query(ModelDepartment).filter_by(id = employee.department_id).first()
        result.append({
            'id': employee.id,
            'name': employee.name,
            'title': employee.title,
            'age': employee.age,
            'address': employee.address,
            'department': department.name
        })
    logger.write_file("DS Nhân viên", result)
    return result

def list_department():
    result = []
    all_departments = session.query(ModelDepartment).all()
    for dept in all_departments:
        result.append({
            'id': dept.id,
            'name': dept.name
        })
    logger.write_file("DS Phòng ban", result)
    return result

def list_department_and_count_employee():
    result = []
    all_departments = session.query(ModelDepartment).all()
    for dept in all_departments:
        result.append({
            'id': dept.id,
            'name': dept.name,
            'count_emp': dept.employees.count()
        })
    logger.write_file("DS Phòng ban với số Nhân viên", result)
    return result

def add_new_employee(new_employee):
    print(f"Chọn phòng ban cho nhân viên {new_employee.name}")
    for item in list_department():
        print(f"\t {item['id']}: {item['name']}")
    department_id = int(input("Select: "))
    new_employee.department_id = department_id
    logger.write_file("Thêm Nhân viên", new_employee)
    session.add(new_employee)
    session.commit()

def add_new_department(new_department):
    logger.write_file("Thêm Phòng ban", new_department)
    session.add(new_department)
    session.commit()

def find_employee(field, value):
    logger.write_file("Tìm nhân viên", f"Theo '{field}' với giá trị '{value}''")
    result = []
    # ['name', 'title', 'id']
    if field == 'name':
        all_employees = session.query(ModelEmployee).filter(ModelEmployee.name.like(f'%{value}%')).all()
    elif field == 'title':
        all_employees = session.query(ModelEmployee).filter(ModelEmployee.title.like(f'%{value}%')).all()
    elif field == 'id':
        all_employees = session.query(ModelEmployee).filter_by(id=value).all()
    for employee in all_employees:
        department = session.query(ModelDepartment).filter_by(id = employee.department_id).first()
        result.append({
            'id': employee.id,
            'name': employee.name,
            'title': employee.title,
            'age': employee.age,
            'address': employee.address,
            'department': department.name
        })
    return result