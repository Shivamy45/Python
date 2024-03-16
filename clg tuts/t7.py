"""
l = [[1,2,3],[4,5,6],[7,8,9]]
for row in l:
    for col in row:
        print(col, end=" ")
    print()

for i in range (5):
    print("*"*i)
for i in range (5,0,-1):
    print("*"*i)
for i in range (1,5):
    for j in range (1,5):
        if j >= 5-i:
            print("*",end="")
        else:
            print(end=" ")
    print()
"""
"""
t = ()
print(t)
t = (1,2,'shivam',4)
print(t)
t1 = tuple(input("enter the elements: ").split(","))
print(t1)
t2 = tuple(map(int,input("enter the elements; ").split(",")))
print(t2)
print(t[3])
for i in t:
    print(i)
del(t)

t = (1,2,3,'python',3,3)
print(t.count(3))
print(t.index(2))
print(t.index(3))
t1 = (1,2,3,4,5)
print(sum(t1))
print(max(t1))
print(min(t1))
print(any(t1))
print(all(t1))
print(len(t1))
t = (1,3,5,3,5,6,7)
print(t[:])
print(t[3:])
print(t[:4])
print(t[2:4])
print(t[::2])
print(t[::-1])
print(t[3:7:3])
print(t[-5:-3])

t = (i*2 for i in range(1,20) if i%4==0)
print(tuple(t))

t = tuple(map(int,input("e: ").split(",")))
t2 = tuple(i for i in t)
print(t2)

t = (2,3,4,3,2,2)
t1 = t[::2]
print(t1.count(2))
"""

