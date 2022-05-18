'''
D Drive
--------
folders    books
                - c
                - python
                - java
           onlinematerial
           movies
                - english
                - hindi
                - telugu
           songs
           scanned copies
           Python



'''
'''
Windows       ==>   Folder       File
Linux         ==>   Directory    File 
P.L Python    ==>   Package      module 

Folder : all sub folders or 
         all files or
         combination of folders and files 
         
Package :   I.  all sub packages or 
           II.  all modules or 
          III.  combination of sub packages and modules 
          Example: 
            _0_maths_basics            : II. Its a package, collection of all modules 
            _00_DataStructures_Programs:  I. all sub packages
            _12_OOPs                   :III. combination of sub packages and modules
    
module : Collection of variables, functions and classes
         .py file is a module 
'''
list1 = list()
num1 = 10
num2 = -20

print(abs(num1), abs(num2))


'''
# include<stdio.h>  <==>  python - from, import    builtins.py- default module available
void main():
    printf()
    scanf()

builtins.py
===============
basics:
------
id() print() input() type()
len() max() min() sorted() sum() range()
help()
enumerate()
filter() map()    reduce() --> functools

abs()    :  To get absolute value 
all()    :
any()
ascii()
bin()
chr()
dir()
divmod()
eval()
exec()
hash()
ord() 
pow()
quit()

oops:
-------
delattr()
getattr()
hasattr()
isinstance() issubclass()
repr()
setattr()
object()
classmethod  staticmethod
classes : int  float bool str list tuple dict set 
super
zip

Exception Handling:
--------------------
BaseException
Exception
All Errors
    ArithmeticError
    AttributeError
    KeyError
    NameError
    TypeError


Iterator : 
-------------
iter() next()  
StopIteration

File Handling:
------------------
open()
enter()
exit()
'''
# from builtins import print, input, len, max, min, print, sorted, sum
print(id(10))
print("----Builtin function calls-----")
'''
print()
len()
max()
min()
print()
sorted()
sum()

'''


# int  # x = 10
# float
# bool  # istrue = True
# list
# dict  # dict1 = {}

'''
Python Modules vs Packages:
------------------------------


Modules in Python:
---------------------
A module is a file with the extension.py that contains Python executable code. 
A module is made up of a number of Python statements and expressions. 
Modules allow us to use pre-defined variables, functions, and classes. 
This cuts down on development time and allows code to be reused. 
The majority of modules are intended to tackle specific difficulties for developers
 and are designed 
to be succinct and straightforward.

Creating a Module in Python:
------------------------------
We can create a module by writing some code in a file and saving that file in a .py extension.

Let us create a module named test.py.

Example of module in Python
'''
def display():
    print("welcome to python")
if __name__ == "__main__":
    display()

'''
Importing a Module in Python:

We can import a module by using the import keyword
'''
# import class in a module


from _12_Oops.practice_oops import *



rec = Rectangle(5,3)
cr = Circle(4)
print("Perimter of rectangel: ",rec.perimeter())
print("Area of rectangel: ",rec.area())

print("Perimter of Circle: ",cr.perimeter())
print("Area of Circle: ",cr.area())


'''
We can import every object in a module by using the asterisk * operator. 

Example of importing a module in Python
'''
from  _07_core_python.test import product

product(12,22,22)
print(dir(product))

'''

dir() in Python:

Python has a built-in function called dir(). It accepts a module name as an input and returns a sorted list of all attributes and functions contained in the provided module.

Example of dir() in Python


[‘__builtins__’, ‘__cached__’, ‘__doc__’, ‘__file__’, ‘__loader__’, ‘__name__’, ‘__package__’, ‘__spec__’, ‘display’]
How Does Python Import a Module:

To import a module, Python first searches in the current directory. 
If the module doesn’t exist in the current directory, 
it then searches in all the directories present in the PYTHONPATH variable. 
If it still can’t find the directory, it then proceeds to the default directory. 
It raises a ModuleNotFoundError if it doesn’t find the module in any of the 
mentioned directories.  

We can see all the directories in the PYTHONPATH variable by using the following code.

Example of PYTHONPATH variable in Python
'''
from os import environ, pathsep
print(environ['PYTHONPATH'].split(pathsep))


'''
Packages in Python
To provide an application development environment, a python package establishes a hierarchical directory structure with several modules and sub-packages. They are nothing more than a bundle of modules and sub-packages.

Creating and Importing a Package
To create a Python package, we need to create a directory with a __init__.py file 
and a module. 
Suppose we have created a package named website with the previously 
created module test.py in it. We can import the website package by using the import keyword and a dot operator.




Python Modules vs Packages
The following are some of the distinctions between Modules and Packages: 

A Package is a directory containing numerous modules and sub-packages, 
whereas a Module is a.py file containing Python code. 
An __init__  .py file is required to create a package. 
There is no such necessity when it comes to creating modules.
We can import all objects in a module at once by using the asterisk (*) operator but we can’t import all modules in a package at once.
Packages and Modules and Functions
The principle is the same for functions, modules, and packages. They want to make it as simple as possible for code to be reused. 

Their core idea is the same, despite the fact that they appear and operate differently. 

Multiple Python statements and expressions make up a function.  Multiple Python functions make up a module and multiple Python modules make up a Package.
'''