'''
Encapsulation
inheritance
abstraction
polymorpism





Encapsulation:

combining of both data and methods within a single unit.  #capsule
So, for example, when you create a class, it means you are implementing encapsulation.
A class is an example of encapsulation as it binds all the data members (instance variables)
and methods into a single unit.


Example:

In this example, we create an Employee class by defining employee attributes
such as name and salary as an instance variable
and implementing behavior using work() and show() instance methods.
'''

class Employee:
    # constructor
    def __init__(self, name, salary, project):
        # data members
        self.name = name
        self.salary = salary
        self.project = project

    # method
    # to display employee's details
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)

    # method
    def work(self):
        print(self.name, 'is working on', self.project)

# creating object of a class
emp = ('Jessa', 8000, 'NLP')

# calling public method of the class
(emp.show())
emp.work()

'''
Using encapsulation, we can hide an object’s internal representation from the outside. 
This is called information hiding.

Also, encapsulation allows us to restrict accessing variables and methods directly 
and prevent accidental data modification by creating private data members and methods 
within a class.

Encapsulation is a way to can restrict access to methods and variables from outside of class. 
Whenever we are working with the class and dealing with sensitive data, providing access to all
variables used within the class is not a good choice.
'''