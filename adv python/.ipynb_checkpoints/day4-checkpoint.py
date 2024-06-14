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
"""

class Student():
    school_name = 'Nalanda'
    #constructor
    def __init__(self,name,branch):
        self.name = name
        self.branch = branch
    @classmethod def change_school(cls):
        cls.school_name = input("Enter school name: ")
    #Instance mehtod
    def student_detail(self):
        print(Student.school_name+'\n'+self.name+'\n'+self.branch)
s1 = Student("Shivam","CSE")
s1.student_detail()
s1.change_school()
s1.student_detail()

    
