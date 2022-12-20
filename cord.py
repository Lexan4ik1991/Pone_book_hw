import csv
import os.path


db = []
Phone_book = "Phone_book.csv"
Phone_book_txt="Phone_book.txt"


def create(name='', surname='', number=''):
    global db
    global Phone_book

    for row in db:
        if (row[0] == name.title() and row[1] == surname.title() and row[2] == number):
            print("Контакт уже существует")
            return

    new_row = [name.title(), surname.title(), number]
    db.append(new_row)

    with open("Phone_book.csv", 'a', encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter=';', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_row)
    return "ok"

def create_txt(name='', surname='', number=''):
    global db
    global Phone_book
    if (db[0] == name.title() and db[1] == surname.title() and db[2] == number):
        print("Контакт уже существует")
        return
    with open("Phone_book.txt", 'a', encoding="utf-8") as f:
        for element in db:
            f.write(f'Фамилия: {element[0]}\n\nИмя: {element[1]}\n\nНомер телефона: {element[2]}\n')
            f.write('\n')
            f.close()

            #f.write(f'Фамилия: {db[0]}\n\nИмя: {db[1]}\n\nНомер телефона: {db[2]}\n\n\n')

    return "ok"

def retrive(name='', surname='', number=''):
    global db
    global Phone_book
    result = []
    for row in db:
        if (name != '' and row[0] != name.title()):
            continue
        if (surname != '' and row[1] != surname.title()):
            continue
        if (number != '' and row[2] != number):
            continue
        result.append(row)
    if len(result) == 0:
        return f'Контакты не найдены'
    else:
        return result

# def retrive_txt(name='', surname='', number=''):
#     # global db
#     # global Phone_book_txt
#     result = []
#     with open("Phone_book.txt", 'r', encoding="utf-8") as f:
#         for line in f:
#          if (name != '' and db[0] != name.title()):
#             continue
#          if (surname != '' and db[1] != surname.title()):
#             continue
#          if (number != '' and db[2] != number):
#             continue
#          result.append(line)
#     if len(result) == 0:
#         return f'Контакты не найдены'
#     else:
#         return result