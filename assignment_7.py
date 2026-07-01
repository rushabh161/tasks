#Q1
'''# a) Tuple with 5 numbers

numbers = (10, 20, 30, 40, 50)

# b) Mixed tuple

mixed = (10, "Rushabh", 5.5, True)

# c) Empty tuple - Method 1

empty1 = ()

# Empty tuple - Method 2

empty2 = tuple()

# d) Single element tuple

single = (99,)

# Important:
# A comma is required for a single-element tuple.
# (99) is treated as an integer, not a tuple.

print("num",numbers, type(numbers))
print("mixed",mixed, type(mixed))
print("empty1",empty1, type(empty1))
print("empty2",empty2, type(empty2))
print("single",single, type(single))'''

#Q2
'''# Tuple Packing

student = "Rushabh", 20, "Pune"

print(student)
print(type(student))

# Tuple Unpacking

name, age, city = student

print("Name =", name)
print("Age =", age)
print("City =", city)'''

#Q3
'''colors = ('red', 'green', 'blue', 'yellow', 'purple', 'orange')

print("First Element =", colors[0])

print("Third Element =", colors[2])

print("Last Element =", colors[-1])

print("Second Last Element =", colors[-2])

index = int(input("Enter Index: "))

print("Element =", colors[index])'''
#Q4
'''numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# tuple[start:end:step]

print("Index 2 to 7 =", numbers[2:8])

print("First 5 Elements =", numbers[:5])

print("Last 4 Elements =", numbers[-4:])

print("Every Second Element =", numbers[::2])

print("Reverse Tuple =", numbers[::-1])'''
#Q5
'''matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print("First Row =", matrix[0])

print("Second Row Third Column =", matrix[1][2])

print("Third Row First Column =", matrix[2][0])'''
#Q6
'''student = ('Rahul', 20, 'Computer Science', 'A')

# Iteration

for item in student:
    print(item)

# Unpacking

name, age, branch, grade = student

print("Name =", name)
print("Age =", age)
print("Branch =", branch)
print("Grade =", grade)'''
#Q7
'''grades = ('A', 'B', 'A', 'C', 'A', 'B', 'D', 'A', 'B')

print("Count of A =", grades.count('A'))

print("Count of B =", grades.count('B'))

grade = input("Enter Grade: ")

print("Count of C =", grades.count(grade))'''
#Q8
'''fruits = ('apple', 'banana', 'cherry', 'banana', 'mango', 'apple')

print("First Banana =", fruits.index('banana'))

print("Banana Starting Search from Index 2 =",
      fruits.index('banana', 2))

try:

    print(fruits.index('kiwi'))

except ValueError:

    print("Not Found")'''
#Q9
'''coordinates = (10, 20)

# Tuples are immutable

# coordinates[0] = 100
# Error:
# TypeError: 'tuple' object does not support item assignment

# coordinates.append(30)
# Error:
# AttributeError: 'tuple' object has no attribute 'append'

# Correct Method

temp = list(coordinates)

temp[0] = 100

temp.append(30)

coordinates = tuple(temp)

print(coordinates)'''
#Q10
# Student Record Program

name = input("Enter Name: ")

roll = int(input("Enter Roll Number: "))

m1 = int(input("Enter Mark 1: "))
m2 = int(input("Enter Mark 2: "))
m3 = int(input("Enter Mark 3: "))

# Tuple Packing

student = name, roll, m1, m2, m3

print("\nComplete Record:")
print(student)

# Tuple Unpacking

name, roll, m1, m2, m3 = student

print("\nStudent Details")

print("Name =", name)
print("Roll Number =", roll)
print("Mark 1 =", m1)
print("Mark 2 =", m2)
print("Mark 3 =", m3)

search_mark = int(input("\nEnter Mark to Count: "))

print("Count =", student.count(search_mark))

# Nested Tuple

student2 = ("Rahul", 102, 75, 80, 85)

records = (student, student2)

print("\nNested Tuple:")
print(records)

print("\nFirst Student Name =", records[0][0])

print("Second Student Roll Number =", records[1][1])