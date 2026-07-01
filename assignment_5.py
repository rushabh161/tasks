'''#Q1
#Taking str input from user
Name = input("Enter your name:")

#Printing the first character
print("The first char is:",Name[0])

#Printing the last character
print("The last char is:",Name[-1])

#Printing the 3rd char from the start
print("The 3rd char from the start is:",Name[2])

#Printing the 2nd char from the end
print("The 2nd char from the end is:",Name[-2])'''

#Q2
'''#Taking str input from user
Country = input("Enter your county:")

#Printing the first 5 characters
print("First 5 char are:",Country[0:5])

#Printing the last 4 characters
print("Last 4 char are:",Country[-4:])

#Printing the str country name in reverse order
print("The country name in reverse order is:",Country[::-1])

#Every second char of the country name
print("Every second char of the country name is:",Country[::2])'''

#Q3
'''#Taking main & sub str input from user
main_str = input("Enter the main string:")
sub_str = input("Enter the sub string:")

#Checks whether the substring is present in the main string using in and not in
if sub_str in main_str:
    print("Substring found!!")
else:
    print("Substring not found!!")

if sub_str not in main_str:
    print("Substring not found!!")
else:
    print("Substring found!!")'''

'''#Q4
# len() returns total number of characters

text = input("Enter a string: ")

length = len(text)

print("Length =", length)

# Last character using len() without negative index
print("Last Character =", text[len(text) - 1])

# Print middle character if length is odd
if len(text) % 2 != 0:

    middle = len(text) // 2

    print("Middle Character =", text[middle])

else:
    print("String length is even. No single middle character.")

# Common Mistake:
# text[len(text)] is invalid because indexing starts from 0.
# Correct last index is len(text)-1.'''

#Q5
'''#a) print num from 0 to 10
print("The num from 1-10 are:")
for i in range(11):
    print(i)

#b) print num from 5 to 15
print("The num from 5-15 are:")
for i in range(5,16):
    print(i)

#c) print odd num from 1 to 21
print("The odd num from 1-21 are:")
for i in range(1,22,2):
    print(i)'''

'''#Q6
print("The num from 20-10 are:")
# range(start, stop, step) with step as -1 to print in reverse order
for i in range(20,9,-1):
    print(i)

print("The num from 15-1 are:")
# range(start, stop, step) with step as -2 to print in reverse order with a step of 2
for i in range(15,0,-2):
    print(i)'''

#Q7
'''#Taking a str from user
text = input("Enter a string: ")
print("Characters with there respective index are:")
#Using for loop and range() to print index and character at that index
for i in range(len(text)):
    print(i,"=",text[i])

print("\nReverse String:")
#Using for loop and range() to print characters in reverse order
for i in range(len(text) - 1, -1, -1):
    print(text[i], end="")'''

#Q8
'''#Taking a num from user
num = int(input("Enter a number to check:"))

#Check whether the num is present in range(1,51)
if num in range(1,51):
    print("The number is present in the range 1-50!!")

else:
    print("The number is not present in the range 1-50!!")

if num not in range(10,100,5):
    print("The number is present in the range 10,100,5")
else:
    print("The number is not present in the range 10,100,5")'''

'''#Q9
# First 10 even numbers

print("First 10 Even Numbers")

for i in range(2, 21, 2):
    print(i)

# Numbers from 1 to 30 in steps of 3

print("\nNumbers from 1 to 30 in Steps of 3")

for i in range(1, 31, 3):
    print(i)

# String Slicing

text = "PythonProgramming"

print("\nPython =", text[:6])

print("Programming =", text[6:])

print("Reverse =", text[::-1])'''

'''#Q!0
# String Analyzer Program

text = input("Enter a string: ")

# Length
print("Length =", len(text))

# First half and second half

mid = len(text) // 2

print("First Half =", text[:mid])

print("Second Half =", text[mid:])

# Case-insensitive search

if "python" in text.lower():
    print("'python' is present")

else:
    print("'python' is not present")

# Positive and negative indices

print("\nCharacters with Positive and Negative Indices")

for i in range(len(text)):

    print("Positive Index =",i)
    print("| Character =", text[i])
    print("| Negative Index =", i - len(text))

# Reverse string

print("\nReverse String =", text[::-1])'''