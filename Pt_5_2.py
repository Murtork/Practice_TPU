import csv


def adding(filename, num_of_books):
    for i in range(num_of_books):
        book_name = input("Название книги: ")
        author = input("Авто книги: ")
        year = input("Год публикации: ")
        one_row = [book_name, author, year]
        with open(filename, "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(one_row)
        print("Добавлена новая строчка", end='\n')


def by_author(filename, author):
    found_books = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[1] == author:
                found_books.append(row)
        if found_books:
            print("Найденные книги автора")
            print(found_books)
        else:
            print("У автора", author, "нет книг")


filename = 'books.csv'

num_of_books = int(input("Кол-во добавляемых записей: "))
adding(filename, num_of_books)

author_find = input("Автор для поиска книг: ")
by_author(filename, author_find)
