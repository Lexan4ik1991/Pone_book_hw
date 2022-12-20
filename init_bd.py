import csv
import os.path

db = []
Phone_book = "Phone_book.csv"

def import_csv():
    with open("Phone_book.csv", encoding='utf-8') as r_file:
     file_reader = csv.reader(r_file, delimiter = ",")
     for row in file_reader:
            print(f'{row}')

def import_txt():
    global db
    with open("Phone_book.txt",'r',encoding="utf-8") as f:
        for line in f:
            print(line.rstrip('\n'))



