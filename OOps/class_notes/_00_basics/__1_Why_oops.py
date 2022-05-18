# Object Oriented Programming System:

'''
Class - logical enity , having group of objects with data and methods
Object - it is entity with state and behaviour and it need
while create class and allocate some memory location
& Method - it is a function that is associated with an object.
------------------
Encapsulation - binding/ combining data and methods
Abstraction - hiding data and show functionality
Inheritance - inherits the properties of one class to another class
Polymorphism - different approaches
'''

# REQUIREMENT : Find Sum of  given two numbers

# STATE :   -  Data Initialization  ==> Data types/data structures
n1 = 10  # int(input("Enter number1"))
n2 = 20  # int(input("Enter number2"))

# BEHAVIOR   - Implementation       ==>  Functions
def get_sum(num1, num2):
    result = num1 + num2
    return result

print("Sum of 2 numbers is : ", get_sum(n1, n2))

'''if elif else 
   for while 
   functions 
   class 
   try except else finally 
   with
'''



# class structure
'''
class <class-name>:
        #1. STATE
    n1 = 10
    n2 = 20
    
        #2. BEHAVIOR
    def get_sum(num1, num2):
        result = num1 + num2
        return result
'''

# REQ : Display each employee information   CRUD -> RETRIEVAL
'''
CRUD 
Data type/structures
STATE
BEHAVIOR
'''
# A1 :: Using Functions
print("---------Using Functions-----------")

    # 1. STATE
empid = 100  # int(input("Enter empid :"))
name = 'Madhu Nettem'  # input("Enter name : ")
sal = 15000  # float(input("Enter sal :"))

    # 2. BEHAVIOR
def get_einfo(eid, ename, esal):
    print("Employee details are ", eid, ename, esal)

get_einfo(empid, name, sal)

# Using OOPs  -- Class
# Step 1:
class Employee:
    # 1. STATE
    empid = 100  # int(input("Enter empid :"))
    name = 'Madhu Nettem'  # input("Enter name : ")
    sal = 15000  # int(input("Enter sal :"))

    # 2. BEHAVIOR
    def get_einfo(empid, name, sal):
        print("Employee details are ", empid, name, sal)
(Employee.get_einfo(empid,name, sal ))
print("---------Using OOPs-----------")

# Step 2:
class Employee:

    # 1. STATE
    def __init__(self, empid, name, sal):
        self.empid = empid
        self.name = name
        self.sal = sal


    # 2. BEHAVIOR
    def get_einfo(self):
        print("Employee details are ", self.empid, self.name, self.sal)

# object creation
# madhu.get_einfo()
madhu = Employee(100, 'Madhu Nettem', 15000)    # x = 10
d1 = madhu.get_einfo()
print(d1)  # tuple packing unpacking
print("--------------Student example in OOPs")

class Student:

    # 1. STATE
    def __init__(self, r_no, name, marks):
        self.r_no = r_no
        self.name = name
        self.marks = marks

    # 2. BEHAVIOR
    def get_sinfo(self):
        print("Student details are ", self.r_no, self.name, self.marks)

madhu = Student(23, 'Madhu Nettem', 65)
madhu.get_sinfo()


'''
Classes combine data and functionality together. Creating a new class creates 
a new type of object, allowing new instances of that type to be made. 
Each class instance can have attributes attached to it for maintaining its state

function vs class:
--------------------
The main purpose of class is for re-usability, 
In function we can call a function any number of times. 
In class , we can create different instances of classes, but we can call functions with 
different parameters.
'''