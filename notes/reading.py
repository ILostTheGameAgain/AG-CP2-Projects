# Alec George, Reading files python notes
import csv

with open("notes/test.txt", "r") as file:
    content = file.read()
    print(content)


#print(content)


users  = {}

with open("notes/user_info.csv") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        users.update({row[0]: row[1]})
        print(row)


    