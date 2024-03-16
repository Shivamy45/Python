"""
Types of parameter:
    1. Default parameter
    2. Required parameter
    3. Keyword parameter
    4. Variable parameter
"""

"""
Default values are set to indicate that the function argument will take that value if no argument value is passed during function call.
The default value is assigned by using assignment (=) operator

def multi(x,y=10):
    print("inside function")
    print("first number is",x,"and second number is",y)
multi(3)
multi(4,6)
a = int(input("a: "))
b = int(input("b: "))
multi(a,b)
"""

"""
Required parameters

def info(name, age ,branch):
    print(f"My name is {name}. My age is {age}. I study in {branch} branch.")
info("shivam", 16, "CSE")
name = input("Name: ")
age = int(input("Age: "))
branch = input("Branch: ")
info(name,age,branch)

def jeeForm(name, address):
    print(f"My name is {name}. I live in {address}.")
jeeForm("Sudhanshu", "Afganistan")
"""

"""
Keyword function

# create a function name as a fullName first name surname
def fullName(firstname, middlename, surname):
    print(firstname,middlename,surname)

fullName(firstname="Shivam", middlename="Harishchandra", surname="yadav")
fullName(firstname="Sudhanshu", surname="Niraj", middlename="Kumar")
"""

"""
Variable parameter

def variarg(*num):
    for i in num:
        print(i,end=" ")

variarg('1','2','3','4','5')

def factOf(num):
    if num == 0:
        return 1
    else:
        return num * factOf(num-1)
print(factOf(5))

# To increase the limit of recursion
import sys
sys.setrecursionlimit(5000)

def factOf(num):
    if num == 0:
        return 1
    else:
        return num * factOf(num-1)
print(factOf(2000))
"""

"""
Lambda function

Sum = lambda a,b:a+b
print(Sum(10,20))
"""

"""
Global & Local variable
Local variable can be accessed only inside the functio  in which they are declared
Global variables can be accessed throughout the program body by all functions
name = "Python"
def f():
    name = "Django"
    print("Within function:", name)
print("Outside function:", name)
f()
"""

"""
A module is a file containing Python definitions and statements.
A module can define functions, classes, and variables.
A module can also include runnable code.
Grouping related code into a module makes the code easier to understand.
It also makes the code logically organized.

We can use any python source file as a module by executing an import statement in some other Python source file.
When the interpreter encounters an import statement, it imports the module if the module is present in the search path
def Sum():
    a,b = 10,20
    print(a+b)
def Sub():
    a,b = 50,40
    print(a-b)

import calendar
print(calendar.calendar(2024))
print(calendar.month(2024,8))

import math
print(math.pow(2,3))
print(math.sin(0))
from math import pow,sqrt,pi
print(pow(2,6))
print(sqrt(5))
print(pi)
import math as m
print(m.pow(2.5))
"""
