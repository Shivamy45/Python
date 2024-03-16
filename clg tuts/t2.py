"'Operators'"
"""
Addition(+)
Substraction(-)
Multiplication(*)
Division(/)
Floor division(//)
Modulus(%)
Exponential(**)
"""

"""
a = 10
b = 20
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("The sum is:",a+b)
print("The difference is:",a-b)
print("The product is:",a*b)
print("The quotient is:",a/b)
print("The integer quotient is:",a//b)
print("The remeinder is:",a%b)
print("The a**b is:",a**b)

a = 10 
b = 20
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

a = 15
b = 10

a += b
print(a)
a -= b
print(a)
a *= b
print(a)
a /= b
print(a)
a %= b
print(a)
a //=b
print(a)
a **= b
print(a)
"""

"'Bitwise Operator'"
"""
AND(&)
OR(|)
XOR(^)
Binary One's Complement(~) --> a = -(a+1)
Binary left shift (<<)
Binary right shift (>>)
"""

"""
a = 4
b = 6
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a>>b)
print(a<<b)
"""

# a,b = map(int, input().split(','))
a, b= 10, 20
# print (a,b)

"'Logical Operator'"
"""
and
or
not
"""
"""
print(a and b)
print(a or b)
print(not a)
"""
"'Membership operator'"
"""
in
not in
"""
"""
print("n" in "String")
print("N" not in "String")
"""
"'Identity operator'"
"""
is
is not
"""
"""
print(3 is 4)
print(3 is not 3)
"""

"'Conditional Statements'"
a = 13

"""
if
If the given conditions true, then the statements inside if clause will be executed.
"""
"""
if(a < 14):
    print("inside if")
    print(f"{a} is less than 14")
print("outside if")

# if no condition is given it is True.
# If we do the below code only statement before colon will be executed.
if print("abc"):
    print('hello')
"""

"""
else
If no condition returns true then else clause will be executed
"""
"""
if(a < 14):
    print("inside if")
    print(f"{a} is less than 14")
else:
    print("inside if")
    print("No case matched")
print("outside if")
"""
"""
{Voting list}
age = int(input("Enter your age: "))
if age>= 18:
    print("You are eliglible")
else:
    print("You are not eligible")

{Condition check}
if 3 and 0 or 4:
    print("True")
else:
    print("False")
"""

"""
elif
If the "if" statement returns 'false' and any elif condition returns 'true' then that elif clause will be executed
"""
"""
if(a < 14):
    print("inside if")
    print(f"{a} is less than 14")
elif(a > 20):
    print("inside if")
    print(f"{a} is greater than 20")
else:
    print("inside if")
    print("No case matched")
print("outside if")
"""
"""
num = int(input("Enter a number: "))
if num<0:
    print(f"{num} is a negative number")
elif num>0:
    print(f"{num} is a positive number")
else:
    print(f"{num} is zero")
"""

"""
Nested if statements
If we insert a conditional statement inside another conditional statement then it is nested if statements
"""
"""
if a<20:
    print("inside if")
    print(f"{a} is less than 20")
    if a<10:
        print("inside nested if")
        print(f"{a} is less than 10")
    else:
        print("inside nested else")
        print(f"{a} is less than 20 but greater than 10")
    print("outside nested if/else")
else:
    print("inside else")
    print(f"{a} is greater than 20")

print("outside if/else")

# print("jai shree ram__"*1008)

num = int(input("Enter a number: "))
if num>0:
    if num%2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
else:
    print("Enter a +ve number")
"""
if 11>15 or 12<15:
    if True and False:
        if not False:
            print(1)
    elif 121 and 543:
        print(2)
    else:
        print(3)
else:
    print(4)