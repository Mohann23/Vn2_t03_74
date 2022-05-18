# instance variables and instance methods:

class Passenger:
# state

    def __init__(self, name, age, date, time):  # name, age, date, time = local variables
        self.name = name
        self.age = age
        self.date = date
        self.time = time                    # self.name, self.age, self.date, self.time = instance variables
# Behaviour
# instant method

    def myfunc(self):
        print("Name of the passenger", self.name)
        print("Age of passenger", self.age)
        print("Date of journey of passenger:", self.date)
        print("Time of journey of passenger:", self.time)


p1 = Passenger("raja", 36, "25aug2021", "12.50")
p1.myfunc()


# instance method call
class Employee:

    def __init__(self, name, eid, sal):
        print("self address:", self)
        self.name = name
        self.eid = eid
        self.sal = sal

    def e_data(self):
        print("employee data:", self.name, self.sal, self.eid)

    def get_hike(self, rating):
        print("employee hike with rating:", rating)
        if rating >= 4 and rating <= 5:
            hike = self.sal*20/100
            print("hike applied:", hike)
        elif rating >= 3 and rating <= 4:
            hike = self.sal*10/100
            print("hike applied:", hike)
        elif rating >= 2 and rating <= 3:
            hike = self.sal*5/100
            print("hike applied:", hike)
        elif rating >= 1 and rating <= 2:
            hike = self.sal*0/100
            print("hike applied:", hike)
        else:
            print("no hike")


mani = Employee("manikanta", 26, 15000)
mani.e_data()
val = int(input("enter your rating:"))
mani.get_hike(val)

# 1
class Passenger:

    def __init__(self, name, age, price):
        print("self address:", self)
        self.name = name
        self.age = age
        self.price = price

    def p_data(self):
        print("employee data:", self.name, self.age, self.price)

    def get_discount(self, number):
        print("Discount with number of bookings:", number)
        if number >= 8 and number <= 10:
            discount = self.price*20/100
            print("Discount applied:", discount)
        elif number >= 5 and number <= 8:
            discount = self.price*10/100
            print("Discount applied:", discount)
        elif number >= 2 and number <= 5:
            discount = self.price*5/100
            print("Discount applied:", discount)
        elif number >= 1 and number <= 2:
            discount = self.price*0/100
            print("Discount applied:", discount)
        else:
            print("no Discount")


p1 = Passenger("manikanta", 26, 10000)
p1.p_data()
val = int(input("enter your number of bookings:"))
p1.get_discount(val)

# 2
class Appliances:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_data(self):
        print("appliance data:", self.name, self.price)

    def get_discount(self, number):
        print("discount with number of purchase:", number)
        if number >= 75 and number <= 100:
            discount = self.price*25/100
            print("Discount applied on purchase  b/w 75 to 100:", discount)
        elif number >= 50 and number <= 75:
            discount = self.price * 15/100
            print("Discount applied on purchase b/w 50 to 75:", discount)
        else:
            print("No discount")


a1 = Appliances("Bosch", 35000)
a1.get_data()
number = int(input("Enter your number of purchases:"))
a1.get_discount(number)


