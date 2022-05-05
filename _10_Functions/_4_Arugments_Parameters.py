# REQ : Find sum of 2 given numbers

# 1. STATE
'''
num1 = int(input("Enter number1 :"))
num2 = int(input("Enter number2 :"))
'''
num1 = 10
num2 = 20


# 2. BEHAVIOR
def sum(n1, n2): # parameters
    result = n1 + n2
    print("Addition : ", result)

sum(10, 20) # arguments
sum(num1, num2)
sum(5 + 5, 10 + 1.5)

'''
From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.


9,10 : num1,num2  ==> Variables     : 10,20      ==> values
13   : n1,n2      ==> Parameters
17,18,19 :        ==> arguments     

'''
print(100)
print(40+60)


