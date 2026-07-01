'''#Q1
# Functions help us reuse code and make programs easier to manage

def welcome():
    print("Welcome to Python Programming!")

# Calling the function
welcome()'''

#Q2
'''# Function with one parameter

def greet(name):
    print("Hello,", name + "! Welcome back.")

# Calling function with different names
greet("Rushabh")
greet("Rahul")'''

#Q3
'''# Default parameters allow a value to be used when no argument is passed
def show_message(message="Hello"):
    print(message)

# Using default value
show_message()

# Passing a custom value
show_message("Good Night!!")'''

'''#Q4
# Function using return
def calculate_sum(a, b):
    return a + b

result = calculate_sum(10, 20)

print("Sum =", result)

# Difference between print() and return()

def display_sum(a, b):
    print("Sum inside function =", a + b)

display_sum(5, 10)'''

'''#Q5
# Function to display student information
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

# Positional Arguments
# Values are passed according to position
student_info("Rushabh", 20)

print()

# Keyword Arguments
# Values are passed using parameter names
student_info(age=20, name="Rushabh")'''

'''#Q6
# Function to calculate square
def square(num):
    return num ** 2

# Function to calculate cube

def cube(num):
    return num ** 3

number = int(input("Enter a number: "))

print("Square =", square(number))
print("Cube =", cube(number))'''

#Q7
'''# Recursive function for countdown
def countdown(n):

    # Base case
    if n == 0:
        return

    print(n)

    countdown(n - 1)

# Function call
countdown(10)'''

#Q8
'''# Recursive factorial function
def factorial(n):

    # Base case
    # Factorial of 0 and 1 is 1
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

number = int(input("Enter a number: ")) #Input from user for which factorial is to be calculated

print("Factorial =", factorial(number))'''
'''#Q9
# Global variable
sum = 0

def add_value(x):

    # Using global keyword
    global sum

    sum += x

    local_var = "Inside Function"

    print("Current sum =", sum)

# Calling function multiple times

add_value(10)
add_value(20)
add_value(30)

# Local variables work only inside functions
# Uncommenting below line will cause an error

# print(local_var)'''

'''#Q10
#Function to take num from user
def get_number():
    return int(input("Enter a number (0 to exit): "))

# Function to check even or odd

def is_even(num):
    return num % 2 == 0

# Function with default parameter

def power(base, exp=2):
    return base ** exp

# Function to display result

def show_result(num):

    if is_even(num):
        print("The number is Even")
    else:
        print("The number is Odd")

    print("Square =", power(num))

# Main Program

while True:

    number = get_number()

    if number == 0:
        print("Program Ended")
        break

    show_result(number)

    print("-" * 25)'''

"""def square (a):
    return a**2
a= int(input("Enter a numbeer to calculate sqaure:"))
result = square(a)
print("Square of", a, "is", result)"""