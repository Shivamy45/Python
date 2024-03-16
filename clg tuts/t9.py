import string
"""
A string is a sequence of characters
String literals in python are surrounded by either single quotion marks, double quotation marks.

a = input().split(" ")
b = {}
for i in range(0,len(a),2):
    b.update({a[i]:a[i+1]})
print(b)

s = "Hello World!"
print(s[4])
print(s[:])
print(s[4:])
print(s[:4])
print(s[2:6])
print(s[2:6:2])
print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.punctuation)
print(string.digits)
print(string.octdigits)
print(string.hexdigits)

s = "Hello Dear Students"
print(s.endswith('s'))
print(s.startswith('S'))
print(s.replace('r','n'))
print("123h".isdigit())
print("abcd2".isalpha())
print("ajf34".isalnum())
print("5.67".isdecimal())
print("Hello Niet".istitle())

print("hello".upper())
print("HELLO".lower())
print("hElLo".swapcase())
s = "Hello everyone\nMyself Shivam"
print(s.partition("o"))
print(s.index('S'))
print(s.rindex('o'))
print(s.splitlines(True))
print(s.capitalize())
print(s.find("el"))
print(s.rfind("el"))
print(s.count("el"))
print(max(s))
print(min(s))
print(len(s))
"""