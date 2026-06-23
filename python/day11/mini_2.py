import csv


with open("students.csv","r") as file:
    reader = csv.reader(file)

    next(reader)
    count=0
    for row in reader:
        print(row[0])
        count+=1
    print(count)
    
    

