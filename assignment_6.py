'''#Q1
# a) Create a list directly

numbers = [10, 20, 30, 40, 50]

print("Numbers List =", numbers)

# b) Create an empty list

empty_list = []

print("Empty List =", empty_list)

# c) List with mixed data types

mixed_list = [10, "Rushabh", 5.5, True]

print("Mixed List =", mixed_list)

# d) List containing 7 zeros

zeros = [0] * 7

print("Seven Zeros =", zeros)'''

'''#Q2
# List of fruits

fruits = ["apple", "banana", "mango", "orange", "grape"]

print("First Item =", fruits[0])

print("Third Item =", fruits[2])

print("Last Item =", fruits[-1])

print("Second Last Item =", fruits[-2])

# User input

index = int(input("Enter an index: "))

print("Element at Index", index, "=", fruits[index])'''

'''#Q3
# List of numbers

numbers = [10,20,30,40,50,60,70,80,90,100]

print("First 4 Elements =", numbers[:4])

print("Last 3 Elements =", numbers[-3:])

print("Elements from Index 2 to 7 =", numbers[2:8])

print("Every Second Element =", numbers[::2])

print("Reversed List =", numbers[::-1])'''

'''#Q4
# Original List

colors = ["red", "blue", "green", "yellow"]

print("Original List =", colors)

# Replace blue with purple

colors[1] = "purple"

# Replace last item with black

colors[-1] = "black"

print("Modified List =", colors)'''

'''#Q5
# Empty list

cities = []

# Add cities using append()

cities.append("Mumbai")
cities.append("Nashik")
cities.append("Nagpur")

print("After Append =", cities)

# Insert Pune at index 2

cities.insert(2, "Pune")

print("After Insert =", cities)'''

'''#Q6
items = [10, 20, 30, 20, 40, 50]

print("Original List =", items)

# remove() removes first occurrence of value

items.remove(20)

print("After remove(20) =", items)

# pop() removes element by index

removed_item = items.pop(3)

print("Removed Item =", removed_item)

print("After pop(3) =", items)

# clear() removes all elements

items.clear()

print("After clear() =", items)'''

'''#Q7
scores = [85, 92, 78, 92, 65, 92, 88]

print("First Occurrence of 92 =", scores.index(92))

print("Count of 92 =", scores.count(92))

num = int(input("Enter a number to search: "))

if num in scores:

    print("Found!")

    print("First Index =", scores.index(num))

    print("Count =", scores.count(num))

else:

    print("Number not found")'''

'''#Q8
marks = [45, 78, 65, 90, 34, 82, 71]

print("Original List =", marks)

# Ascending order

marks.sort()

print("Ascending Order =", marks)

# Descending order

marks.sort(reverse=True)

print("Descending Order =", marks)

# Reverse current order

marks.reverse()

print("Reversed List =", marks)'''

'''#Q9
list1 = [1, 2, 3]

list2 = [4, 5, 6]

# Using extend()

temp1 = list1.copy()

temp1.extend(list2)

print("Using extend() =", temp1)

# Using append()

temp2 = list1.copy()

temp2.append(list2)

print("Using append() =", temp2)'''

#Q10
# Student Marks Manager

marks = []

# Input 5 marks

for i in range(5):

    mark = int(input("Enter Mark " + str(i + 1) + ": "))

    marks.append(mark)

# Add one more mark

new_mark = int(input("Enter One More Mark: "))

marks.append(new_mark)

print("Marks List =", marks)

# Highest mark

print("Highest Mark =", max(marks))

# Lowest mark

print("Lowest Mark =", min(marks))

# Sort in descending order

marks.sort(reverse=True)

print("Marks in Descending Order =", marks)

# Average

average = sum(marks) / len(marks)

print("Average Marks =", average)

# Total subjects

print("Total Subjects =", len(marks))