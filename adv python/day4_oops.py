"""
Object Oriented Programming (OOPs)
1. Inheritance
2. Encapsulation
3. Abstraction
4. Polymorphism
"""

"""
--------------- Inheritance ---------------

------------ Single Inheritance ------------
Class A
   |
   |
Class B

------------ Multi-level Inheritance ------------
Class A
   |
   |
Class B
   |
   |
Class C

------------ Multiple Inheritance ------------
Class A         Class B
    \              /
     \            /
      \          /
       \        /
         ClassC

------------ Multipath Inheritance ------------
         Class A
        /   |   \
       /    |    \
    ClassB  |   Class C
       \    |    /
        \   |   /
         Class D

------------ Hierarchical Inheritance ------------
            Class A
            /      \
           /        \
          /          \
       ClassB       Class C
       / \            /  \
      /   \          /    \
     /     \        /      \
Class D  Class E Class F  Class G


------------ Hybrid Inheritance ------------
                Class A         Class B
                /    \           /
               /      \         /
              /        \       /
             /          \     /
         Class C        Class D
         /   \      
        /     \     
       /       \    
   Class D    Class E

"""
"""
class MathOperations():
    def add(a,b):
        return a+b
    def substract(a,b):
        return a-b
    def multiply(a,b):
        return a*b
    def divide(a,b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        else:
            return a/b
result_add = MathOperations.add(10,5)
result_sub = MathOperations.substract(10,5)
result_multiply = MathOperations.multiply(10,5)
result_div = MathOperations.divide(10,5)
print(f"Addition: 10 + 5 =",result_add)
print(f"Subtraction: 10 - 5 =",result_sub)
print(f"Multiplication: 10 * 5 =",result_multiply)
print(f"Division: 10 / 5 =",result_div)

class ComplexNumber():
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary
    def __str__(self):
        return f"{self.real} + {self.imaginary}j"
def add_complexNumber(x,y):
    real_sum = x.real + y.real
    imaginary_sum = x.imaginary + y.imaginary
    return ComplexNumber(real_sum,imaginary_sum)
a = ComplexNumber(2,3)
b = ComplexNumber(4,5)
print(a)
print(b)
print(add_complexNumber(a,b))
"""
class Distance():
    def __init__(self,km=0,m=0):
        self.km = km
        self.m = m
    def __str__(self):
        return f"{self.km}km and {self.m}m"
def add_distance(a,b):
    total_km = a.km + b.km
    total_m = a.m + b.m
    if total_m > 1000:
        total_km += total_m//1000
        total_m = total_m%1000
    return Distance(total_km,total_m)
x = Distance(3,200)
y = Distance(2,900)
print(add_distance(x,y))
