import init_bd
from os.path import exists
def init_csv():
    file = 'Phone_book.csv'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'Имя;Фамилия;Номер телефона\n')

def pb_whereis():
    path = 'Phone_book.csv'
    valid = exists(path)
    if not valid:
        init_csv()