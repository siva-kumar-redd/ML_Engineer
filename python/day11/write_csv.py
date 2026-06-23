import csv

with open("employee.csv","w",newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["name","salary"])
    writer.writerow(["siva",20000])
    writer.writerow(["kumar",50000])
