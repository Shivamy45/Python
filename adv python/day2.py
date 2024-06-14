"""
list = ['abcd',786,2.23,'john',70.2]
tinylist = [123,'john']
print(list)
print(list[0])
print(list[1:4])
print(list[2:])
print(list*2)
print(list+tinylist)
list[1:3]= ['new','hitman']
print(list)

tuple = ('hello','this','is','a','tuple',39)
tinytuple = ('tiny','tuple')
print(tuple)
a = list(tuple)
print(a)
a[1],a[4] = 'he','RAM'
print(a)

x = ['RAM',25,'SITA',46]
print(x[2][2])

a = {1,2,3,3,1,3,5,6}
print(a)

x = {"Brand":"Maruti","Model":"800","Year":"2024"}
print(x["Brand"])

a = [1,5,2,6,3]
sum = 0
for i in a:
    sum += i
print(sum)

n=[]
for i in a:
    n.append(i**3)
    print(i**3,end=" ")
print()
print(n)

mul = 1
for i in a:
    mul *= i
print(mul)

def disp():
    def show():
        print("this is show")
    show()
    print("This is disp")
disp()
def add(x,y):
    c = x+y
    return c
print(add(10,2))
def show(name,age,add="noida"):
    print(name,age,add)

show(name="Shivam",add="Delhi",age=14)
def factorial(n):
    mul = 1
    for i in range(1,n+1):
        mul *= i
    return mul

def recFact(n):
    if n ==1 or n ==0:
        return 1
    else:
        return n * recFact(n-1)

n = int(input("Enter a number: "))
print(factorial(n))
print(recFact(n))

def fib(n):
    x = 0
    y = 1
    c = 1
    print(x,y,c)
    for i in range(n-3):
        d = c + y
        y = c
        c = d
        print(d,end=" ")
print(fib(7))
a=50
def add(y):
    x = 10
    print(x)
    print(a)
    print(x+y)
add(20)
print(a)
print(x)
a = 'global a'
b = 'global b'
def test_namespace():
    a = 'enclosed a'
    def inner_namespace():
        a = 'local a'
        print(a)
        print(b)
    inner_namespace()
    print(a)
    print(b)
test_namespace()
print(a)
print(b)

def factorial(n):
    mul = 1
    for i in range(1,n+1):
        mul *= i
    return mul
n = int(input("Enter n:"))
r = int(input("Enter r:"))
print(factorial(n)/(factorial(r)*factorial(n-r)))

a = lambda x,y : x+y
print(a(4,5))
def mysquare(x):
    return x**2
mylist= [10,12,11,13,14]
mob = map(mysquare,mylist)
mylist1 = list(mob)
print("Original list:",mylist)
print("New list:",mylist1)

list = [7,9,1,3,5,20]
def odd(n):
    if n % 2!=0:
        return True
a = sorted(filter(odd,list))
for i in  a:
    print(i)

list = ['a','b','c','d','e']
vowel = ['a','e','i','o','u']
def vowels(a):
    if a in vowel:
        return True
b = filter(vowels,list)
for i in b:
    print(i)

list = [1,4,5,3]
list.sort()
print(list)
list.reverse()
print(list)
"""
