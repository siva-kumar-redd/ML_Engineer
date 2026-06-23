import csv


with open("student.csv","r") as file:

    reader = csv.reader(file)

    next(reader)
    count=0
    for row in reader:
        count += 1
    print(count)