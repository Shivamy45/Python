# ques 1
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
print((a+b+c)/3)

# ques 2
d = complex(1,4)
e = complex(2,3)
print(d+e)

# ques 3
f = int(input("Enter f: "))
if f%2 == 0:
    print("Even")
else:
    print("Odd")

# ques 4
g = int(input("Enter g: "))
h = int(input("Enter h: "))
i = int(input("Enter i: "))
if g>h:
    if g>i:
        print(g)
    else:
        print(i)
elif h>i:
    print(h)
else:
    print(i)

# ques 5
for i in range(1,21):
    if i%2==0:
        print(i,end = " ")

# ques 6
for i in range (1,11):
    print(f"5 X {i} = {i*5}")

# ques 7
j = int(input("Enter j: "))
x = 0
y = 1
z = 1
for i in range(j):
    w = z + y
    y = z
    z = w
    print(w)

# ques 8
k = int(input("Enter k: "))
num1 = k-1
num2 = k+1
if k==2 or k==3 or num1%6== 0 or num2%6==0:
    print("This is prime.")
else:
    print("Not prime")

# ques 9
for i in range (1,6):
    for j in range(1,i):
        print("*",end = "")
    print()

# ques 10
for i in range(5,501,2):
    for j in range (2,i):
        if i%j==0:
            break
        else:
            if j==i-1:
                print(i)
    

# ques 11
l = input("Enter l: ")
print(l[::-1])

# ques 12
m = ['a','hello',45,20.5]
print(m)
m.append('new')
print(m)
m.remove('a')
print(m)
m.insert(2,'hi')
print(m)

# ques 13
for i in m:
    if i == 45:
        break
    print(i,end=" ")

# ques 14
for i in range(1,21):
    if i/3 == 0:
        continue
    print(i)

# ques 15
n = []
for i in range (1,11):
    n.append(i**2)
print(n)

# ques 16
o = [23,45,13,65,134,631,34,5,2,6]
print(sorted(o))







