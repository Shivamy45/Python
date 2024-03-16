"""
from packages import file1

print(file1.Sum(4,5))
print(file1.Sub(4,5))
from packages.file1 import Sum
print(Sum(3,4))

from packages.file2 import *
print(mul(3,4))
print(exp(2,5))
"""
"""
LIST and TUPLES

L = []
print(L)
L = list(map(int,input("Enter list: ").split(",")))
print(L)
L2 = input("Enter list: ").split()
print(L2)
for i in L2:
    print(i)
l = [1,2,3,6,7,8,[1,2,3,4,5]]

print(l[-2])
print(l[-1][2])

del(l)
print(l)

l = [1,2,3,4,5]
for i in range (1,4):
    l[i-2]=l[i]
for i in range (0,4):
    print(l[i], end=" ")
"""
"""
l = [1,2,4,3,6]
l.append(["append1", "append2"])
print(l)
l.insert(4,'added')
print(l)
l.remove('added')
print(l)
l.extend(["extended1", "extended2"])
print(l)
l.pop()
print(l)
print(l.index(3))
l.sort
print(l.sort)
print(l.count)
l2 = l.copy
print(l2)
print(l.reverse)
l.clear()
print(l)

l = [1,2,4,0,5,8]
print(sum(l))
print(max(l))
print(min(l))
print(all(l))
print(any(l))
print(len(l))
l = [i**2 for i in range(1,20) if i%2 == 0]
print(l)
"""