import csv

header = ["Book", "Author", "Year of Release"]
books = [["Wolf and Spice", "Isuna Hasekura", "2006"],
         ["OnePunchMan", "Yusuke Murata", "2009"],
         ["Toradora", "Yuyuko Takemiya", "2004"],
         ["Made in Abyss", "Akihito Tsukushi", "2012"],
         ["Crime and Punishment", "Fyodor Dostoevsky", "1866"]]

filename = "books.csv"

with open(filename, "w", encoding="utf-8", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(books)
