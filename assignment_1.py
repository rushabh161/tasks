'''#Q1
full_name = "Rushabh Ratnaparkhi" #String variable to store the full name
age = 20 #Integer variable to store the age
height = float(1.78) #Float variable to store the height
is_student = True #Boolean variable to store the student status
print("Full Name:", full_name, type(full_name)) #Prints the full name and its data type
print("Age:", age, type(age)) #Prints the age and its data type
print("Height:", height, type(height)) #Prints the height and its data type
print("Is Student:", is_student, type(is_student)) #Prints the student status and its data type
'''
'''#Q2
# Creating variables of different data types
name = "JAVA"
number = 65
percentage = 90.25
passed = True

# Printing variables and their data types
print("Name:", name, "-", type(name))
print("Number:", number, "-", type(number))
print("Percentage:", percentage, "-", type(percentage))
print("Passed:", passed, "-", type(passed))

# Type conversion examples
converted_float = float(number)
converted_int = int(percentage) # int() removes the decimal part

print("\nAfter Conversion:")
print("Integer to Float:", converted_float)
print("Float to Integer:", converted_int)'''

'''#Q3
a = 10
b = 3
print("Addition:", a + b) # Addition of a and b
print("Subtraction:", a - b) # Subtraction of b from a
print("Multiplication:", a * b) # Multiplication of a and b
print("Division:", a / b) # Division of a by b
print("Modulus:", a % b) # Modulus of a by b
print("Exponentiation:", a ** b) # a raised to the power of b
print("Floor Division:", a // b) # Floor division of a by b

# / is used for regular division which returns a float
# // is used for floor division which returns the largest integer less than or equal to the result of the division.

print("\n Example")
print("10/3", "=", 10/3)
print("10//3", "=", 10//3)'''

'''#Q4
x = 25
y = 30
z = 25

print("Is x greater than y?", x > y)

print("Is x equal to z?", x == z)

print("Is x less than or equal to y AND y not equal to z?",x <= y and y != z)

print("Is x greater than y OR x equal to z?",x > y or x == z)'''

'''#Q5
# Taking user input 
name = input("Enter your name:") # input() returns a string
birth_year = int(input("Enter your birth year:")) # Therefore birth year must be converted into integer
current_year = 2026
age = current_year - birth_year # Calculating age by subtracting birth year from current year

print("\nHello", name)
print("Your age is", age)'''

'''#Q6
# Taking user inputs

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))

bmi = weight / (height ** 2) # BMI Formula

print("Your BMI is:", round(bmi, 2))# Displaying BMI rounded to 2 decimal places'''

'''#Q7
"""Rectangle Calculator Program
   This program calculates
   the area and perimeter
   of a rectangle."""

# User enters rectangle length
length = float(input("Enter length: "))

# User enters rectangle width
width = float(input("Enter width: "))

# Area helps determine occupied space
area = length * width

# Perimeter helps determine total boundary length
perimeter = 2 * (length + width)

# Display calculated area
print("Area =", area)

# Display calculated perimeter
print("Perimeter =", perimeter)'''

#Q8
'''# Creating list and score variable

fruits = ["mango", "apple", "banana", "cherry"]
score = 50

# Adding 25 using assignment operator
score += 25

print("Updated Score:", score)

# Membership operator
print("Is apple in fruits list?",
      "apple" in fruits)

# Not membership operator
print("Is grape not in fruits list?",
      "grape" not in fruits)'''

#Q9
#Taking user input for name,age and city
name = input("Enter your name:")
age = int(input("Enter your age:"))
city = input("Enter your city:")

#Taking marks from user for three subjects
marks_1 = float(input("Enter marks for ssub 1:"))
marks_2 = float(input("Enter your marks fro sub 2:"))
marks_3 = float(input("Enter your marks for sub 3:"))

#Calculatiung total marks
total_marks = marks_1 + marks_2 + marks_3

#calculating percentage
percentage = (total_marks / 3)

#Displaying the results
print("\n ----Student Information----")
print("Name:", name)
print("Age:", age)
print("City:", city)
print("Total Marks:", total_marks)
print("Percentage:", round(percentage, 2), "%")