'''#Q1
print("Your name is: Rushabh")
print("Your age is: 20")
print("Your city is:jalgaon")'''

'''#Q2
name= input("Enter your name:")
print("Hello Mr.", name,"!!")'''

'''#Q3
a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
print("Sum",a+b)
print("Sub", a-b)
print("Modulus", a%b)
print("Div", a/b)
print("Floor div",a//b)
print("Multp",a*b)
print("Exponent",a**b)'''

'''#Q4
print("Voting eligibility...")
age =  int(input("Enter your age:"))
if age>=18:
    print("Eligible to vote!!")
else:
    print("Not eligible to vote!!")
print("Eligibility check successful...")'''

'''#Q5
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")'''

'''#Q6
marks = int(input("Enter marks: "))

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")'''

'''#Q7
for i in range(1,21):
    print(i)'''

'''#Q8
for i in range (1,51):
    if i % 2 ==0:
        print(i)'''
'''#Q9
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)'''

'''#Q10
i = 10
while i>=1:
    print(i)
    i -=1'''
'''#Q11
total=0
for i in range(1,101):
    total+=i
print("Sum is:",total)'''
#Q12
'''str = "Artificial Intelligence"

count = 0

for ch in str.lower():
    if ch in "aeiou":
        count += 1

print("Vowels =", count)'''
#Q13
'''text = input("Enter a string: ")

print("Length =", len(text))
print("First Character =", text[0])
print("Last Character =", text[len(text)-1])'''
#Q14
'''str= input("Enter a string:")
print("Reversed string is:",str[::-1])'''
#Q15
'''text = input("Enter a string: ")

count = 0

for ch in text.lower():
    if ch == 'a':
        count += 1

print("Count =", count)'''
#Q16
'''str_1= input("Enter a string 1:" )
if str_1==str_1[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
'''

#Q17
'''text = "Machine learning"
print(text[0:7])
print(text[8:18])
print(text[4:12])
print(text[0:18])'''

#Q18
'''fruits=["Mango","Apple","Orange","Banana","Grapes"]
print(fruits[0])
print(fruits[-1])
print(len(fruits))'''
#Q19

'''numbers=[]

for i in range(5):
    num=int(input("Enter number:"))
    numbers.append(num)
print("Largest num:",max(numbers))'''
#Q20
'''numbers=[]

for i in range(5):
    num=int(input("Enter number:"))
    numbers.append(num)
print("Smallest num:",min(numbers))'''
#Q21
#Q22
#Q23
#Q24
#Q25
#Q26
'''tuple_1=(12,5,45,65,18)
print(tuple_1[0])
print(len(tuple_1))'''
'''#Q27
numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))'''

#Q28
'''set={10,20,30,40}
set.add(50)
print(set)'''
#Q29
'''set={10,20,30,40,50}
set.remove(20)
print(set)'''
#Q30
'''numbers = [1, 2, 2, 3, 3, 4, 4, 5]

result = set(numbers)

print(result)'''
#Q31
'''student = {
    "name": "Rushabh",
    "age": 20,
    "city": "Nashik"
}

print(student.values())'''
#Q32
'''student = {
    "name": "Rushabh",
    "age": 20,
    "city": "Nashik"
}

print(student["name"])'''
#Q33
'''student = {
    "name": "Rushabh",
    "age": 20,
    "city": "Nashik"
}
student["course"]="AI/ML"
print(student)'''
#Q34
'''student = {
    "name": "Rushabh",
    "age": 20,
    "city": "Nashik"
}
student["age"]="21"
print(student)'''
#Q35

#Q36
'''num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")'''
#Q37

#Q38
'''a=int(input("Enter a num:"))
b=int(input("Enter a num:"))
c=int(input("Enter a num:"))

if a>b and a>c:
   print("A is greater")
elif b>c :
   print("B is greater")
else:
   
   print("c is greater")'''

#Q39
'''num = input("Enter a number: ")

print("Digits =", len(num))'''
#Q40
'''name=input("enter name:")
age=int(input("enter age:"))
print(f"Hello,{name}. welcome to python!. Your age is:{age}")'''
tup= 1,4,7,"Hello"
print(type(tup)) 