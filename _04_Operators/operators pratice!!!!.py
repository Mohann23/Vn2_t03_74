'''
print("Arithmetic operators")
x=20
y=10
print("sum",x+y)
print("sub",x-y)
print("mul",x*y)
print("div",x/y)
print("Power",x**y)
print("Floor Division",x//y)
print("Modules",x%y)
print()
'''

'''
print("Relational Operators!!!")
x=20
y=10
print()
print(x==y)
print(x!=y)
print(x<y)
print(x>y)
print(x>=y)
print(x<=y)
print()
'''


'''
print("Assignment Operators")
x=20
y=10
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)
'''


'''
print("Logical operators!!!!!!")
a=10
print(a>9 or a>50)
print(a<20 and a>9)
'''


'''
print("Membership Operators!!!!!")
a=[1,2,3,4,5]
print(1 in a)
print(6 not in a)
'''

'''
print("Identity Operator!!")
a=10
b=10
print(a is b)
print(a is not b)
'''

'''
l=[-51,50,150,250,350,450,550]
for i in l:
    if i>=1 and i<=500:
        print(i," Valid number")
    else:
        print(i,"  Invalid Number")
'''




class Personal:
    def __init__(self,name,age,cno,):     #cnumber= Contact number
        self.name=name
        self.age=age
        self.cno=cno
    def talk1(self):
        print("My name is {}, and I am {} years old, and my contact number is {}".format(self.name,self.age,self.cno))

class Office(Personal):
    def __init__(self,name, age, cno, eno, esal):
        super().__init__(name, age, cno)
        self.eno=eno
        self.esal=esal
    def talk2(self):
        print("My employee no is {}, and I am expecting around {}".format(self.eno,self.esal))

class Bankdetails(Office):
    def __init__(self, name, age, cno,eno,esal,bankname,bankaccno):
        super().__init__(name, age, cno,eno,esal)
        self.bankname=bankname
        self.bankaccno=bankaccno

    def talk3(self):
        print("My Bank details are, "
              "Bank name: {},"
              "Account number: {},".format(self.bankname,self.bankaccno))

b=Bankdetails("Mohan","23","7382719885","143","25000","Jagan Int Bank","34567891209876")
b.talk1()
b.talk2()
b.talk3()

























