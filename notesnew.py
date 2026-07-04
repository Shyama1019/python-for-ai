file = open("newoutput.txt", "r")
content = file.read()
print(content)
file.close()



file = open("newoutput.txt", "w")
file.write("I am learning python\n")
file.write("i love to become an ai engineer\n")
file.write("I love my family\n")
file.close()


file = open("newoutput.txt", "a")
file.write("I am learning python\n")
file.write("i love to become an ai engineer\n")
file.write("I love my family\n")
file.close()


with open("newoutput.txt", "w") as file:
    file.write("I am learning python\n")
    file.write("i love to become an ai engineer\n")
    file.write("I love my husband\n")

import csv
with open("new.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

import csv

with open("new.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], "is", row["age"], "years old and scored", row["score"])


import csv

students = [
    {"name": "Sivagami", "age": 42, "score": 65},
    {"name": "Mohan", "age": 43, "score": 45},
    {"name": "Akshanth", "age": 15, "score": 95},
]

def get_grade(score):
    if score > 90:
        return("Grade A")
    elif score > 80:
        return ("Grade B")
    elif score > 70:
        return ("Grade C")
    else:
        return("Grade D")
for student in students:
    grade = get_grade(student["score"])

    print(student["name"], "scored", student["score"],"and got",grade)

import csv
def get_grade(score):
    if score > 90:
        return("Grade A")
    elif score > 80:
        return ("Grade B")
    elif score > 70:
        return ("Grade C")
    else:
           return("Grade D")
    
with open("results.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        grade = get_grade(int(row["score"]))
        row ["grade"]= grade
        print(row["name"], "is", row["age"], "years old and scored", row["score"], "got", grade)



with open("results.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "score", "grade"])
    writer.writeheader()
    for student in students:
        writer.writerow(student)


grocery_item = []
count= int(input("How many grocery_items?"))

for i in range(count):
    item = input("Enter the item_name:")
    price = input("Enter the price")
    quantity = input("Enter the quantity")

    grocery_item.append({
    "item": item,
    "price": price,
    "quantity":quantity
})
print(grocery_item)

    
students_mark = [{
    "name":"Mohan","Maths": 67, "Tamil": 32, "English": 45},
    {"name":"Ramu", "Maths": 82, "Tamil": 56, "English": 67},
    {"name":"Sivagami","Maths": 56, "Tamil":56, "English": 78},
    {"name":"Akshanth","Maths": 65, "Tamil":54, "English":67},
    {"name":"Dhanvanth","Maths":56, "Tamil":65, "English":74

}]


def total_marks(Maths,Tamil,English):
    return Maths+Tamil+ English

for student in students_mark:
    total = total_marks(
        student["Maths"],
        student["Tamil"],
        student["English"]
    )
    average = total/3

    if average  > 65:
        print("Grade A")
    elif average  > 60:
        print("Grade B")
    else:
        print("Grade C")



    print(student["name"])
    print(total)
    print(average)

