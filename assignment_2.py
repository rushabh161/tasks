'''# Ask user to enter their age
age = int(input("Enter your age: "))

# Check if age is 18 or above
if age >= 18:
    print("You are eligible to vote.")

# If condition is false, nothing will be printed'''

#Q2
'''# Enter any number from user
num = int(input("Enter any number: "))

# Check whether number is even or odd
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")'''

'''#Q3
# Enter marks from user
marks = int(input("Enter marks: "))

# Assign grade according to marks
if marks >= 90:
    print("Grade A - Excellent")

elif marks >= 75:
    print("Grade B - Good")

elif marks >= 60:
    print("Grade C - Average")

elif marks >= 40:
    print("Grade D - Pass")

else:
    print("Fail")'''

'''#Q4
# Program using for loop and range()

# a) Print all numbers from 1 to 30
print("Numbers from 1 to 30:")

# range(1, 31) generates numbers from 1 to 30
for i in range(1, 31):
    print(i)

# b) Print all odd numbers from 1 to 50
print("\nOdd numbers from 1 to 50:")

for i in range(1, 51, 2):
    print(i)

# c) Print the sum of numbers from 1 to 15
total = 0

# range(1, 16) generates numbers from 1 to 15
for i in range(1, 16):
    total += i

print("\nSum of numbers from 1 to 15 =", total)'''

'''#Q5
# Program using while loop to print numbers from 1 to 20
# and their cubes

i = 1

while i <= 20:
    print("Number =", i, "Cube =", i ** 3)
    i += 1'''

#Q6
# Program to keep taking positive numbers from user
# and add them to a running total

total = 0

while True:
    num = int(input("Enter a positive number: "))

    if num <= 0:
        break

    total += num

print("Total Sum =", total)

'''#Q7
# Program to give advice based on temperature and rain

temperature = int(input("Enter temperature: "))
is_raining = input("Enter yes or no: ")

if temperature > 30:

    if is_raining == "no":
        print("Hot day, wear light clothes.")

    else:
        print("Hot and rainy, carry umbrella.")

elif temperature < 15:

    if is_raining == "yes":
        print("Cold and rainy, wear jacket and take umbrella.")

    else:
        print("Cold day, wear warm clothes.")

else:
    print("Weather is pleasant.")'''

'''#Q8
# FizzBuzz Program

for i in range(1, 41):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)'''

'''#Q9
# Create a simple calculator

while True:

    print("\nCalculator Menu")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Multiply two numbers")
    print("4. Divide two numbers")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Exiting Calculator...")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result =", num1 + num2)

    elif choice == 2:
        print("Result =", num1 - num2)

    elif choice == 3:
        print("Result =", num1 * num2)

    elif choice == 4:

        if num2 == 0:
            print("Division by zero is not allowed")

        else:
            print("Result =", num1 / num2)

    else:
        print("Invalid Choice!")'''

'''#Q10
# Take input and convert it into integer
num = int(input("Enter a number: "))

# Fixed missing colons and indentation
if num > 100:
    print("Large number")

elif num > 50:
    print("Medium number")

else:
    print("Small number")

# Initialize counter
count = 1

# Fixed while loop syntax
while count < 10:
    print(count)

    # Increment counter
    count = count + 1'''