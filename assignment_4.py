'''#Q1
#Using def function
def square (a):
    return a**2
a= int(input("Enter a number to calculate sqaure:"))
result = square(a)
print("Square of", a, "is", result)

#Using lambda function
square_lambda = lambda x:x**2 #
x = int(input("Enter a number to calculate square using Lambda:"))
result_lambda = square_lambda(x)
print("Square of", x, "using Lambda is", result_lambda)

#Difference between def and lambda:
#def function with a name and can contain n number of statements 
#Lambda function is an anaonymous function that contains single expression & is used for short, simple functions.'''

'''#Q2
#Lamda function for addition 
add_three = lambda a,b,c: a+b+c
a= int(input("Enter a number to add:"))
b= int(input("Enter a number to add:"))
c= int(input("Enter a number to add:"))
result_add = add_three(a,b,c)
print("Sum of",a,",",b,"and",c,"is", result_add)'''

'''#Q3
# For loop is used when the number of iterations is known
# a) Print numbers from 1 to 25
print("Numbers from 1 to 25:")

for i in range(1, 26):
    print(i)

# b) Find sum of numbers from 1 to 20
total = 0

for i in range(1, 21):
    total += i

print("\nSum of numbers from 1 to 20 =", total)

# c) Print table of 5
print("\nTable of 5:")

for i in range(1, 11):
    print("5 x", i, "=", 5 * i)'''

'''#Q4
#While loop
# Program to keep taking positive numbers
# and add them to a running total

total = 0

while True:

    num = int(input("Enter a positive number: "))

    if num <= 0:
        break

    total += num

print("Total Sum =", total)'''

'''#Q5
import math

# Taking number as input
num = float(input("Enter a number: "))

# Square root
print("Square Root =", math.sqrt(num))

# Factorial only for positive integers
if num >= 0 and num == int(num):
    print("Factorial =", math.factorial(int(num)))
else:
    print("Factorial can only be calculated for positive integers.")

# Ceiling value
print("Ceiling Value =", math.ceil(num))

# Floor value
print("Floor Value =", math.floor(num))

# Math module provides ready-made mathematical functions'''

'''#Q6
import random

# Generate 5 random integers between 1 and 100

print("Five Random Numbers:")

for i in range(5):
    print(random.randint(1, 100))

# Generate random number between 50 and 150

print("\nRandom Number (50 to 150):")
print(random.randint(50, 150))

# Generate random floating point number

print("\nRandom Float Number:")
print(random.random())'''

'''#Q7
# Method 1
import math

print("Using import math:")
print("2^4 =", math.pow(2, 4))

# Method 2
from math import sqrt

print("\nUsing from math import sqrt:")
print("Square Root of 25 =", sqrt(25))

# Method 3
import math as m

print("\nUsing alias m:")
print("Factorial of 5 =", m.factorial(5))'''

'''#Q8
import mymodule

mymodule.greet("Rushabh")

result = mymodule.calculate_power(2, 5)

print("Power =", result)'''

'''#Q9
# Function definition

def greet():
    print("Hello from Python!")

# This block runs only when this file is executed directly

if __name__ == "__main__":
    print("Program is running directly.")
    greet()'''

#Q10
import math
import random

# Lambda function
square = lambda x: x * x

# Function using math module
def power(base, exp):
    return math.pow(base, exp)

while True:

    print("\n===== MENU =====")
    print("1. Square")
    print("2. Power")
    print("3. Random Number")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        num = int(input("Enter a number: "))
        print("Square =", square(num))

    elif choice == 2:

        base = int(input("Enter base: "))
        exp = int(input("Enter exponent: "))

        print("Power =", power(base, exp))

    elif choice == 3:

        print("Random Number =", random.randint(1, 100))

    elif choice == 4:

        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")