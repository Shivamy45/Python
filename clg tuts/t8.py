"""
fruits = {"Apple", "Banana", "Cherry", "Apple", "Kiwi"}

print('Unique elements:', fruits)

# Add new fruit
fruits.add("Orange")
print('After adding new element:', fruits)

# Size of the set
print('Size of the set:', len(fruits))

# check if the element is present in the set
print('Apple is present in the set:', "Apple" in fruits)
print('Mango is present in the set:', "Mango" in fruits)

# Remove the element from the set
# This will return error if "Mango" is not present
fruits.remove("Mango")
print('After removing element:', fruits)

# Discard the element from the set
fruits.discard("Mango")
print('After discarding element:', fruits)


fruits = {"Apple", "Banana", "Cherry", "Apple", "Kiwi"}
basket = frozenset(fruits)

print('Unique elements:', basket)

# Add new fruit throws an error!
basket.add("Orange")
print('After adding new element:', basket)
"""
"""
A dictionary is a collection which is unordered, changeable and indexed.
In Python dictionaries are written with curly brackets, and they have keys and values.
Values can be of any data type, and can be duplicated.
Whereas keys cannot be repeated and must be immutable.

d = {1:"Shivam",2:"Ayush", 3:"Mansi",4:"Vishal",3:"Narendra"}
print(d)
for i in range (2):
    key = input("Key: ")
    userInput = input("Value: ")
    d[key]=userInput
print(d)

"""
data1 = (1, 2, 3, 4)
data2 = ("Shivam", "Ayush", "Hello", "World")
a = dict(zip(data1,data2))
"""
print(a)
b = dict(zip(data2,data1))
print(b)
print(a[1])
print(a.get(2))
for i in a:
    print(i,":",a[i])
a[1] = "Tanishka"
print(a)
del (a[4])
print(a)
a.update({1:"Hello World", 3: "Shivam", 4:"Neyoo"})
print(a)
b = a.copy()
print(b)
a.pop(1)
print(a)
a.popitem()
print(a)
a.clear()
print(a)
print(a.keys())
print(a.values())
b = (1,2,3,4)
c = dict.fromkeys(b, 10)
print(c)
print(type(b))
print(type(c))
print(c.setdefault(6,8))
# if key is already present then it will not change the value
print(c.setdefault(3,20))
print(c.setdefault("a",5))
print(c)
"""
# l39-41,42,43,45,46