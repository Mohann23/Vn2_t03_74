'''
object is a name of  person exists physically
class is a group of activities which does not exist physically

instancemethod acts on both instance and class variables
class method acts on only class variable.

features

1.Encapsulation - combining of both state/behaviour or class/object into an entity

class - variables -logically          methods - physically
object -variables - physically        methods - logically
'''

class Employee:
    company = "accenture"
    e_count = 0

    def __init__(self, name, eid, salary):
        self.name = name
        self.eid = eid
        self.salary = salary
        Employee.e_count += 1

    def get_empdetails(self):
        print("employee details:", self.name, self.eid, self.salary)

    @classmethod
    def get_employeecount(cls):
        print("employyes count:", cls.company, cls.e_count)


sarfaraj = Employee("sarfaraj", 124563, 150000)
sarfaraj.get_empdetails()
sarfaraj.get_employeecount()

dada = Employee("dada", 2563, 234664)
dada.get_empdetails()
dada.get_employeecount()

'''
Inheritance - creating new classes from existing classes and aquire same features from it.
code reusability.
classes
1.super class     2.sub class
parent             children
company            employee
hotel              worker

#inheritance :is a relation
parent is a relation to children

# aggregation - has a relation

Animal
             |                 |
         Wild                   Domestic
         |  |                    |     |
    Tiger   Lion              Cat       Dog 

Without inheritance:
---------------------
Animal 
========
    - eating()
    - running()
    - sleeping()
    - hunting()    # Unnecessary behavior will come to all classes
    .....
    
Tiger, Lion, Cat, Dog 
======================
    Tiger        Lion              Cat         Dog 
      eating()    eating()           eating()   eating()   # Code duplication

With inheritance:
---------------------
                   Animal
        Tiger   Lion       Cat    Dog 
    
                       Animal
                         eating()            # code reusability, avoids code duplication
             |        |           |       |  
         Tiger        Lion        Cat     Dog 
      
Inheritance => is-a relationship **
Aggregation => has-a relationship  # Controller-Service-DAO layer

Tiger is a Animal     - TRUE
Lion is a Animal      - TRUE
Cat is a Animal       - TRUE
Dog is a Animal       - TRUE
SEmployee is a Animal - FALSE 


'''

class Animal:
    def __init__(self):
        print("super class:constructor ")
    def eating(self):
        print("super class: eating ")

class Lion(Animal):

    def __init__(self):
        print("sub class: constructor")

    def hunting(self):
        print("sub class: hunting")


leopard = Animal()   # returns only super class
leopard.eating()


tiger = Lion()      # returns both super and sub class
tiger.hunting()
tiger.eating()


print("____Example- 2____")
'''
             flight
              Types

1. business type       2.economy type
   food water            water
'''



class Flight:
    def __init__(self, type):
        self.type = type

    def get_type(self):
        print("buisiness or economy: ", self.type)


class Business(Flight):
    def __init__(self, name, age, ticket):
        self.name = name
        self.age = age
        self.ticket = ticket

    def get_passenger(self):
        print("passenger details in business type:", self.name, self.age, self.ticket)


t1 = Flight("buisiness type")
p1 = Business("manikanta", 26, 789654)
t1.get_type()
p1.get_passenger()


class Economy(Flight):
    def __init__(self, name, age, flightno):
        self.name = name
        self.age = age
        self.flightno = flightno

    def get_economyflightdetails(self):
        print("passenger details in economy type:", self.name, self.age, self.flightno)


t2 = Flight("Economy type")
p2 = Economy("aditya", 24, 78954)
t2.get_type()
p2.get_economyflightdetails()

print("____Example -3____")


class College:
    def __init__(self):
        print("super class: constructor")

    def get_collegename(self):
        print("college name")


class Branch(College):
    def __init__(self):
        print("sub class: constructor")

    def get_studentdetails(self):
        print("student details")


s1 = Branch()
s1.get_collegename()
s1.get_studentdetails()

print("__has a relation example____")


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