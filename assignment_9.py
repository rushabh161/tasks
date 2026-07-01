'''#Q1
#a)Dictionary using two diff ways:
empty_1= {}
empty_2= dict()

#b)Dictionary with string keys:
student= {
    "Name":"Rushabh",
    "City":"Bhusawal",
    "Course":"AiML"

}
#c) Dictionary with int keys:
integer={
    1:99,
    2:95,
    3:90,
    4:85,
    5:80
}
#d)Dictionary with mixed data type:
mix_type={
    "Name":"Rushabh",
    "Age":20,
    "Cgpa":8.5
}

print(type(empty_1),empty_1)
print(type(empty_2),empty_2)
print(type(student),student)
print(type(integer),integer)
print(type(mix_type),mix_type)'''

#Q2
'''student = {
 "name": "Rushabh",
 "age": 20,
 "city": "Bhusawal",
 "marks": 76
}
#Print the value of "name" using square brackets.
print("Name:",student["name"])
#Update the "marks" to 92.
student["marks"]= 92
print("Updated marks:",student["marks"])
#Add a new key "grade" with value "A".
student["grade"]="A"
#Print the updated dictionary.
print("Updated Dictionary:")
print(student)'''

'''#Q3
person = {"name": "Priya", "age": 21, "profession": "Engineer"}
#a) Using get() to access "age" and a non-existing key "salary" (with default value).
print("Age =", person.get("age"))
print("Salary =", person.get("salary", "Not Available"))
#b) Print all keys using keys().
print("\nAll keys:")
print(person.keys())
#c) Print all values using values().
print("\n All values:")
print(person.values())
#d) Print all key-value pairs using items().
print("\nItems:")
print(person.items())'''

#Q4
'''students = {
 "s1": {"name": "Rahul", "age": 20, "marks": 88},
 "s2": {"name": "Sneha", "age": 21, "marks": 95}
}
#Print the details of the first student.
print("Details of s1:")
print(students.get("s1"))
#Print the marks of the second student.
print("\nMarks of the second student:")
print(students["s1"]["marks"])
#Add a new subject "math" with marks 90 for the first student.
students["s1"]["math"]=90

print("\n Updated Profile...")
print(students)'''

#Q5
'''info = {"brand": "Samsung", "model": "A52", "price": 25000}
#Update it with new information: {"color": "Black", "price": 24000}.
info.update({
    "color":"Black",
    "price":24000
})

#Remove the key "model" using pop() and print the removed value.
removed_value = info.pop("model")
print("Removed Value =", removed_value)

#Print the final dictionary.
print("\nFinal Dictionary:")
print(info)'''

#Q6
'''# Dictionary with 5 key-value pairs
data = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40,
    "e": 50
}

print("Original Dictionary:")
print(data)

# popitem() removes the last inserted key-value pair
removed1 = data.popitem()
print("\nFirst Removed Item:")
print(removed1)

removed2 = data.popitem()

print("\nSecond Removed Item:")
print(removed2)

print("\nDictionary After popitem():")
print(data)

# clear() removes all items
data.clear()
print("\nAfter clear():")
print(data)

# Difference:
# pop(key) removes a specific key.
# popitem() removes the last inserted key-value pair.'''

#Q7
'''# Original Dictionary

d = {
    "a": 1,
    "b": 2
}

# Creating a copy

copied_dict = d.copy()

# Add key c if not present

d.setdefault("c", 3)

# Existing key a remains unchanged

d.setdefault("a", 100)

print("Original Dictionary:")
print(d)

print("\nCopied Dictionary:")
print(copied_dict)'''

#Q8
#creating a dic using fromkeys()
'''keys=["name","age","city"]
person=dict.fromkeys(keys,None)

print("Initial Dictionary:")
print(person)

#Taking user input
person["name"]=input("Enter your name:")
person["age"]=int(input("Enter your age:"))
person["city"]=input("Enter your city:")

print("\nUpdated Dictionary:")
print(person)

# Checking key existence

search_key = input("\nEnter Key to Search: ")

if search_key in person:
    print("Key Exists")

else:
    print("Key Does Not Exist")'''


#Q9
'''# Dictionary to store contacts
contacts = {}

# Taking user input
name = input("Enter Name: ")
phone = input("Enter Phone Number: ")
email = input("Enter Email: ")

# Storing data
contacts[name] = {
    "phone": phone,
    "email": email
}

# Searching contact
search_name = input("\nEnter Name to Search: ")

result = contacts.get(search_name)

if result:
    print("Contact Found:")
    print(result)

else:
    print("Contact Not Found")

# Display all contacts
print("\nAll Contacts:")

for key, value in contacts.items():
    print(key, ":", value)'''

#Q10
'''# Student Management System

students = {}

while True:

    print("\n===== MENU =====")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Remove Student")
    print("6. Exit")

    choice = int(input("Enter Choice: "))

    # Add Student
    if choice == 1:

        roll = input("Enter Roll Number: ")

        name = input("Enter Name: ")

        age = int(input("Enter Age: "))

        marks = int(input("Enter Marks: "))

        students[roll] = {
            "name": name,
            "age": age,
            "marks": marks
        }

        print("Student Added Successfully")

    # Update Marks

    elif choice == 2:

        roll = input("Enter Roll Number: ")

        if roll in students:

            new_marks = int(input("Enter New Marks: "))

            students[roll].update({"marks": new_marks})

            print("Marks Updated")

        else:

            print("Student Not Found")

    # Search Student

    elif choice == 3:

        roll = input("Enter Roll Number: ")

        student = students.get(roll)

        if student:

            print(student)

        else:

            print("Student Not Found")

    # Display All Students

    elif choice == 4:

        if len(students) == 0:

            print("No Student Records Found")

        else:

            for roll, details in students.items():

                print("\nRoll Number:", roll)

                print(details)

    # Remove Student

    elif choice == 5:

        roll = input("Enter Roll Number: ")

        removed = students.pop(roll, None)

        if removed:

            print("Student Removed")

        else:

            print("Student Not Found")

    # Exit

    elif choice == 6:

        print("Exiting Program...")

        break

    else:

        print("Invalid Choice")'''