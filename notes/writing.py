#Alec George, writing to text notes
import csv


"""
r = to read the file
w = write on a file (replaces old file)
w+ = read and write
a = append (adds to the file, doesn't delete them, create the file if it doesn't exist)
x = create a file
a+ = append and read
"""

with open("notes/test.txt", "w") as f:
    f.write("Created using write mode.")

with open("notes/test.txt", "r") as file:
    print(file.read())
data = [
    {"username": "isougfgijngvksuhgvp", "color": "beige"},
    {"username": "fdoiuhfnbvoafbh", "color": "dark beige"},
    {"username": "hgvosbnvoisbf", "color": "light beige"},
    {"username": "vpoiushfgogafsg", "color": "beigish beige"},
    {"username": "goishfgos", "color": "a color close to beige"},
    {"username": "gosfhdnafdoi", "color": " beigish beige"},
    {"username": "vgaifgbaiug", "color": "green beige"}
]

data_2 = [
    {"username": "fgaofdhboadf", "color": "beige"},
    {"username": "dfavclkhoi", "color": "dark beige"},
    {"username": "aiufodhiua", "color": "light beige"},
    {"username": "gtialfoudfhgi", "color": "beigish beige"},
    {"username": "goishgoaisfhffgos", "color": "a color close to beige"},
    {"username": "fadfihv", "color": " beigish beige"},
    {"username": "gpiaujfdnhapdhf", "color": "green beige"}
]



with open("notes/user_info.csv", "w", newline="") as file:
    fieldnames = ["username", "color"]
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(data_2)





with open("notes/user_info.csv","r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(f"username: {row[0]}, color: {row[1]}")