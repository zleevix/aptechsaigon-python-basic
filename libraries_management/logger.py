log_file_name = 'libraries-management.log'

def write_file(action, data):
    with open(log_file_name,'a+', encoding = 'utf-8') as file:
        file.write("="*100 + "\n") 
        file.write(f"Hành động: {action}\n")
        file.write(f"Giá trị: {data}\n")
        file.write("="*100 + "\n")