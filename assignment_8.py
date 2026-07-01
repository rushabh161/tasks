'''# Q1. Creating Sets

# a) A set with 5 integers
int_set = {1, 2, 3, 4, 5}
print("a) Integer set:", int_set, "| Type:", type(int_set))

# b) A set with mixed data types (integer, string, float)
mixed_set = {10, "hello", 3.14}
print("b) Mixed set:", mixed_set, "| Type:", type(mixed_set))

# c) An empty set using the correct method
# empty_set = {} would actually create a DICTIONARY, not a set.
# The only correct way to create an empty set is set().
empty_set = set()
print("c) Empty set:", empty_set, "| Type:", type(empty_set))

# d) A set from the string "hello" using the set() constructor
# sets cannot hold duplicates, the repeated 'l' is automatically removed.
string_set = set("hello")
print("d) Set from 'hello':", string_set, "| Type:", type(string_set))
'''

# Q2. Characteristics of Sets

''''numbers = {10, 20, 30, 20, 40, 10, 50}
# The set has duplicates value,printing the set will discard the duplicate values.
print("Set (1st print):", numbers)

# Demonstrating that sets are UNORDERED by printing multiple times.
# order is NOT preserved/guaranteed the way it is for lists.
print("Set (2nd print):", numbers)
print("Set (3rd print):", numbers)
print("Set (4th print):", numbers)

#Can't access elemnts through indexing cause set doesn't allow indexing n slicing due to which it will cause an error
try:
    first_element = numbers[0]
except TypeError as e:
    print("Error when trying numbers[0]:", e)'''

# Q3. Membership Testing

'''colors = set()
print("Enter 5 colors:")
for i in range(5):
    color = input(f"Color {i + 1}: ").strip().lower()
    colors.add(color)

print("Your color set:", colors)

search_color = input("Enter a color name to check: ").strip().lower()

# Checking membership using 'in'
if search_color in colors:
    print(f"'{search_color}' IS present in the set.")
else:
    print(f"'{search_color}' is NOT present in the set.")

# Checking membership using 'not in'
if search_color not in colors:
    print(f"(using 'not in') -> '{search_color}' is missing from the set.")
else:
    print(f"(using 'not in') -> '{search_color}' was found in the set.")'''

# Session 08 (AIML) - Assignment
# Q4. add(), remove(), discard()

'''fruits = {'apple', 'banana', 'mango'}
print("Original set:", fruits)

# a) Add 'orange' using add()
fruits.add('orange')
print("a) After add('orange'):", fruits)

# b) Add 'banana' again -> since 'banana' already exists, the set
# remains unchanged (no duplicate is added, and no error occurs).
fruits.add('banana')
print("b) After add('banana') again (no change expected):", fruits)

# c) Remove 'mango' using remove()
# remove() deletes the element; if the element does NOT exist,
# it raises a KeyError.
fruits.remove('mango')
print("c) After remove('mango'):", fruits)

# d) Try to remove 'grape' using discard()
# discard() also deletes the element, but if the element does NOT
# exist, it does nothing and does NOT raise an error.
fruits.discard('grape')
print("d) After discard('grape') [no error, 'grape' wasn't present]:", fruits)'''

# Session 08 (AIML) - Assignment
# Q5. pop() and clear()

'''s = {100, 200, 300, 400, 500}
print("Original set:", s)

# pop() removes and returns an ARBITRARY element from the set
# (since sets are unordered, you cannot control/predict which
# element gets removed).
popped_element = s.pop()
print("Popped element:", popped_element)
print("Set after pop():", s)

# clear() empties the set completely, leaving an empty set object.
s.clear()
print("Set after clear():", s)

# DIFFERENCE BETWEEN remove(), discard(), and pop():
# - remove(x): deletes element x. Raises KeyError if x is not found.
# - discard(x): deletes element x. Does NOT raise an error if x is
#               not found (silently does nothing).
# - pop(): removes and returns a random/arbitrary element from the
#          set. Raises KeyError if the set is already empty.
#          You don't get to choose which element is removed.'''
# Session 08 (AIML) - Assignment
# Q6. update() and copy()

'''set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}

# Make a copy of set1 BEFORE modifying it, so we still have the
# original elements preserved separately.
set1_copy = set1.copy()

# update() adds all elements of set2 into set1 (in place),
# automatically skipping any duplicates (like 3, which is in both).
set1.update(set2)

print("Original copy of set1:", set1_copy)
print("set1 after update() with set2:", set1)'''
# Session 08 (AIML) - Assignment
# Q7. Union and Intersection

'''A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# UNION: combines all unique elements from both sets.
union_method = A.union(B)
union_operator = A | B
print("Union using .union():", union_method)
print("Union using | operator:", union_operator)

# INTERSECTION: keeps only the elements common to BOTH sets.
intersection_method = A.intersection(B)
intersection_operator = A & B
print("Intersection using .intersection():", intersection_method)
print("Intersection using & operator:", intersection_operator)'''

# Session 08 (AIML) - Assignment
# Q8. Combined Methods

'''number_set = set()
print("Enter 6 numbers (duplicates will be removed automatically):")
for i in range(6):
    num = float(input(f"Number {i + 1}: "))
    number_set.add(num)

print("Set after input:", number_set)

# Add two more numbers using add()
extra1 = float(input("Enter an extra number to add: "))
extra2 = float(input("Enter another extra number to add: "))
number_set.add(extra1)
number_set.add(extra2)
print("Set after adding 2 more numbers:", number_set)

# Remove one number safely using discard() (no error even if missing)
remove_num = float(input("Enter a number to remove safely: "))
number_set.discard(remove_num)
print("Set after discard():", number_set)

print("Final set:", number_set)
print("Length of final set:", len(number_set))'''

# Session 08 (AIML) - Assignment
# Q9. Practical Application

'''scores = [85, 92, 78, 92, 85, 88, 95, 78]
print("Original scores list:", scores)

# Convert the list to a set -> automatically removes duplicate marks
unique_scores_set = set(scores)
print("Unique scores (as a set):", unique_scores_set)

# Convert the set back to a SORTED list
sorted_unique_scores = sorted(unique_scores_set)
print("Unique scores (sorted list):", sorted_unique_scores)

# Total number of unique scores
print("Total number of unique scores:", len(sorted_unique_scores))'''

# Session 08 (AIML) - Assignment
# Q10. Mini Project - Unique Item Collector

items = set()  # stores all the unique items entered by the user

menu = """
========== UNIQUE ITEM COLLECTOR ==========
1. Add item
2. Remove item (discard)
3. Show all unique items
4. Check if an item exists
5. Clear all items
6. Exit
============================================
"""

while True:
    print(menu)
    choice = input("Enter your choice (1-6): ").strip()

    if choice == '1':
        # Add a new item; duplicates are automatically ignored by the set
        new_item = input("Enter item to add: ").strip()
        items.add(new_item)
        print(f"'{new_item}' added (or already existed).")

    elif choice == '2':
        # discard() is used so the program never crashes even if the
        # item the user wants to remove doesn't exist.
        remove_item = input("Enter item to remove: ").strip()
        items.discard(remove_item)
        print(f"'{remove_item}' removed (if it was present).")

    elif choice == '3':
        if items:
            print("Current unique items:", items)
        else:
            print("No items have been added yet.")

    elif choice == '4':
        check_item = input("Enter item to check: ").strip()
        if check_item in items:
            print(f"'{check_item}' EXISTS in the collection.")
        else:
            print(f"'{check_item}' does NOT exist in the collection.")

    elif choice == '5':
        items.clear()
        print("All items cleared.")

    elif choice == '6':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")