'''
class, object, init, self

static method @staticmethod,
class method  cls  @classmethod,
instance method   self

method overloading





Python | Method Overloading - "method name" same - "functionality" different

Like other languages (for example, method overloading in C++) do,
python does not support method overloading by default.
But there are different ways to achieve method overloading in Python.

The problem with method overloading in Python is that we may overload the methods
but can only use the latest defined method.

* In the process of method overloading, all the functions or methods must contain the
same name with different signatures.
* It comes under compile-time polymorphism.Compile-time polymorphism allows us to have more than one method share the
same name with different signatures and different return types.
* One may or may not require inheritance in the case of method overloading.
* One can perform method overloading between methods that reside within a class.
* We use method overloading for adding more to the behavior of all the methods.
* A user won’t need more than one class for implementing method overloading.

'''
# First product method.
# Takes two argument and print their
# product
def product(a, b):
    p = a * b
    print(p)

product(4,5)
# Second product method
# Takes three argument and print their
# product
def product(a, b, c):
    p = a * b * c
    print(p)
#product(4,5)
# Uncommenting the below line shows an error
# product(4, 5) # missing 1 positional arg

# This line will call the second product method
product(4, 5, 5)

# In the above code, we have defined two product method,
# but we can only use the second product method,
# as python does not support method overloading.
# We may define many methods of the same name and different arguments,
# but we can only use the latest defined method.
#
# Calling the other method will produce an error. Like here calling product(4, 5) will produce an error
# as the latest defined product method takes three arguments.

# Thus, to overcome the above problem we can use multiple dispatch decorator to achieve the method overloading.

# Method 1 (Not The Most Efficient Method):
# We can use the arguments to make the same function work differently i.e. as per the arguments.

# +  for int ---sum, for str -- concatenate
# Function to take multiple arguments
def add(a, b):
    res = a+b
    print(res)

add('mani', 'kanta')



def add(datatype, *args):  # **kwargs
    if datatype =='int':   # if datatype is int, initialize answer as 0
        answer = 0

    if datatype =='str':  # if datatype is str, initialize answer as ''
        answer =''

    for x in args:
        answer = answer + x

    print(answer)



# Integer
add('int', 5, 6, 7 , 8)

# String
add('str', 'Hi ', 'Good ', 'morning')


# The problem with above code is that makes code more complex with multiple
# if/else statement and is not the desired way to achieve the method overloading.

# Method 2 (Efficient One):
#===================================
# By Using Multiple Dispatch Decorator
# Multiple Dispatch Decorator Can be installed by:

# pip3 install multipledispatch

from multipledispatch import dispatch

#passing one parameter
@dispatch(int,int)
def product(first,second):
    result = first*second
    print(result)

#passing two parameters
@dispatch(int,int,int)
def product(first,second,third):
    result  = first * second * third
    print(result)

#you can also pass data type of any value as per requirement
@dispatch(float,float,float)
def product(first,second,third):
    result = first * second * third
    print(result)


#calling product method with 2 arguments
product(2,3)
product(2,3,2) #this will give output of 12
product(2.2,3.4,2.6) # this will give output of 17.985999999999997

# In Backend, Dispatcher creates an object which stores different implementation and on runtime,
# it selects the appropriate method as the type and number of parameters passed.

