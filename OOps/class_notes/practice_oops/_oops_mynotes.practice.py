'''
# oops - object oriented programming system: c++, java, python, smalltalk, simula-67
in this approach main task is divided into sub tasks called classes and each class is a module which contain
data and methods to achieve the task.Each class performing several inter related tasks for which several methods
written in a class

procedure oriented programming system: c, fortran, pascal
in this approach main task is divide into sub tasks and each sub task is
represented as a function/procedure.

features:
They are 5 important features in oops
1. classes and object
2.Encapsulation
3.Abstraction
4.inheritance
5.Polymorphism

# 1.classes and object:

Entire oops derived from single root concept called "object"
An object is anything that exist in real world and distinguish from others.
each object has behaviour and represented by Attributes and actions

attributes can be represented by  variables
name                              mani
age                               26  int type variable
sex                               male str type

actions   can be performed by  methods
talking                        talk()
walking                        walk()
eating                         eat()

classes:
some objects have similar behavior. such objects are belonged to same category called class
class is group name does not exist physically but objects exist physically

2.Encapsulation: combining of state and behaviour / variables and methods that act on data

3.Abstraction : hiding unnecessary data from user and expose data that is of interest to the user

4. Inheritance: creating new classes from existing classes and acquire all features of existing class

5. polymorphism: poly means many, morphos mean forms similarly, if an object or method exhibiting different
behaviour in different contexts.

'''



# flight ticket details


class Flight:
    def __init__(self, passenger, age, flightno, date, time, origin, destination):
        self.passenger = passenger
        self.age = age
        self.flightno = flightno
        self.date = date
        self.time = time
        self.origin = origin
        self.destination = destination


f1 = Flight("manikanta", "46", "Ai12548", "22aug2021", "10.30", "RGIA", "KIA")
print("Name of the passenger:", f1.passenger)
print("Age of passenger:", f1.age)
print("Flight number of passenger:", f1.flightno)
print("Travelling date and time of passenger:", f1.date, f1.time)
print("Passenger travelling origin and destination:", f1.origin, f1.destination)

# employee details


class Employee:

    def __init__(self, name, eid, salary):
        self.name = name
        self.eid = eid
        self.salary = salary


d1 = Employee("mani", 56, 15000)
print("Name of employee:", d1.name)
print("Employee id:", d1.eid)
print("Employee salary:", d1.salary)

print("____using object method____")

# 1


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("name ", self.name)
        print("age of person", self.age)


x1 = Person("raj", 199)
x1.myfunc()
# 2


class Restaurant:

    def __init__(self, chat, water):
        self.chat = chat
        self.water = water

    def myfunc(self):
        print("price of chat in restaurant:", self.chat)
        print("price of water in restaurant:", self.chat)


r1 = Restaurant(125, 25)
r1.myfunc()
# 3


class Trainticket:

    def __init__(self, train, name, age):
        self.train = train
        self.name = name
        self.age = age

    def myfunc(self):
        print("Train number :", self.train)
        print("Name of passenger:", self.name)
        print("Age of passenger:", self.age)


t1 = Trainticket(12458, "naresh", 46)
t1.myfunc()
# 4


class Mobile:
    def __init__(self, model, price, ram, camera):
        self.model = model
        self.price = price
        self.ram = ram
        self.camera = camera

    def myfunc(self):
        print("name of model:", self.model)
        print("price of mobile:", self.price)
        print("ram of mobile:", self.ram)
        print("camera of mobile:", self.camera)


m1 = Mobile("vivo", 10000, "2gb", "15mp")
m1.myfunc()
# 5


class Pen:

    def __init__(self, colour, price, brand):
        self.colour = colour
        self.price = price
        self.brand = brand

    def myfunc(self):
        print("colour of pen:", self.colour)
        print("price of pen", self.price)
        print("brand of pen:", self.brand)


p1 = Pen("blue", 10, "cello")
p1.myfunc()
# 6


class Laptop:
    def __init__(self, brand, price, processor, os, ram):
        self.brand = brand
        self.processor = processor
        self.price = price
        self.brand = brand
        self.os = os
        self.ram = ram

    def myfunc(self):
        print("brand :", self.brand)
        print("processor", self.processor)
        print("price:", self.price)
        print("os:", self.os)
        print("ram: ", self.ram)


l1 = Laptop("dell", 56000, "i5", "64bit", 2)
l1.myfunc()
# 7


class Car:
    def __init__(self, brand, price, year):
        self.brand = brand
        self.price = price
        self.year = year

    def myfunc(self):
        print("brand of car:", self.brand)
        print("price of car:", self.price)
        print("year of car:", self.year)


c1 = Car("AUDi", 5000000, 2020)
c1.myfunc()
# 8


class Jeans:
    def __init__(self, colour, price, discount):
        self.colour = colour
        self.price = price
        self.discount = discount

    def myfunc(self):
        print("colour of jeans:", self.colour)
        print("price of jeans:", self.price)
        print("discount of jeans:", self.discount)


j1 = Jeans("levis", 999, "50%")
j1.myfunc()
# 9


class Airpods:
    def __init__(self, brand, price, discount):
        self.brand = brand
        self.price = price
        self.discount = discount

    def myfunc(self):
        print("brand of airpods:", self.brand)
        print("price of airpods:", self.price)
        print("discount of airpods", self.discount)


a1 = Airpods("apple", 14000, "5%")
a1.myfunc()
# 10


class Watch:
    def __init__(self, price, brand, discount):
        self.price = price
        self.brand = brand
        self.discount = discount

    def myfunc(self):
        print("price of watch:", self.price)
        print("brand of watch:", self.brand)
        print("discount of watch:", self.discount)


w1 = Watch(5000, "fasttrack", "25%")
w1.myfunc()
# 11


class Busticket:
    def __init__(self, date, time, name, age, origin, destination):
        self.date = date
        self.time = time
        self.name = name
        self.age = age
        self.origin = origin
        self.destination = destination

    def myfunc(self):
        print("Date of journey:", self.date)
        print("Time of journey:", self.time)
        print("Name of passenger:", self.name)
        print("Age of passenger:", self.age)
        print("origin of passenger:", self.origin)
        print("Destination of passenger:", self.destination)


b1 = Busticket("23aug2021", "11.00", "karna", 32, "HYD", "BLR")
b1.myfunc()
# 12


class Tv:
    def __init__(self, brand, price, discount):
        self.brand = brand
        self.price = price
        self.discount = discount

    def myfunc(self):
        print("Brand of tv:", self.brand)
        print("Price of Tv:", self.price)
        print("Discount of Tv:", self.discount)


t1 = Tv("sony", 30000, "12%")
t1.myfunc()
# 13


class Shoes:
    def __init__(self, brand, size, discount):
        self.brand = brand
        self.size = size
        self.discount = discount

    def myfunc(self):
        print("Brand of shoes:", self.brand)
        print("Size of shoes:", self.size)
        print("Discount of shoes:", self.discount)


s1 = Shoes("puma", 9, "10%")
s1.myfunc()
# 14


class Marks:
    def __init__(self, telugu, hindi, english, maths, science, social):
        self.telugu = telugu
        self.hindi = hindi
        self.english = english
        self.maths = maths
        self.science = science
        self.social = social

    def myfunc(self):
        print("Telugu marks:", self.telugu)
        print("Hindi marks:", self.hindi)
        print("English marks:", self.english)
        print("Maths marks:", self.maths)
        print("Science marks:", self.science)
        print("Social marks:", self.social)


m1 = Marks(78, 84, 96, 99, 65, 75)
m1.myfunc()
# 15


class Hotel:

    def __init__(self, room, price, days):
        self.room = room
        self.price = price
        self.days = days

    def myfunc(self):
        print("Room type in hotel:", self.room)
        print("Price per day  in Hotel:", self.price)
        print("Number of days staying in hotel:", self.days)


h1 = Hotel("suit type", 12500, 3)
h1.myfunc()
# 16


class Washingmachine:
    def __init__(self, brand, price, mode):
        self.brand = brand
        self.price = price
        self.mode = mode

    def myfunc(self):
        print("Brand of washing machine:", self.brand)
        print("Price of washing machine:", self.price)
        print("Mode of payment in washing machine:", self.mode)


w1 = Washingmachine("Bosch", 30000, "online")
w1.myfunc()
# 17


class Movies:
    def __init__(self, temper, orange, acharya):
        self.temper = temper
        self.orange = orange
        self.acharya = acharya

    def myfunc(self):
        print("Temper movie artist:", self.temper)
        print("Orsnge movie artist:", self.orange)
        print("Acharya movie artist:", self.acharya)


m1 = Movies("ntr", "ram", "chiranjeevi")
m1.myfunc()
