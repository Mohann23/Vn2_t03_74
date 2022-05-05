'''
Variables that are defined inside a function body have a local scope,
and those defined outside have a global scope.

This means that local variables can be accessed only inside the function
in which they are declared, whereas global variables can be accessed
throughout the program body by all functions.

When you call a function, the variables declared inside it are brought into scope.

'''
total = 0  # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2 # Here total is local variable.
   print("Inside the function local total : ", total)
   return total
# Now you can call sum function
sum( 10, 20 )
print("Outside the function global total : ", total)

'''
There are two types of variables: global variables and local variables.

The scope of global variables is the entire program whereas the scope of
local variable is limited to the function where it is defined.
'''
def func():
    x = "Python"
    print(x)
    print(s)

s = "language"
print(s)
func()
# print(x)
'''
In above program- x is a local variable whereas s is a global variable,
we can access the local variable only within the function

it is defined (func() above) and trying to call local variable outside its scope(func()) will through an Error. However, we can call global variable anywhere in the program including functions (func()) defined in the program.

Local variables:
----------------------------
Local variables can only be reached within their scope(like func() above).
Like in below program- there are two local variables – x and y.
'''
def sum(x,y):
    sum = x + y
    return sum
print(sum(5, 10))


#print(x)
#print(y)
'''
Output
15
The variables x and y will only work/used inside the function sum() 
and they don’t exist outside of the function. 
So trying to use local variable outside their scope, might through NameError. 
So obviously below line will not work.


Global variables :
---------------------------
A global variable can be used anywhere in the program as its scope is the entire program.

Let’s understand global variable with a very simple example -
'''
z = 25
def func():
    global z
    print(z)
z=20
func()
print(z)

'''
Output
25
20
A calling func(), the global variable value is changed for the entire program.

Below example shows a combination of local and global variables and function parameters -
'''
def func(x, y):
    global a
    a = 45
#x,y = y,x
b = 33
b = 17
c = 100
#print(a,b,x,y)
a,b,x,y = 3,15,3,4
func(9,81)
print (a,b,x,y)





# 3 Using Functions  ==> 10
print("--------3 Using Functions----------")
    # I. STATE
message = 'Hello World'
    # BEHAVIOR
def get_str_len(msg):
    leng = 0
    for char in msg:
        leng = leng + 1
    print("Length of given string : ", leng)
get_str_len(message)

# With return type
message = 'Hello World' # Global
def get_str_len(msg):   # msg -> local scope
    print("String is : ",message)  # Global variable can be accesssed from anywhere
    lent = 0            # lent -> Local scope
    for char in msg:
        lent += 1
    return lent
# print(msg, lent) # Local variables cant be accessed from outside fuction
# print(msg)
# print(lent)
print(message)
str_len = get_str_len(message)   # x = 10 print(x)
print("Length of given string : ", str_len)

print("Length of given string : ", get_str_len(message))   # print(10)


# Find number is even or odd
x = 10
if x % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# Print even and odd numbers between 1 to 100
# STATE
st = 1  # int(input("Enter start number"))
end = 100  # int(input("Enter end number"))
# BEHAVIOR
def print_even_odd(ini_val, fin_val):   # evenorodd()   evenOrOdd()
    for num in range(ini_val, fin_val+1): # 100, 200 (200, 300)

        if num % 2 == 0:
            print("EVen number : ", num)
        else:
            print("Odd number  : ", num)



print_even_odd(10, 20)
print_even_odd(30, 40)

