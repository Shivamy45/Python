"""
A function is a set of statements that take inputs, do some specific computation and produces output
These set of statements can be used anywhere just by calling it name and we call this as resuability
1. Python buit-in functions:
    abs()
    all()
    any()
    ascii()
    bin()
    bool()
    bytearray()
    byte()
2. Python user-defined functions
3. Python recursion functinos
4. Python Lambda functions

function syntax
def functionNameHere (parameters):
    #your code here

with parameter with return type
with parameter without return type
without parameter with return type
without parameter without return type
def Sum():
    a = 5
    b =6
    print("Addition fo a and b is:",a+b)
print("function call")
Sum()

All parameters in python lang are passed by refrence. It means you can change whar a parameter refers to within a function, the  change also reflects in the calling

# write a program to check whether the given no. is even or odd with argument without return type
def evenodd(num):
    if num%2==0:
       return "even"
    else:
        return "odd"
print(evenodd(9))
num = 4
print(evenodd(num))
"""
