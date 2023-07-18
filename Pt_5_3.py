import csv


def search_by_year(filename, start, end):
    try:
        if int(start) > int(end):
            print("Начальный год больше последнего")
            return
    except ValueError:
        print("Некорректные ввод срока")
        return

    found_books = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if (int(row[2]) > int(start)) & (int(row[2]) < int(end)):
                found_books.append(row)
    if found_books:
        print("Книги выпущенные в веденном промежутке: ")
        print(found_books)
    else:
        print("Книг в выбранном промежутке нет")


filename = 'books.csv'

start_year = input("Введите начальный год (включительно): ")
end_year = input("Введите последний год (включительно): ")
search_by_year(filename, start_year, end_year)
