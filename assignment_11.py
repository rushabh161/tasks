'''#Q1
try:
    num1=int(input("Enter a num:"))
    num2=int(input("Enter a num"))

    result= num1/num2
    print("Result:" ,result)

except ValueError:
    print("Invalid input, Enter a number!!")'''

#Q2
'''try:
    num1=int(input("Enter a num for div:"))
    num2=int(input("Enter a num for div:"))

    result=num1/num2

    print("Div:", result)

except ZeroDivisionError:
    print("Div by zero not allowed!!")'''

#Q3
# Program demonstrating multiple exceptions

'''try:

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    result = num1 / num2

    print("Division Result:", result)

    text = input("Enter a Number as String: ")

    number = int(text)
    print(type(text))
    print(type(number))

    print("Converted Integer:", number)

except ZeroDivisionError:

    print("Cannot divide by zero.")

except ValueError:

    print("Invalid input. Please enter numbers only.")'''

#Q4
'''try:

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    result = num1 / num2

    print("Division Result:", result)

except ZeroDivisionError:

    print("Cannot divide by zero.")

except ValueError:

    print("Invalid input. Please enter numbers only.")
else:
    print("Division Performed Successfully!!")'''

#Q5
''''try:

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    result = num1 / num2

    print("Division Result:", result)

except ZeroDivisionError:

    print("Cannot divide by zero.")

except ValueError:

    print("Invalid input. Please enter numbers only.")


finally:
    print("Program Execution Completed!!")'''

#Q6
"""try:

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    result = num1 * num2

    print("Multiplication Result:", result)

except ZeroDivisionError:

    print("Cannot multiply by zero.")

except ValueError:

    print("Invalid input. Please enter numbers only.")

else:
    print("Multiplication performed successfully")

finally:
    print("Program Execution Completed!!")"""

#Q7
'''try:
    age_str=input("Enter your age:")
    age=int(age_str)

    if age<0:
        raise ValueError("Age can't be negative!!")
    print("Age:",age)

except ValueError as e:
    print("Error:",e)'''
#Q8
'''try:
    num=int(input("Enter a num:"))
    div= num/100

    print("Div:",div)

except (ValueError , ZeroDivisionError):
    print("Can't div by zero or Enter numeric value!")'''

'''#Q9
try: #Semi colon was missing
 num = int(input("Enter a number: "))
 result = 100 / num
 print("Result:", result)
except ValueError: #Semi colon was missing
 print("Please enter a valid number")'''

'''#Q10
# ==================================
# SIMPLE CALCULATOR
# ==================================

while True:

    print("\n===== CALCULATOR MENU =====")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try:

        choice = int(input("Enter Choice: "))

        if choice == 5:

            print("Exiting Calculator...")

            break

        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        if choice == 1:

            print("Result =", num1 + num2)

        elif choice == 2:

            print("Result =", num1 - num2)

        elif choice == 3:

            print("Result =", num1 * num2)

        elif choice == 4:

            print("Result =", num1 / num2)

        else:

            print("Invalid Choice")

    except ValueError:

        print("Please enter valid numbers.")

    except ZeroDivisionError:

        print("Division by zero is not allowed.")

    finally:

        print("Operation attempted.")'''
