"""
import keyword
print(keyword.kwlist)
a = "RAM"
A = 123
print(type(a))
print(id(a)
x = complex(2,3)
print(x)
print(type(x))
a = 5
b = 3

print(a+b)
print(a-b)
print("Shivam")
x = 18
y = "shivam"

print("%s is %d years old."%(y,x))
print("{} is {} years old".format(y,x))
print(f"{y} is {x} years old")

a = list(map(int, input("Enter the numbers : ").split(",")))
sum = 0
for i in a:
    sum += i
print(sum)

for i in range (1,5):
    a = int(input(f"Enter integer {i}: "))
    sum += a
print("The sum is "+ str(sum))
"""
def xyz(a):
    """
    This is a program of doc string
    This will print multi line comments
    """
    print(xyz.__doc__)
# xyz(9)
"""
print("hello",end= " ")
print("world")
print("Namaste","India",sep=" ")

a = "Anuj"
b = "OP"
print(a+b)
print(a+b*2)
str1 = "Ayodhya"
print(str1[1:6:2])
print(str1[-5:-2])
print(str1[-2:-5:-1])

a1 = int(input("value1: "))
b = int(input("value2: "))
c = int(input("value3: "))
s = (a1+b+c)/2
area = (s*(s-a1)*(s-b)*(s-c))**(1/2)
print(area)
vowel = ['a','e','i','o','u']
print('a' in vowel)

a = list(map(int,input("value: ").split(',')))
print(a)
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
if n1 > n2:
    if n1> n3:
        print(f"{n} is greatest")
    else:
        print(f"{n3} is greatest")
elif n2>n3:
    print(f"{n2} is greatest")
else:
    print(f"{n3} is greatest")
length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))
if length == breadth:
    print("It is a square")
    print("Its area is {}".format(length**2))
else:
    print("It is a rectangle")
yos = int(input("How many years you served?\n"))
if yos > 5:
    salary = int(input("Enter your salary: "))
    print("Your salary with bonus is {}".format(salary+salary*0.05))
    
a = input("Enter a number: ")
try:
    if int(a) > 0:
        print("Positive")
    elif int(a)<0:
        print("Negative")
    elif int(a) == 0:
        print("Zero")
except ValueError as e:
    print("You did not enter a number")
i=10
while(i>0):
    print(i,end= " ")
    i-=1
n = int(input("Enter a number: "))
i=1
sum = 0
while (i<=n):
    sum += i**2
    i+=1
print(sum)

for i in range(10,0,-1):
    print(i,end=" ")

for i in range (0,10):
    for j in range (0,5):
        print(i,end=" ")
    print(f"\n{j}")
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print("")

num = [1,2,3,4,5,6,7,8,9]
num_sum = 0
count = 0
for x in num:
    num_sum += x
    count += 1
    if count == 5:
        break
print("Sum of first", count, "integers is:",num_sum)
"""
for i in range(7):
    if i == 3 or i ==6:
        continue
    print(i)


num = int(input("Enter a number: "))
if num is 2:
    pass
else:
    print("Number is :",num)
