person = {
    "name" : "Sivagami",
    "age" : 42,
    "city" : "Coimbatore"
}

print(person["name"])
print(person["age"])
print(person["city"])

print(person["name"], "is", person["age"], "years and lives in", person["city"])


students = [
    {"Name": "Sivagami", "age":42, "mark": 65},
    {"Name": "Mohan", "age":43, "mark": 72},
    {"Name": "Akshanth", "age":15, "mark": 91},
    {"Name": "Dhanvanth", "age": 10, "mark": 87}
]
def get_grade(mark):
    if mark > 90:
        return("Grade A")
    elif mark>80:
        return("Grade B")
    elif mark > 70:
        return("Grade C")
    else:
        return("Grade D")

for student in students:
    grade = get_grade(student["mark"])

    print(student["Name"], "scored", student["mark"], "and got", grade)


expenses = [
    {"item": "Rice", "price": 65, "quantity": 5},
    {"item": "sugar", "price":43, "quantity": 3},
    {"item": "book", "price": 125, "quantity": 7},
    {"item": "oil", "price": 90, "quantity": 5}
]
highest_cost = float("-inf")
expensive_item = ""
grand_total = 0
chepest_cost = float("inf")
chepest_item = ""
total_item = len(expenses)

def get_total(price,quantity):
    return price*quantity

for expense in expenses:
    total_exp = get_total(expense["price"], expense["quantity"])
    print(expense["item"], expense ["price"], "*" ,expense ["quantity"], "=", total_exp)
    grand_total+= total_exp
    
    
    if total_exp > highest_cost:
        highest_cost = total_exp
        expensive_item = expense["item"]
    
    if total_exp < chepest_cost:
        chepest_cost = total_exp
        chepest_item = expense["item"]

    if total_exp > 400:
        print(expense["item"],"*", expense["price"], "=", total_exp)
    
    if total_exp<300:
        print(expense["item"])

    average_item = grand_total/total_item
    
    
   

print("average expenses",average_item)
print("Grand_Total:", grand_total)   
print("Highest_Cost:", highest_cost)
print("Expensive_Item:",expensive_item )
print("Chepest_Item:", chepest_item)
print("Chepest_cost:", chepest_cost)