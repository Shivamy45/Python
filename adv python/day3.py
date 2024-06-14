"""
import functools import reduce
number = [2,5,8,32,64,7,47,38,74,97,53]
def even(n):
    if n % 2 == 0:
        return True
a = list(filter(even,number))
print(a)

def sqr(n):
    return n**2
b = list(map(sqr,a))
print(b)

sum = functools.reduce(lambda x, y: x+y, b)
print(sum)

import math
print(math.factorial(5))

import math as m
print(m.sqrt(25))

from math import sqrt
print(sqrt(36))

from math import sqrt as rt
print(sqrt(2,5))
print(rt(2,5))

from math import *
# this imports all names except funciton with '__'

import day3_func
day3_func.add(3,4)
day3_func.sub(9,4)
day3_func.mul(7,4)
day3_func.div(12,4)
print(dir(day3_func))

class class1():
    a = 4
    print(a)
print(class1)
p1 = class1()
print(p1.a)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

s1 = Person("Shivam",18)
print(s1.name)
print(s1.age)



class student ():
    def __init__(self):
        self.name = input("Enter the name student's name: ")
        self.age = int(input("Enter the student's age: "))
    def display ():
        print("student's name: ",self.name)
        print("Student's age: ",self.age)
s1=student()
s1=display()

class book():
    def __init__(self):
        self.title = input("Enter title: ")
        self.author  = input("Enter author: ")
        self.nop = int(input("Enter number of pages: "))
    def display(self):
        print(f"Author {self.author} wrote {self.title} of {self.nop} pages.")
    
b1 = book()
b1.display()

class circle():
    def __init__(self):
        self.radius = float(input("Enter radius: "))
    def area(self):
        return 3.14*(self.radius**2)
    def p(self):
        return 2*3.14*self.radius

c = circle()
print("Area of circle",c.area())
print("Circumference of circle",c.p())

class Rectangle():
    def __init__(xyz,l,b):
        xyz.length = l
        xyz.breadth = b
    def area(xyz):
        return xyz.length*xyz.breadth
    def perimeter(xyz):
        return 2*(xyz.length+xyz.breadth)
r = Rectangle(3,5)
print("Area of rectangle is",r.area())
print("Perimeter of rectangle is",r.perimeter())
"""
class student():
    college = "NIET"
    city = "Noida"
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
    @classmethod
    def college_info(cls):
        print("College name:",cls.college)
        print("City:",cls.city)
    @staticmethod
    def avg(x,y):
        av = (x+y)/2
        print(av)
s1 = student("shivam",39)
s1.college_info()
s1.avg(2,4)

