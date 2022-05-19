'''
Python Try Except:
---------------------
Error in Python can be of two types i.e. Syntax errors and Exceptions.
Errors are the problems in a program due to which the program will stop the execution.
On the other hand, exceptions are raised when some internal events occur which changes
the normal flow of the program.
Note: For more information, refer to Errors and Exceptions in Python
Some of the common Exception Errors are :


IOError: if the file can’t be opened
KeyboardInterrupt: when an unrequired key is pressed by the user
ValueError: when built-in function receives a wrong argument
EOFError: if End-Of-File is hit without reading any data
ImportError: if it is unable to find the module


Try Except in Python:
----------------------
Try and Except statement is used to handle these errors within our code in Python.
The try block is used to check some code for errors.

i.e the code inside the try block will execute when there is no error in the program.
Whereas the code inside the except block will execute whenever the program encounters
some error in the preceding try block.


Syntax:

try:
    # Some Code
except:
    # Executed if error in the
    # try block
How try() works?:
---------------------


First, the try clause is executed i.e. the code between try and except clause.
If there is no exception, then only the try clause will run, except the clause is finished.
If any exception occurs, the try clause will be skipped and except clause will run.
If any exception occurs, but the except clause within the code doesn’t handle it,
it is passed on to the outer try statements.
If the exception is left unhandled, then the execution stops.
A try statement can have more than one except clause

Code 1: No exception, so the try clause will run.

# Python code to illustrate
# working of try()
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")

# Look at parameters and note the working of Program
divide(3, 2)
Output :


('Yeah ! Your answer is :', 1)
Code 1: There is an exception so only except clause will run.



# Python code to illustrate
# working of try()
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")

# Look at parameters and note the working of Program
divide(3, 0)
Output :


Sorry ! You are dividing by zero


Else Clause
In python, you can also use the else clause on the try-except block which must be present after all the except clauses. The code enters the else block only if the try clause does not raise an exception.


Syntax:

try:
    # Some Code
except:
    # Executed if error in the
    # try block
else:
    # execute if no exception
Code:


# Program to depict else clause with try-except

# Function which returns a/b
def AbyB(a , b):
    try:
        c = ((a+b) // (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
Output:

-5.0
a/b result in 0


Finally Keyword in Python
Python provides a keyword finally, which is always executed after the try and except blocks.
The final block always executes after normal termination of try block or after try
block terminates due to some exceptions.


Syntax:

try:
    # Some Code
except:
    # Executed if error in the
    # try block
else:
    # execute if no exception
finally:
    # Some code .....(always executed)
Code:


# Python program to demonstrate finally

# No exception Exception raised in try block
try:
    k = 5//0 # raises divide by zero exception.
    print(k)

# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')
Output:

Can't divide by zero
This is always executed


'''