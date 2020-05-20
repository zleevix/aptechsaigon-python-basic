import actions
from models import ModelEmployee, ModelDepartment
def usage_first_menu():
    print("*"*10 + "\tHUMAN RESOURCE MANAGEMENT SYSTEM\t" + "*"*10)
    print('Xin mời các chọn lựa sau đây')
    print('\t 1. Hiển thị danh sách nhân viên')
    print('\t 2. Hiển thị danh sách phòng ban')
    print('\t 3. Hiển thị danh sách phòng ban và số nhân viên theo phòng ban')
    print('\t 4. Nhập thêm nhân viên mới')
    print('\t 5. Nhập thêm phòng ban mới')
    print('\t 6. Nhập thêm phòng ban và nhân viên mới')
    print('\t 7. Tìm kiếm nhân viên')
    print('\t 8. Kết thúc')
    print('='*30)
    select = int(input('Lựa chọn của bạn: '))
    return select

def usage_find_employee():
    print('='*30)
    print('Xin mời các chọn lựa sau đây')
    print('\t 1. Tìm theo tên')
    print('\t 2. Tìm theo chức vụ')
    print('\t 3. Tìm theo mã nhân viên')
    print('='*30)
    select = int(input('Lựa chọn của bạn: '))
    accept_fields = ['name', 'title', 'id']
    value = input('Nhập gía trị tìm kiếm: ')
    return accept_fields[select], value

def usage_add_employee_also():
    print('='*30)
    print('Bạn có muốn thêm nhân viên luôn không ?')
    print('\t 1. Có')
    print('\t 2. Không')
    print('='*30)
    select = int(input('Lựa chọn của bạn: '))
    return select

def display_employees(data):
    print('{0:>10} | {1:>20} | {2:>20} | {3:>20} | {4:>20} | {5:>20}'.format('Mã NV', 'Tên', 'Chức Danh', 'Tuổi', 'Địa chỉ', 'Phòng'))
    print('-'*120)
    for item in data:
        print('{0:>10} | {1:>20} | {2:>20} | {3:>20} | {4:>20} | {5:>20}'.format(item['id'], item['name'], item['title'], item['age'], item['address'], item['department']))
    print('-'*120)

def display_department(data):
    print('{0:>10} | {1:>30}'.format('Mã NV', 'Tên'))
    print('-'*50)
    for item in data:
        print('{0:>10} | {1:>30}'.format(item['id'], item['name']))
    print('-'*120)

def display_department_count_employees(data):
    print('{0:>10} | {1:>30} | {2:>30}'.format('Mã NV', 'Tên', 'Tổng nhân viên'))
    print('-'*120)
    for item in data:
        print('{0:>10} | {1:>30} | {2:>30}'.format(item['id'], item['name'], item['count_emp']))
    print('-'*120)
if __name__ == "__main__":
    select = 0
    while True:
        select = usage_first_menu()
        if select == 8:
            print("Hẹn gặp bạn lần sau")
            break
        if select == 1:
            print("Bạn đã chọn: Chức năng 1 - Danh sách Nhân viên")
            display_employees(actions.list_employee())
        elif select == 2:
            print("Bạn đã chọn: Chức năng 2 - Danh sách Phòng Ban")
            display_department(actions.list_department())
        elif select == 3:
            print("Bạn đã chọn: Chức năng 3 - Danh sách Phòng Ban và số lượng Nhân Viên")
            display_department_count_employees(actions.list_department_and_count_employee())
        elif select == 4:
            print("Bạn đã chọn: Chức năng 4 - Thêm nhân Viên mới")
            new_nv = ModelEmployee.input_employee()
            actions.add_new_employee(new_nv)
        elif select == 5:
            print("Bạn đã chọn: Chức năng 5 - Thêm Phòng Ban mới")
            new_dept = ModelDepartment.input_department()
            actions.add_new_department(new_dept)
        elif select == 6:
            print("Bạn đã chọn: Chức năng 6 - Thêm Phòng Ban cùng Nhân Viên")
            new_dept = ModelDepartment.input_department()
            is_add_nv = usage_add_employee_also()
            if is_add_nv == 1:
                while True:
                    new_nv = ModelEmployee.input_employee()
                    new_dept.employees.append(new_nv)
                    is_cont = input("Continue ? (y/n)")
                    if is_cont == 'n':
                        break
            actions.add_new_department(new_dept)
        elif select == 7:
            select_field, value_search = usage_find_employee()
            display_employees(actions.find_employee(select_field, value_search))
