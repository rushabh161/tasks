#Q1
'''# Q1 - Basic Class and Object

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

# Creating two objects
car1 = Car("Toyota", "Innova")
car2 = Car("Honda", "City")

print("--- Car 1 ---")
car1.display_info()

print("--- Car 2 ---")
car2.display_info()'''

'''# Q2 - Using __init__ Constructor

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_details(self):
        print("Title  :", self.title)
        print("Author :", self.author)
        print("Price  : Rs.", self.price)

# Creating two book objects
book1 = Book("Python Basics", "Guido van Rossum", 350)
book2 = Book("Let Us C", "Yashavant Kanetkar", 275)

print("--- Book 1 ---")
book1.show_details()

print("--- Book 2 ---")
book2.show_details()'''

'''# Q3 - Instance Methods and self

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited Rs.", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance = self.balance - amount
            print("Withdrawn Rs.", amount)

    def show_balance(self):
        print("Current Balance: Rs.", self.balance)

# Creating object and demonstrating methods
acc = BankAccount("Rushabh", 5000)

print("Account Holder:", acc.account_holder)
acc.show_balance()

acc.deposit(2000)
acc.show_balance()

acc.withdraw(1500)
acc.show_balance()

acc.withdraw(10000)  # This should show insufficient balance'''

'''# Q4 - Method with Parameters

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"

# Creating 3 student objects
s1 = Student("Aarav", 75)
s2 = Student("Sneha", 38)
s3 = Student("Rohan", 40)

students = [s1, s2, s3]

for s in students:
    print("Name:", s.name, "| Marks:", s.marks, "| Result:", s.calculate_grade())'''

'''# Q5 - Multiple Methods

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print("Name   :", self.name)
        print("Salary : Rs.", self.salary)

    def give_raise(self, amount):
        self.salary = self.salary + amount
        print("Raise given! New Salary: Rs.", self.salary)

    def yearly_bonus(self):
        bonus = self.salary * 10 / 100
        return bonus

# Creating employee object
emp = Employee("Vikram", 30000)

emp.display_details()
emp.give_raise(5000)

bonus = emp.yearly_bonus()
print("Yearly Bonus: Rs.", bonus)'''

# Q6 - Real-world Object Modeling

'''class MobilePhone:
    def __init__(self, brand, model, battery_percentage):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage

    def charge(self, percent):
        self.battery_percentage = self.battery_percentage + percent
        # Battery can't go above 100%
        if self.battery_percentage > 100:
            self.battery_percentage = 100
        print("Charged! Battery:", self.battery_percentage, "%")

    def use_phone(self, minutes):
        # 1% battery used per 10 minutes
        battery_used = minutes // 10
        self.battery_percentage = self.battery_percentage - battery_used
        if self.battery_percentage < 0:
            self.battery_percentage = 0
        print("Used phone for", minutes, "minutes. Battery:", self.battery_percentage, "%")

    def show_status(self):
        print("Brand  :", self.brand)
        print("Model  :", self.model)
        print("Battery:", self.battery_percentage, "%")

# Creating object and simulating usage
phone = MobilePhone("Samsung", "Galaxy A54", 40)

phone.show_status()
phone.charge(30)
phone.use_phone(50)
phone.use_phone(120)
phone.show_status()'''

# Q7 - Combining Concepts
'''
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display(self):
        print("Length    :", self.length)
        print("Width     :", self.width)
        print("Area      :", self.area())
        print("Perimeter :", self.perimeter())

# Taking input from user
length = float(input("Enter length: "))
width = float(input("Enter width: "))

rect = Rectangle(length, width)
rect.display()'''

# Q8 - Updating Attributes
'''
class Player:
    def __init__(self, name, score, level):
        self.name = name
        self.score = score
        self.level = level

    def increase_score(self, points):
        self.score = self.score + points
        print("Score updated! New Score:", self.score)

    def level_up(self):
        self.level = self.level + 1
        print("Level Up! Current Level:", self.level)

    def show_progress(self):
        print("Player :", self.name)
        print("Score  :", self.score)
        print("Level  :", self.level)

# Creating object and updating multiple times
p = Player("Rushabh", 0, 1)

p.show_progress()

p.increase_score(150)
p.increase_score(200)
p.level_up()

p.increase_score(300)
p.level_up()
p.level_up()

print("\n--- Final Progress ---")
p.show_progress()'''

'''# Q9 - Debugging OOP Code
# Original code had 3 errors. All fixed below with comments.

class Person:
    # FIX 1: 'self' was missing as first parameter in __init__
    def __init__(self, name, age):
        # FIX 2: self.name and self.age were not used
        # Without self, name and age are just local variables, not stored in the object
        self.name = name
        self.age = age

    # FIX 3: 'self' was missing as first parameter in introduce()
    def introduce(self):
        # FIX 4: print() needs commas between variables, not just spaces
        print("My name is", self.name, "and I am", self.age, "years old.")

p1 = Person("Rushabh", 20)
p1.introduce()'''

# Q10 - Mini Project: Simple Library Management System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "Available"  # Default status

    def issue_book(self):
        if self.status == "Available":
            self.status = "Issued"
            print("Book issued successfully:", self.title)
        else:
            print("Sorry, this book is already issued.")

    def return_book(self):
        if self.status == "Issued":
            self.status = "Available"
            print("Book returned successfully:", self.title)
        else:
            print("This book was not issued.")

    def show_info(self):
        print("Title  :", self.title)
        print("Author :", self.author)
        print("Status :", self.status)
        print("----------------------------")


# List to store all books
library = []

# Adding some default books at start
library.append(Book("Python Basics", "ABC Author"))
library.append(Book("Data Science 101", "XYZ Author"))
library.append(Book("Machine Learning", "PQR Author"))

# Menu using while loop
while True:
    print("\n===== Library Menu =====")
    print("1. Add a new book")
    print("2. Issue a book")
    print("3. Return a book")
    print("4. Show all books")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        new_book = Book(title, author)
        library.append(new_book)
        print("Book added:", title)

    elif choice == "2":
        title = input("Enter book title to issue: ")
        found = False
        for book in library:
            if book.title.lower() == title.lower():
                book.issue_book()
                found = True
                break
        if not found:
            print("Book not found in library.")

    elif choice == "3":
        title = input("Enter book title to return: ")
        found = False
        for book in library:
            if book.title.lower() == title.lower():
                book.return_book()
                found = True
                break
        if not found:
            print("Book not found in library.")

    elif choice == "4":
        if len(library) == 0:
            print("No books in library.")
        else:
            print("\n--- All Books ---")
            for book in library:
                book.show_info()

    elif choice == "5":
        print("Exiting Library System. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1 to 5.")