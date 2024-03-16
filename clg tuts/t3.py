"""
i = 1
while i <= 10:
    print (f"2 x {i} =",i*2)
    i += 1
print("end loop")

x = "abcdef"
i = "i"
while i in x:
    print(i, end=" ")

for i in range (3):
    print(i, end =" ")
print("for loop ended")
for i in range (2,5):
    print(i,end="_")
print("for loop ended")
# syntax: for var in range (start,end,step)
for i in range (3,6,1):
    print(i, end="-")
print("for loop ended")

# Write a program to print prime number 
factorial = 1
num = int(input("Enter a num: "))
if num<0:
    print("Enter a +ve number")
else:
    for i in range (1,num+1):
        factorial *= i
print(factorial)
a = 0
for i in range (2):
    for j in range (1,4):
        print(a, end=" ")
    print()
    a += 1
for i in range (3):
    for j in range (1,6):
        print("*", end="")
    print()

for i in range (5):
    if i == 3:
        break
    print(i)
print("break loop ended")

for i in range(20):
    if(i==10):
        print("break")
        break
    else:
        print(i,end=" ")
print("program is ended")
for i in range (5):
    if i == 3:
        print("continue")
        continue
        print("Will not be printed")
    elif i == 4:
        pass
    else:
        print(i)
"""

# The statement does nothing 
"""
We use pass statement when you create a method that you don't wnat to implement yet
"""
"""
i = 0
while i<=3:
    print("Python")
    i+=1
    break
else:
    print("end loop")

i = 0
while i <=3:
    print("Python")
    i+=1
else:
    print("end loop")
"""

