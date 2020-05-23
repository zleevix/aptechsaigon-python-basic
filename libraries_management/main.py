import actions
from models import ModelBook, ModelAuthor
def usage_first_menu():
    print("*"*10 + "\tLIBRARIES MANAGEMENT SYSTEM\t" + "*"*10)
    print('Xin mời các chọn lựa sau đây')
    print('\t 1. Hiển thị danh sách sách')
    print('\t 2. Hiển thị danh sách tác giả')
    print('\t 3. Hiển thị danh sách tác giả và số lượng sách')
    print('\t 4. Nhập thêm sách mới')
    print('\t 5. Nhập thêm tác giả mới')
    print('\t 6. Nhập thêm tác giả và sách mới')
    print('\t 7. Tìm kiếm sách')
    print('\t 8. Kết thúc')
    print('='*30)
    select = int(input('Lựa chọn của bạn: '))
    return select

def usage_find_book():
    print('='*30)
    print('Xin mời các chọn lựa sau đây')
    print('\t 1. Tìm theo tên')
    print('\t 2. Tìm theo thể loại')
    print('\t 3. Tìm theo mã sách')
    print('='*30)
    select = int(input('Lựa chọn của bạn: '))
    accept_fields = ['name', 'category', 'id']
    value = input('Nhập gía trị tìm kiếm: ')
    return accept_fields[select], value

def usage_add_book_also():
    print('='*30)
    print('Bạn có muốn thêm sách luôn không ?')
    print('\t 1. Có')
    print('\t 2. Không')
    print('='*30)
    select = int(input('Lựa chọn của bạn: '))
    return select

def display_book(data):
    print('{0:>10} | {1:>20} | {2:>20} | {3:>20}'.format('Mã Sách', 'Tên', 'Thể Loại', 'Tác giả'))
    print('-'*90)
    for item in data:
        print('{0:>10} | {1:>20} | {2:>20} | {3:>20}'.format(item['id'], item['name'], item['category'], item['author']))
    print('-'*90)

def display_author(data):
    print('{0:>10} | {1:>30}'.format('Mã Tác giả', 'Tên'))
    print('-'*50)
    for item in data:
        print('{0:>10} | {1:>30}'.format(item['id'], item['name']))
    print('-'*120)

def display_author_count_books(data):
    print('{0:>10} | {1:>30} | {2:>30}'.format('Mã tác giả', 'Tên', 'Tổng sách'))
    print('-'*90)
    for item in data:
        print('{0:>10} | {1:>30} | {2:>30}'.format(item['id'], item['name'], item['count_book']))
    print('-'*90)
if __name__ == "__main__":
    select = 0
    while True:
        select = usage_first_menu()
        if select == 8:
            print("Hẹn gặp bạn lần sau")
            break
        if select == 1:
            print("Bạn đã chọn: Chức năng 1 - Danh sách Sách")
            display_book(actions.list_book())
        elif select == 2:
            print("Bạn đã chọn: Chức năng 2 - Danh sách Tác giả")
            display_author(actions.list_author())
        elif select == 3:
            print("Bạn đã chọn: Chức năng 3 - Danh sách tác giả và số lượng sách")
            display_author_count_books(actions.list_author_and_count_book())
        elif select == 4:
            print("Bạn đã chọn: Chức năng 4 - Thêm sách mới")
            new_book = ModelBook.input_book()
            actions.add_new_book(new_book)
        elif select == 5:
            print("Bạn đã chọn: Chức năng 5 - Thêm Tác giả")
            new_author = ModelAuthor.input_author()
            actions.add_new_author(new_author)
        elif select == 6:
            print("Bạn đã chọn: Chức năng 6 - Thêm Tác giả và sách")
            new_author = ModelAuthor.input_author()
            is_add_book = usage_add_book_also()
            if is_add_book == 1:
                while True:
                    new_book = ModelBook.input_book()
                    new_author.books.append(new_book)
                    is_cont = input("Continue ? (y/n)")
                    if is_cont == 'n':
                        break
            actions.add_new_author(new_author)
        elif select == 7:
            select_field, value_search = usage_find_book()
            display_book(actions.find_book(select_field, value_search))
