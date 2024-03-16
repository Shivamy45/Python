import keyword
# This is a single line comment
a = 3 
b = 5

''' 
This
is
 a
   multiple
 line comment
'''

'''
"This is also  a multiple line comment"
print (a)
print (b)

if (b > a):
    print("b is greater than a\n")
else:
    print("b is smaller than a\n")

# To print the keywords of python
print(keyword.kwlist,"\n")
print("These are keyword list: \n", keyword.kwlist)

# Declaration
num = 100
print(num)
# Reassignment
num = 200
print(num)

# Multiple numbers with different value
a, b = 10, 20
print(a, b)

# Multiple numbers with same value
x = y = z = 1
print(x, y, z)

# Integer
n = 1_000_000
print(n)

# Decimal number
n1 = .59
print(n1)
'''

'''Data Types'''
'''
1. str = text type
2. int, float, complex = numberic type
3. list, tuple, range = sequence type
4. dict = mapping type
5. set, frozenset = set type
6. bool = boolean type
7. bytes, bytearray, memory = binary types 
'''
'''
str1 = "Hello World!"
print(str1, type(str1))

num, fnum, cnum =  1,.23,3j-2
print (num, type(num))
print(fnum, type(fnum))
print(cnum, type(cnum))

list = [1,2,3,"hello",4.3, 2+3j]
print(list, type(list))

tuple1 = ("a", .3, 12)
print(tuple1, type(tuple1))

range1 = range(1,3)
print(range1, type(range1))

dict1 = {'a':10, 'b': 3+8j, 'c':"shivam", 'd':3.4}
print(dict1, type(dict1))

stra = "100"
print(type(stra))
print(type(int(stra)))
stra = 3.5
print(type(int(stra)))
stra = 4
print(type(float(stra)))

user_input = input("Enter something: ")
print(user_input, type(user_input))

user_a = float(input("Enter a number a: "))
print("The given input is ",user_a)


print(f"{a},{b}")
print("{},{}".format(a,b))
print("{1},{0}".format(a,b))
print("The value of a and b is {} and {} respectively".format(a,b))

fnum2 = 4.2389423
print(format(fnum2, ".2f"))
print("Hello {}".format("World!"))
'''

