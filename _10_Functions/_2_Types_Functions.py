''''''
'''
# Types 
1. Builtin/ Predefined    : print() id() type()   int float str list tuple dict set
2. User defined Functions : Programmer defined functions 
'''
x = 10
'''
x  <==> variable 
10 <==> value
=  <==> Assignment operator 
'''
print("Value of x : ", x)
'''
Defining a Function: 

* You can define functions to provide the required functionality. 
Here are simple rules to define a function in Python.
* Function blocks begin with the keyword def followed by the function name and parentheses ( ).  # def <fun name>():
* Any input parameters or arguments should be placed within these parentheses. 
You can also define parameters 
inside these parentheses.
* The first statement of a function can be an optional statement - 
the documentation string of the function or docstring.
* The code block within every function starts with a colon (:) and is indented.
* The statement return [expression] exits a function, optionally passing back an expression to the caller. 
A return statement with no arguments is the same as return None.
n1 = 100
n2 =200

Function definition syntax :    def <func_name> (x) :    # f(var)
                                  # def sum(n1, n2):    # f(x)   

n1,n2 are arguments not variables
'''

# Requirement : Sum of 2 given numbers

# A. With out functions
        # I. STATE
num1 = 10
num2 = 20
        # II. BEHAVIOR
result = num1 + num2
print("Addition is : ", result)


print("-----------Using functions--------")
# B. With Functions
        # I. STATE
num1 = 10
num2 = 20
        # II. BEHAVIOR

# Function definition
def sum(n1, n2):       # function signature
    result = n1 + n2   # function body
    print("Addition is : ", result)

# Function calling/invocation
sum(10, 20)
sum(100, 200)
'''
Calling a Function
* Defining a function only gives it a name, specifies the parameters that are to be included in the function 
and structures the blocks of code.
* Once the basic structure of a function is finalized, you can execute it by calling it from another function 
or directly from the Python prompt. 

from _07_DecisionMaking._2_if_else._2_Conditions import get_st_result

marks = 44
res = get_st_result(marks)
print("Student result : ", res)
'''
'''
1. Function definition:
                                def sum(n1, n2):
                                    result = n1 + n2 
                                    print("Addition is : ", result)

    -   Function signature:
                                def sum(n1, n2):

    -  Function body/implementation
                                result = n1 + n2 
                                print("Addition is : ", result)
'''

from _10_Functions._1_basics import sum

print("addition: ", sum(23,34))