'''
Polymorphism means multiple forms. In python we can find the same operator or function
taking multiple forms. It also useful in creating different classes which will have
class methods with same name.
That helps in reusing a lot of code and decreases code complexity.
Polymorphism is also linked to inheritance as we will see in some examples below.

Polymorphism in operators:
----------------------------
The + operator can take two inputs and give us the result depending on what the inputs are.
In the below examples we can see how the integer inputs yield an integer and
if one of the input is float then the result becomes a float.
Also for strings, they simply get concatenated.
This happens automatically because of the way the + operator is created in python.



Eg: + does different int, string
    len() - for string it return each element count, tuple, list , it return each iteration count
    class methods: Having same methods with different functionality it will call when object bound with respective
    classes. area, perimeter
Example
'''
a = 23
b = 11
c = 9.5
s1 = "Hello"
s2 = "world"
print(a + b)
print(type(a + b))
print(b + c)
print(type (b + c))
print(s1 + s2)
print(type(s1 + s2))


# Polymorphism in in-built functions
# We can also see that different python functions can take inputs of different types
# and then process them differently.
# When we supply a string value to len() it counts every letter in it.
# But if we five tuple or a dictionary as an input, it processes them differently.


str = 'Hi There !' # 10
tup = ('Mon','Tue','wed','Thu','Fri')  # 5
lst = ['Jan','Feb','Mar','Apr', 11]  #  5
dict = {'1D':'Line','2D':'Triangle','3D':'Sphere'}  # 3
print(len(str))
print(len(tup))
print(len(lst))
print(len(dict))

# Polymorphism in user-defined methods
# We can create methods with same name but wrapped under different class names.
# So we can keep calling the same method with different class name pre-fixed
# to get different result.
# In the below example we have two classes, rectangle and circle to get their
# perimeter and area using same methods.

from math import pi

class Rectangle:
   def __init__(self, length, breadth):
      self.l = length
      self.b = breadth
   def perimeter(self):
      return 2*(self.l + self.b)
   def area(self):
      return self.l * self.b

class Circle:
   def __init__(x, radius):
      x.r = radius
   def perimeter(x):
      return 2 * pi * x.r
   def area(x):
      return pi * x.r ** 2

# Initialize the classes
rec = Rectangle(5,3)
print(rec.perimeter())
print(rec.area())


r2 = Rectangle(100,440)
print(r2.perimeter())
print(r2.area())

print("Perimter of rectangel: ",rec.perimeter())
print("Area of rectangel: ",rec.area())

cr = Circle(4)

print("Perimter of Circle: ",cr.perimeter())
print("Area of Circle: ",cr.area())

