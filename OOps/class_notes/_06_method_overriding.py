

'''
Method Overriding in Python - method name -same , function
================================
We can provide some specific implementation of the parent class method in our child class.
When the parent class method is defined in the child class with some specific implementation,
then the concept is called method overriding.

We may need to perform method overriding in the scenario where the different definition
of a parent class method is needed in the child class.



Method overriding is an ability of any object-oriented programming language that allows a subclass/child class
to provide a specific implementation of a method that is already provided by one of its super-classes or parent classes.
When a method in a subclass has the same name, same parameters or signature and same return type(or sub-type)
as a method in its super-class, then the method in the subclass is said to override the method in the super-class.

overriding-in-python

The version of a method that is executed will be determined by the object that is used to invoke it.
If an object of a parent class is used to invoke the method,
then the version in the parent class will be executed,
but if an object of the subclass is used to invoke the method,
then the version in the child class will be executed.


In other words, it is the type of the object being referred to (not the type of the reference variable)
that determines which version of an overridden method will be executed.




* In the process of method overriding, all the functions or methods must possess
the very same name along with similar signature
Run-time polymorphism is allied in different classes but allows us
to have the same method with the same signature name.
* It comes under run-time polymorphism. Run-time polymorphism is allied in different classes but allows us
to have the same method with the same signature name.
* Inheritance is a prerequisite in the case of method overriding.
* One can perform method overriding between both the methods- child class and parent class (or superclass).
* We use the method overriding for changing the behaviour of the methods that already exist.
* A user would always require at least two classes for implementing method overriding.
It always works with more than one class.





Example:

'''
# Python program to demonstrate
# method overriding


# Defining parent class
class Parent():
    # Constructor
    def __init__(self):
        self.value = "Inside Parent"
    # Parent's show method
    def show(self):
        print(self.value)
# Defining child class
class Child(Parent):


    def __init__(self):
        self.value = "Inside Child"
    # Child's show method
    def show(self):
        print(self.value)


# Driver's code
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()
print("___________________________")
'''
Method overriding with multiple and multilevel inheritance:
--------------------------------------------------------------
Multiple Inheritance: When a class is derived from more than one base class it is called multiple Inheritance.
Example: Let’s consider an example where we want to override a method of one parent class only. 
Below is the implementation.


# Python program to demonstrate
# overriding in multiple inheritance
  
'''
# Defining parent class 1
class Parent1():

    # Parent's show method
    def show(self):
        print("Inside Parent1")

# Defining Parent class 2
class Parent2():

    # Parent's show method
    def display(self):
        print("Inside Parent2")


# Defining child class
class Child(Parent1, Parent2):

    # Child's show method
    def show(self):
        print("Inside Child")


# Driver's code
obj = Child()
obj.show()
print("+++++++++++++++++++++++++")

'''
Multilevel Inheritance: When we have a child and grandchild relationship.
Example: Let’s consider an example where we want to override only one method of one of its parent classes. Below is the implementation.


# Python program to demonstrate
# overriding in multilevel inheritance 
  
  
# Python program to demonstrate
# overriding in multilevel inheritance 
  
'''
class Parent():

    # Parent's show method
    def display(self):
        print("Inside Parent")


# Inherited or Sub class (Note Parent in bracket)
class Child(Parent):

    # Child's show method
    def show(self):
        print("Inside Child")

# Inherited or Sub class (Note Child in bracket)
class GrandChild(Child):

    # Child's show method
    def show(self):
        print("Inside GrandChild")

# Driver code
g = GrandChild()
g.show()
g.display()
print("==========================")
'''
Calling the Parent’s method within the overridden method
Parent class methods can also be called within the overridden methods. This can generally be achieved by two ways.

Using Classname: Parent’s class methods can be called by using the Parent classname.method inside the overridden method.
Example:


# Python program to demonstrate
# calling the parent's class method
# inside the overridden method
  
'''
class Parent():

    def show(self):
        print("Inside Parent")

class Child(Parent):

    def show(self):
        # Calling the parent's class method
        Parent.show(self)
        print("Inside Child")

# Driver's code
obj = Child()
obj.show()

# Using Super(): Python super() function provides us the facility to refer to the parent class explicitly. It is basically useful where we have to call superclass functions. It returns the proxy object that allows us to refer parent class by ‘super’.
# Example 1:


# Python program to demonstrate
# calling the parent's class method
# inside the overridden method using
# super()


class Parent():

    def show(self):
        print("Inside Parent")

class Child(Parent):

    def show(self):
        # Calling the parent's class method
        super().show()
        print("Inside Child")

# Driver's code
obj = Child()
obj.show()



def product(a, b, c):
    p = a * b * c
    print(p)