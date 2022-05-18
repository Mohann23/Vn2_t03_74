# class method

class Student:
    college = "jntu"
    stud_count = 60

    def __init__(self, name, sid, marks):
        self.name = name
        self.sid = sid
        self.marks = marks
        Student.stud_count += 1
# instance method act only on instance variables

    def get_studentdata(self):
        print("student information:", self.name, self.sid, self.marks)

    @ classmethod
    def get_scount(cls):
        print("student count:", cls.college, cls.stud_count)


mani = Student("manik", 25, 600)
mani.get_studentdata()
mani.get_scount()

# 2 bus ticket

class Passenger:
    Agency = "intercity"
    pas_count = 0

    def __init__(self, name, mobile, date):
        self.name = name
        self.mobile = mobile
        self.date = date
        Passenger.pas_count += 1

    def get_passengerdata(self):
        print("passenger details:", self.name, self.mobile, self.date)

    @ classmethod
    def get_passengercount(cls):
        print("passenger count:", cls.Agency, cls.pas_count)


tarak = Passenger("Tarak", 9652256872, "25aug2021")
tarak.get_passengerdata()
tarak.get_passengercount()

arya = Passenger("arya", 1234567891, "25aug2021")
arya.get_passengerdata()
arya.get_passengercount()

ayan = Passenger("ayan", 13346485545, "25aug2021")
ayan.get_passengerdata()
ayan.get_passengercount()


print("---only class method___")

class Product:
    brand = "Bosch"
    sale_count = 0
    @ classmethod
    def get_salecount(cls):
        print("sale count details:", cls.brand, cls.sale_count)
# call class method


consumer = Product()
print("consumer address", consumer)
consumer.get_salecount()

print("___All methods___")
# movie ticket
class Movie:
    Theatre = "svc"
    sale_count = 0
    def __init__(self, moviename, date, screen):
        self.moviename = moviename
        self.date = date
        self.screen = screen
        Movie.sale_count += 1
    def get_ticketdata(self):
        print("ticket details:", self.moviename, self.date, self.screen)

    @ classmethod
    def get_salecount(cls):
        print("sale count:", cls.Theatre, cls.sale_count)
# call instance method


aditya = Movie("paagal", "25aug2021", "screen-3")
aditya.get_ticketdata()
# call class method
aditya.get_salecount()

mani = Movie("srk", "25aug2021", "screen-2")
mani.get_ticketdata()
mani.get_salecount()

class Movie:
    @staticmethod
    def getinfo():
        print("static method")

Movie.getinfo()





'''
instance variable - variables whose seperate copy is created in every instance.These are defined and initialised
by constructor with 'self' parameter.

class/static variables having only single copy to all instances of class.class variables are also called
static variables.These are defined and initialised by 'cls' parameter.

# methods: The purpose of method is process variables provided in class or method.
types:
1.instance method : To act on instance variable,we do not pass any value to self variable.
i. accesssor method: simply access or read data and do not modify data of variables.Here get_Name() is an
accessor method
ii.mutator method:modify the data and setName() is an mutator method.selfname() represents the instance variable
and rhs 'name' indicates parameter that receives new value from outside

class method : To act only on class variables

tech : stu_id, name, marks ==> instance variables
        college name        ==> class variables(share)
        attendance          ==> class variable (share+Modify)


employees : eid,name,sal   Instance vars  UNIQUE(INDIVIDUAL DATA)
            hike           class vars     instance
            comp_name      class vars     SHARABLE to all employees
            emp_count      class vars     SHARABLE + MODIFY
            attendance     class vars     SHARABLE + MODIFY


'''

