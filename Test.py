'''

class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def talk(self):
        print("Hello my name is {}, I am {}, and I got {} percentage in my 10th class".format(self.name,self.age,self.marks))

s=Student("Noor",26,85)
s.talk()
'''

'''
class Test:
    def __init__(self):
        print("Constructor Executed!!!")

    def m1(self):
        print("Method Executed!!!")

t1=Test()
t2=Test()
t1.m1()
'''


'''
#Static Variable!!!!!!!!!!!!
class Test:
    def __init__(self):
        self.a=10
        self.b=20
    def change(self):
        self.c=30

t1=Test()
t2=Test()
print("t1",t1.a,t1.b)
print("t2",t2.a,t2.b)
print(t1.a)
print(t1.b)
t1.a=100
t2.b=200
print("t1",t1.a,t1.b)
print("t2",t2.a,t2.b)'''

'''
#Bank example

import sys
class Customer:
    """Customer class with bank operations"""
    bank_name="Mohan_Bank"
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print("Balance after deposit:",self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print("Insufficient Funds..Can't perform this opertion")
            sys.exit()
        self.balance=self.balance-amt
        print("Balance after withdraw:",self.balance)

print("Welcome to",Customer.bank_name)
name=input("Enter your name:")
c=Customer(name)
while True:
    print("d=Deposit \nw-Withdraw \ne-Exit")
    option=input("Choose your option:")
    if option=="d" or option=="D":
        amt=float(input("Enter amount:"))
        c.deposit(amt)
    elif option=="w" or "W":
        amt=float(input("Enter amount:"))
        c.withdraw(amt)
    elif option=="e" or option=="E":
        print("Thanks for Banking")
        sys.exit()
    else:
        print("Invalid option... Plz Choose valid option")

'''

'''
Duck typing philosophy of python!!!!

class Duck:
    def talk(self):
        print("Quack.. Quack..")

class Dog:
    def talk(self):
        print("Bow..Bow..")

def f1(obj):
    obj.talk()

l=[Duck(),Dog()]
for obj in l:
    f1(obj)

'''




'''

#Banking application

import sys
class Customer:
    bank_name="Vn2 solutions!!"
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance

    def deposite(self,amt):
        self.balance=self.balance+amt
        print("Avaialbe balance after the deposit is: ",self.balance)

    def withdrawal(self,amt):
        if amt>self.balance:
            print("In sufficient funds.. Try again!!")
            sys.exit()
        elif amt<=self.balance:
            self.balance=self.balance-amt
            print("Availabe balance after the withdrawal is: ",self.balance)

print("Welcome to Vn2 Solutions bank ")
name=input("Enter your Name: ")
c=Customer(name)
while True:
    print("d=deposit \nw-Withdraw \ne=Exit")
    option=input("Select any option: ")
    if option=="d" or option=="D":
        amt=float(input("Enter The amount: "))
        c.deposite(amt)

    elif option=="w" or option=="W":
        amt=float(input("Enter The amount: "))
        c.withdrawal(amt)

    elif option=="e" or option=="E":
        print("Thanks for banking with us!!!")
        sys.exit()

    else:
        print("Enter valid input...")

'''

'''
days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")


while True:
    num = int(input("Enter the Number:"))
    if num==1:
        print(days[0])
    elif num==2:
        print(days[1])
'''




























