
'''
Python OOPs Concepts
------------------------------
Object Oriented Programming System:

Python is an object-oriented language, It allows  to develop applications using an Object-Oriented approach.
In Python, we can easily create and use classes and objects.

An object-oriented program is to design the program using classes and objects.
The object is related to real-word entities such as book, house, pencil, etc.
The oops concept focuses on writing the reusable code.
It is a widespread technique to solve the problem by creating objects.

Major principles of object-oriented programming system are given below.

* Class
* Object
* Method
* Inheritance
* Polymorphism
* Data Abstraction
* Encapsulation

Class:
-----------
The class can be defined as a collection of objects.
It is a logical entity that has some specific attributes and methods.

For example: if you have an employee class, then it should contain an attribute and method,
i.e. an email id, name, age, salary, etc.

Accessing Elements of Union


Syntax

class Employee:
        <statement-1>
        .
        .
        <statement-N>

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)


The __init__() Function (constructor)
---------------------------------
All classes have a function called __init__(), which is always executed when
the class is being initiated.
Use the __init__() function to assign values to object properties,
or other operations that are necessary to do when the object is being created

intialize the objects

Self parameter:
-----------------
self represents the instance of the class. By using the “self”  we can access the attributes
and methods of the class in python. It binds the attributes with the given arguments.

self instance of class
'''

class Person:
    def __init__(self, id, name, age):
        self.id = id   # self.id - instance
        self.name = name
        self.age = age

p1 = Person(36, "john", 12)  # p1 - object
p2 = Person(33, "kiran", 225) # p2 - object
print(p1)
print(p1.age)
print(p1.name, p1.id, p1.age)
print(p2.age, p2.name, p2.id)
'''
class - logical entity
object - physical entity

Object:
----------
The object is an entity that has state and behavior.
It may be any real-world object like the mouse, keyboard, chair, table, pen, etc.

Everything in Python is an object, and almost everything has attributes and methods.
All functions have a built-in attribute __doc__, 
which returns the docstring defined in the function source code.

When we define a class, it needs to create an object to allocate the memory. 
Consider the following example.

Example:
'''
class Car:
    def __init__(self,modelname, year): # attributes
        self.modelname = modelname # self - instance variables  modelname = local variables
        self.year = year
    def display(self):
        print(self.modelname,self.year)

c1 = Car("Toyota", 2016) # instance object
c2 = Car("audi", 2020)
print(c1.modelname, c1.year)
c1.display()
c2.display()

'''
Output:

Toyota 2016
In the above example, we have created the class named car, 
and it has two attributes modelname and year.
We have created a c1 object to access the class attribute.
The c1 object will allocate memory for these values.


Method:
-------
The method is a function that is associated with an object.
In Python, a method is not unique to class instances.
Any object type can have methods.
Object Methods
Objects can also contain methods. 
Methods in objects are functions that belong to the object.

Let us create a method in the Person class:
'''

print("____Insert a function that prints a greeting, and execute it on the p1 object:____")

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

'''


Inheritance:
----------------------
Inheritance is the most important aspect of object-oriented programming,
which simulates the real-world concept of inheritance.
It specifies that the child object acquires all the properties and 
behaviors of the parent object.

By using inheritance, we can create a class which uses all the properties 
and behavior of another class.
The new class is known as a derived class or child class,
and the one whose properties are acquired is known as a base class or parent class.
It provides the re-usability of the code.

parentclass

child class

Polymorphism:
--------------
Polymorphism contains two words "poly" and "morphs". Poly means many, and morph means shape.
By polymorphism, we understand that one task can be performed in different ways.

For example -
you have a class animal, and all animals speak.But they speak differently.
Here, the "speak" behavior is polymorphic in a sense and depends on the animal.

So, the abstract "animal" concept does not actually "speak",
but specific animals (like dogs and cats) have a concrete implementation of the action "speak".

Encapsulation:
--------------
Encapsulation is also an essential aspect of object-oriented programming.
It is used to restrict access to methods and variables.
In encapsulation, code and data are wrapped together within a 
single unit from being modified by accident.

combination of methods and attributes
capsule


Data Abstraction:
-----------------
Data abstraction and encapsulation both are often used as synonyms.
Both are nearly synonyms because data abstraction is achieved through encapsulation.

Abstraction is used to hide internal details and show only functionalities.
Abstracting something means to give names to things so that the name captures
the core of what a function or a whole program does.


class 


@

Object-oriented vs. Procedure-oriented Programming languages
The difference between object-oriented and procedure-oriented programming is given below:


    Object-oriented Programming	
    --------------------                             
1.	It is the problem-solving
approach and used where computation is done by using objects.	
2.	It makes the development and maintenance easier.	        
3.	It simulates the real world entity.
So real-world problems can be easily solved through oops.	    
4.	It provides data hiding. So it is more secure
than procedural languages.                                      
Procedural language doesn't provide any proper way for data binding, so it is less secure.
5.	Example of object-oriented programming languages
is C++, Java, .Net, Python, C#, etc.	                        

Procedural Programming:
1.It uses a list of instructions to do computation step by step.
2.It is not easy to maintain the codes when the project becomes lengthy.
3.It doesn't simulate the real world. It works on step by step instructions divided into small parts 
called functions.
4.You cannot access private data from anywhere.
5.Example of procedural languages are: C, Fortran, Pascal, VB etc.


'''

