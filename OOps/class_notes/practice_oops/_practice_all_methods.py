'''
oops - object oriented programming system - c++, java, python
procedure oriented programming - c,fortran, pascal

state:
variables:
1. instance variables: self data /not sharable
2. class variables : sharable data
student : name, rollno, marks, fees are variables
          college - class variable
          attendance - class variable (sharable +modify)

Behavior:
methods:
1.class methods : Act only on class variable
2.instance methods : acts on instance variable or acts on both class and instance variables.
3.static method : acts on neither class nor instance variables

CM --- CV
IM ---IV,CV

features of oops

class:class is a group of objects   eg.company, college
object: object is anything that exists in real world.eg:name of person, age exist physically
1.Encapsulation : combining fields and methods into single entity
2.Abstraction: hiding unnecessary data from user and expose when it is interested of by user.
3.Inheritance: creating new classes from existing class and aquire same features from existing class.
4.polymorphism: poly means many morphos means forms.if an object exhibiting different behavior in different context

'''

print("___1.hostel example_____")
class Hostel:
    hostelname = "Brindavan pg"
    occupancy_count = 0

    def __init__(self, name, age, address, mobile, purpose, doj, duration, emergency_contact, fees, advance,
                 father_name, maintainance):
        self.name = name
        self.address = address
        self.age = age
        self.mobile = mobile
        self.purpose = purpose
        self.doj = doj
        self.duration = duration
        self.emergency_contact = emergency_contact
        self.fees = fees
        self.advance = advance
        self.father_name = father_name
        self.maintainance = maintainance
        Hostel.occupancy_count += 1

    def get_occupantdata(self):
        print("occupant data:", self.name, self.age, self.address, self.mobile, self.purpose, self.doj,
              self.duration, self.emergency_contact, self.fees, self.advance, self.father_name, self.maintainance)

    @classmethod
    def get_occupantcount(cls):
        print("occupant count:", cls.hostelname, cls.occupancy_count)

    def get_discount(self, number):
        print("discount applied:", number)
        if number >= 3 or number <= 5:
            discount = self.fees*20/100
            print("discount applied on 3 to 5 members:", discount)
        elif number >= 1 and number <= 3:
            discount = self.fees*10/100
            print("discount apllied on 1 to 3 members:", discount)
        else:
            print("no discount")


manikanta = Hostel("Manikanta D", 26, "ATP", 9652256872, "education", "25aug2021", "3months", 6281651717, 6500,
                   3000, "Govindappa.D", 1500)
manikanta.get_occupantdata()
number = int(input("enter number of members joined:"))
manikanta.get_discount(number)
manikanta.get_occupantcount()

faran = Hostel("fran", 25, "blr", 78956, "work", "26aug", 1, 78945, 6500, 3000, "jahan", 1500)
faran.get_occupantdata()
number = int(input("enter number of members joined:"))
faran.get_discount(number)
faran.get_occupantcount()

print("_______2.student example______")

class Student:
    college = "Srit"

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def get_studentdata(self):
        print("student data:", self.name, self.age, self.marks)

    @ classmethod
    def get_college(cls):
        print("college name:", cls.college)


s1 = Student("manu", 26, 300)
s1.get_studentdata()
s1.get_college()
print("---------3.Ajio example")

class Ajio:
    brandname = "levis"
    sale_count = 0

    def __init__(self, name, age, address, mobile, outfit, price):
        self.name = name
        self.address = address
        self.age = age
        self.mobile = mobile
        self.outfit = outfit
        self.price = price
        Ajio.sale_count += 1

    def get_consumerdata(self):
        print("occupant data:", self.name, self.age, self.address, self.mobile, self.outfit, self.price)

    @classmethod
    def get_salecount(cls):
        print("sale count:", cls.brandname, cls.sale_count)

    def get_discount(self, number):
        print("discount applied:", number)
        if number >= 3 or number <= 5:
            discount = self.price*20/100
            print("discount applied on 3 to 5 members:", discount)
        elif number >= 1 and number <= 3:
            discount = self.price*10/100
            print("discount applied on 1 to 3 members:", discount)
        else:
            print("no discount")


manikanta = Ajio("Manikanta D", 26, "ATP", 9652256872, "jeans", 3000)
manikanta.get_consumerdata()
number = int(input("enter number of purchase:"))
manikanta.get_discount(number)
manikanta.get_salecount()

print("---------4.Hotel example")

class Hotel:
    hotel_name = "Taj bangalore"
    occupancy_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Hotel.occupancy_count += 1

    def get_customerdata(self):
        print("customer data:", self.name, self.age)

    @ classmethod
    def get_occupancycount(cls):
        print("Occupancy details:", cls.hotel_name, cls.occupancy_count)

    def get_discount(self, number):
        print("discount on number on booking:", number)
        if number >= 3 and number <= 5:
            print("discount:", 1500)
        elif number >= 1 and number <= 3:
            print("discount:", 1000)
        else:
            print("no discount")


p1 = Hotel("mani", 25)
number = int(input("number of rooms booked:"))
p1.get_occupancycount()
p1.get_discount(number)

print("---------5.Amazon purchase example")

class Amazon:
    brand = "mi"
    sale_count = 0

    def __init__(self, customername, mobileno, price):
        self.customername = customername
        self.mobileno = mobileno
        self.price = price
        Amazon.sale_count += 1

    def get_customerdetails(self):
        print("Customer details:", self.customername, self.mobileno, self.price)

    @ classmethod
    def get_salecount(cls):
        print("Sales details:", cls.brand, cls.sale_count)

    def get_offer(self, produtno):
        print("offer based on number of products purchased:", produtno)
        if produtno >= 10 or productno <= 20:
            offer = self.price*produtno*.25
            print("offer applied on purchase of 1 to 20:", offer)
        else:
            print("no offer")


ram = Amazon("Ram", 9652256872, 25000)
ram.get_customerdetails()
productno = int(input("enter number of products to be purchased:"))
ram.get_salecount()
ram.get_offer(productno)
