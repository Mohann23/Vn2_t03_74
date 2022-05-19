'''
The errors in software development is called "Bugs"
and process of removing them is called Debugging.

robust means strong which purpose of handling errors is called robust

Errors  in a python program (CT R l)
1. compile-time errors: syntactical errors found in the code due to program
which a program fails to complete

2. Run time errors: when PVM does not execute byte code it flags runtime error.
Runtime errors are not detected by PVM

3.Logical errors: it occurs when programmer using wrong design or formula ,
it detects by programmer only.





                   # exaples of compilation-time errors  : ;  indentation
-------------------------------------------------------
x = 1
if x == 1:        # if : removes shows invalid syntax Ex.of compile-time errors
    print("where is the colon?")

x = 10
if x % 2 == 0:
    print(x, "divisible by 2")
    print(x, "x is even number")  # if again indentation as from line 20 shows indentation error

# examples of runtime errors : + with str, num raises error
#-----------------------------------------------


def concat(a, b):
    print(a+b)

concat('hai', 25)
# here we concat two arguments with + operator data types are not checked by compiler , 
by PVM returns Type error

animal = ["dog", "cat", "Horse", "Lion"]
print(animal[4])

# here we get list index out of range


# Examples of logical errors : using wrong formulas here output gives increment only not total
-------------------------------------------------
'''
def increment(sal):
    sal = (sal * 15/100) # sal = sal * 15/100 gives only increment amount not added to original salary
    return sal

sal = increment(5000.00)
print('incremented sal= %2f' %sal)
# This is wrong here we get only
# here we have to use sal = sal+(sal*15/100)

print("___Exception:____")
'''
-------------

# Exception is a runtime error which can be expected by programmer and eliminated which make harm caused to program
if programmer cannot do anything in cause of an error , then it is called an error and not an exception.
All exceptions are represented as classes in python .The exceptions which are available in python called
BUILTIN EXCEPTIONS.The base class for builtin function are called BASE EXCEPTION
From base class, subclass exception derived .from exception standard error and warning derived

All errors are defined as subclass of standard error , An error should be handled otherwise program will not execute
all warnings should be derived as subclass from "warning class"

User defined exceptions are created by own exceptions in program

           Base Exception
             exception
Standard error  (asterin) warning (rid)
1. Arthemetic error      Deprecation warning
2. Assertion error       Runtime warning
3.Syntax error           import warning
4.Type error
5.EOF error
6.Runtime error
7.Import Error
8.Name error

 Exception : handling of errors called exception and make program robust means strong.Robust program doesnot
 terminate in middle and display appropriate message where error occured

 Exception handling: the program in which performing try,except,finally tasks

 try:
     statements (observe where there may  possibility exception ,write in try block.Even error in statement
     doesnot terminate by PVM allows to except block
 except: exception name
       statement (write exception name which helps to user to understand where error is in statement )
 finally:
        statements( in this block closing actions terminate the process whether it is running

'''
try:
    f = open("myfile", 'w')
    a, b = [int(x) for x in input("enter two numbers:").split(',')]
    c = a/b
    f.write("writing %d into my file" %c)
except ZeroDivisionError:
    print("division by zero happened")
    print("please do not enter 0 in input")
finally:
    f.close()
    print("file closed")

try:
    f = open("myfile1",'w')
    x, y = [int(i) for i in input("enter two numbers: ").split(',')]
    c = x/y
    f.write("writing %d in myfile1"%c)
except ZeroDivisionError:
    print("Zero division error happened")
    print("please donot enter 0 in input")
finally:
    f.close()
    print("file closed")

# program to handle syntax error
try:
    date = eval(input("enter date: "))
except:
    print("invalid date entered")
finally:
    print("you entered:", date)


# program to handle IOE error
try:
    name = input("enter filename:   ")
    f = open(name, 'r')
except IOError:
    print("file not found", name)
finally:
    n = len(f.readlines())
    print(name, 'has', n, 'lines')
    f.close()

try:
    filename = input("enter filename to open: ")
    f = open(filename, 'r')
except IOError:
    print("file not found", filename)
finally:
    n = len(f.readlines())
    print(filename, "has", n, 'lines')
    f.close()



# program to handle multiple exception

def avg(list):
    tot=0
    for x in list:
        tot+=x
    avg = tot/len(list)
    return tot, avg

try:
    t, a = (avg([1, 2, 3, 4, 5]))
    print('Total = {}, Average = {}'.format(t, a))
except TypeError:
    print('Type error, please provide numbers.')
except ZeroDivisionError:
    print("zeroDivisionError, please do not give empty list")

def avg(tup):
    tot = 0
    for x in tup:
        tot += x
    avg = tot/len(tup)
    return tot, avg

try:
    total, average = avg((1, 5, 8, 15, 75, 78))
    print("Total = {}, Average = {}".format(total, average))
except TypeError:
    print("type erro please enter numbers only ")
except ZeroDivisionError:
    print("zeroDivisionError", "please donot give empty tuple")


                 # Except block

# program to understand usage og try block
try:
    x = int(input('enter a number:'))
    y = 1/x
finally:
    print("we are not catching exception")
    print("inverse is :", y)



# assert statement raises an error when the statement is not true

try:
    x = int(input("enter number between 5 and 10 : "))
    assert x >= 5 and x <= 10
    print("the number entered :", x)
except AssertionError:
    print("condition is not fulfiled")



try:
    x = int(input("enter numbers between 1 and 50: "))
    assert x >= 1 and x <= 100, 'your input is not correct'
    print("The number you entered: ", x)
except AssertionError as obj:
    print(obj)


# user defined exceptions

# create our own class and raise it when needed


class MyException(Exception):

    def __init__(self, arg):
        self.msg = arg

    def check(dict):
        for k, v in dict.items():
            print("Name= {:15s} Balance= {:10.2f}".format(k, v))
            if(v<2000.00):
                raise MyException("Balance amount in the account", +k)
    bank = {'sharma': 5000.00, 'kiran': 7500.00, 'dev': 900.15}
    try:
        check(bank)
    except Exception as me:
        print(me)

# Logging the exceptions:
'''
critical - 50  serious message
error = 40     serious error
warning = 30   caution needed warns to programmer
info - 20      important information
debug =10      debugging notification
notset = 0      reports level not set
'''

import logging
from logging import *
# store messages in logfile
logging.basicConfig(filename='mylog.txt', level=logging.ERROR)

# store messages into the file
logging.error("There is an error in prgram")
logging.critical("There is a problem in design")
# but these are not stored
logging.warning("the project is going slow")
logging.info("you are a junior programer")
logging.debug("lineno.10 contains syntax error")



# program to store messages released by any exception

import logging
logging.basicConfig(filename='log.txt', level=logging.ERROR)
try:
    a = int(input("enter a number:"))
    b = int(input("enter another number: "))
    c = a/b
except Exception as e:
    logging.exception(e)
else:
    print("the result of division: ", c)