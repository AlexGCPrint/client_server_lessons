import csv

def get_data():
    files_li = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    os_prod_li = []
    os_name_li = []
    os_code_li = []
    os_type_li = []
    result_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for file in files_li:
        with open(file, 'r', encoding='cp1251') as f_n:
                data = f_n.read().split('\n')
                for string in data:
                    row_data = string.split(':')
                    if 'Изготовитель системы' in row_data[0]:
                        os_prod_li.append(row_data[1].strip())
                    if 'Название ОС' in row_data[0]:
                        os_name_li.append(row_data[1].strip())
                    if 'Код продукта' in row_data[0]:
                        os_code_li.append(row_data[1].strip())
                    if 'Тип системы' in row_data[0]:
                        os_type_li.append(row_data[1].strip())
                result_data.append(
                    [
                        os_prod_li[:1][0],
                        os_name_li[:1][0],
                        os_code_li[:1][0],
                        os_type_li[:1][0]
                    ]
                )
    # print(result_data)
    return result_data

def write_to_csv(file_name):
    with open(file_name, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        # print(get_data())
        for row in get_data():
            csv_writer.writerow(row)

write_to_csv('csv_task_1')

