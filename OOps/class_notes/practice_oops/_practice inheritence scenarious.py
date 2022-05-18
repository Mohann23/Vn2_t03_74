class Vehicle:
    def __int__(self):
        print("super class constructor")

    def get_vehiclename(self):
        print("input vehicle name:")


class Mileage(Vehicle):

    def __int__(self):
        print("sub class constructor")

    def get_fuel(self):
        print("fuel consumption:")


v = Vehicle()
v.get_vehiclename()

f = Mileage()
f.get_fuel()
f.get_vehiclename()


class Address:
    def __init__(self, flatno, street, city, state, pincode):
        self.flatno = flatno
        self.street = street
        self.city = city
        self.state = state
        self.pincode = pincode

    def get_address(self):
        print("get employee address:", self.flatno, self.street, self.city, self.state, self.pincode)


class Employee(Address):
    def __init__(self, name, eid, salary, address):
        self.name = name
        self.eid = eid
        self.salary = salary
        self.address = address

    def get_employeedetails(self):
        print("get employee details:", self.name, self.eid, self.salary, self.address)


addr = Address(201, "sbi colony", "anantapur", "ap", 515001)
addr.get_address()
e1 = Employee("manika", 1254, 8500, addr)
e1.get_employeedetails()

'''
Inheritance Types
1.single  : i super class 1 sub
2.multilevel : 1 super and 1 sub and 1 subsub
3. hierarchial : 1 super and two or more sub
4. hybrid  : comb of multilevel and hierarchial 
5. multiple : 1 sub and 2 or more sub class
'''


print(" single or simple type inheritence")

class Employee:
    def a(self):
        print("a type employee")

class Worker(Employee):
    def b(self):
        print("b type employee")




emp = Employee()
emp.a()
work = Worker()
work.b()
work.a()
print("multiple type  1 super and 1 sub and 1 ")

class A:
    def get_inputa(self):
        print("a")

class B(A):
    def get_inputb(self):
        print("input of b")

class C(B):
    def get_inputc(self):
        print("input c")

x = A()
x.get_inputa()

y = B()
y.get_inputa()
y.get_inputb()

z = C()
z.get_inputa()
z.get_inputb()
z.get_inputc()


print("Hierarchy type  =  1 super 2 sub or more")

class Coin:
    def get_coin(self):
        print("input coins")

class Notes(Coin):
    def get_notes(self):
        print("input notes with coins")

class Currency(Coin):
    def get_currency(self):
        print("input currency with coins")


x = Coin()
x.get_coin()

y = Notes()
y.get_coin()
y.get_notes()

z = Currency()
z.get_coin()
z.get_currency()


print("Hybrid type  = combination of multilevel and hierarchy")

print("mulitiple = 1 sub and 2 or more super class")

class A:
    def get_inputa(self):
        print("input a")

class B:
    def get_inputb(self):
        print("input b")

class C(A, B):
    def get_inputc(self):
        print("input c")



x = A()
x.get_inputa()

y = B()
y.get_inputb()

z = C()
z.get_inputa()
z.get_inputb()
z.get_inputc()
