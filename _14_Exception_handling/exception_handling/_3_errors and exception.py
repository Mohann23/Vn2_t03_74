'''
Errors and Exceptions in Python:
---------------------------------
Errors are the problems in a program due to which the program will stop the execution.
On the other hand, exceptions are raised when some internal events occur which
changes the normal flow of the program.
Two types of Error occurs in python.


Syntax errors: syntactical errors
Logical errors (Exceptions) : even though syntax is correct exceptions are encountered in execution


Exception	Description
-------------------------------------
IndexError: 	When the wrong index of a list is retrieved.
AssertionError:	It occurs when the assert statement fails
AttributeError:	It occurs when an attribute assignment is failed.
ImportError:	It occurs when an imported module is not found.
KeyError:	It occurs when the key of the dictionary is not found.
NameError:	It occurs when the variable is not defined.
MemoryError:	It occurs when a program runs out of memory.
TypeError:	It occurs when a function and operation are applied in an incorrect type.



Error Handling
When an error and an exception are raised then we handle that with the help of the
Handling method.


Handling Exceptions with Try/Except/Finally
We can handle errors by the Try/Except/Finally method.
we write unsafe code in the try, fall back code in except and final code in finally block.
Example
try:
    code
except :
    it will catch 1 exception
else:
    it will show other exception
finally:
    always executes show exit of code

# put unsafe operation in try block
try:
     print("code start")

     # unsafe operation perform
     print(1 / 0)

# if error occur the it goes in except block
except:
     print("an error occurs")

# final code in finally block
finally:
     print("Python")
Output:

code start
an error occurs
python


'''