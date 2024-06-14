"""
class Account():
    def __init__(self):
        self.balance = 0
        print("Welcome")
    def deposit(self):
        amount = float(input("Enter the amount: "))
        self.balance += amount
        print("Deposit successful")
    def withdraw(self):
        withdrawal_amount = float(input("Enter the withdrawal amount: "))
        if self.balance>withdrawal_amount:
            self.balance -= withdrawal_amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")
    def net_balance(self):
        print("Net balance is",self.balance)
    
a = Account()
a.deposit()
a.withdraw()
a.net_balance()

class Student():
    school_name = 'Nalanda'
    #constructor
    def __init__(self,name,branch):
        self.name = name
        self.branch = branch
    def change_school(self):
        self.school_name = input("Enter school name: ")
    #Instance mehtod
    def student_detail(self):
        print(self.school_name+'\n'+self.name+'\n'+self.branch)
s1 = Student("Shivam","CSE")
s1.student_detail()
s1.change_school()
s1.student_detail()
print(dir(str))

a = 10
a = a.__add__(5)
print(a)

class Student():
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
        self.m1 = float(input("enter mark1"))
        self.m2 = float(input("enter mark2"))
        self.m3 = float(input("enter mark3"))
        self.m = list(map(float,input("Enter marks: ").split(",")))
    def display(self):
        print(self.name, self.roll_no)
        sum = self.m1+self.m2+self.m3
        print(sum)
        sum2 = 0
        for i in range(len(self.m)):
            sum2 += self.m[i]
        print(sum2)

s = Student("Shivam",39)
s.display()

class str():
    def __init__(self):
        self.a = input("Enter string: ")
        self.upperCase = 0
        self.lowerCase = 0
        self.others = 0
        
        self.vowel = 0
        self.consonants = 0
        self.space = 0
    def count(self):
        vowels = ['a','e','i','o','u']
        for i in self.a:
            if i.isupper():
                self.upperCase += 1
                if i in vowels:
                    self.vowel += 1
                else:
                    self.consonants += 1
            elif i.islower():
                self.lowerCase += 1
                if i in vowels:
                    self.vowel += 1
                else:
                    self.consonants += 1
            else:
                self.space += 1
                
    def display(self):
        print("UPPERCASE =",self.upperCase)
        print("lowercase =",self.lowerCase)
        print("Vowels =",self.vowel)
        print("Consonants =",self.consonants)
        print("Space =",self.space)

s = str()
s.count()
s.display()

# Magic Methods
x = 10
num = 'ABCD'
print(str(x),num)
print(x.__str__(),num.__str__(),num.__repr__())

class Person():
    def __new__(self):
        print("new method")
    def __init__(self):
        print("init method")
p = Person()

class MyClass():
    def __init__(self,value):
        self.value = value
def display(obj):
    print("value of x = ",obj.value)
obj = MyClass(10)
display(obj)
"""













































    
