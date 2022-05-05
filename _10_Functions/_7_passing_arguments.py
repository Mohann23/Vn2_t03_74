# Passing Arguments
'''
1. Positional arguments (Required arguments)
2. Default arguments
3. Keyword arguments (Named arguments)
'''
x = 10    # int x = 10


# 1. Positional arguments (Required arguments)
'''
Required arguments are the arguments passed to a function in correct positional order. 
Here, the number of 
arguments in the function call should match exactly with the function definition.
'''
print("--------1. Positional arguments--------------")

def sum(n1, n2, n3):   # sum(int n1, int n2, int n3) sum(int n1, String n2, List n3)
    print("In sum method : with vals :", n1, n2, n3)
    res = n1 + n2 + n3
    print("Sum is : ", res)

sum(10, 20, 30)
#sum(10, 20)            # TypeError: sum() missing 1 required positional argument: 'n3'3#
#sum(10, 20, 30, 40)    # TypeError: sum() takes 3 positional arguments but 4 were given


# 2. Default arguments
'''
A default argument is an argument that assumes a default value 
if a value is not provided in the function call 
for that argument
'''
print("--------2. Default arguments-------------")
def sum(n1, n2, n3 = 1000):
    res = n1 + n2 + n3
    print("Sum is : ", res)

sum(10, 20)      # n3 = 1000
sum(10, 20, 30)  # n3 = 1000 will be overriden with 30
#sum(10)          # sum() missing 1 required positional argument: 'n2'
#sum(10, 20, 30, 40)  # Additional argument




def sum(n1, n2 = 500, n3 = 1000):
    res = n1 + n2 + n3
    return res

print("One argument     :", sum(10))   # 1510
print("Two argument     :", sum(10, 20))  # 1030
print("Three argument   :", sum(10, 20, 30))  # 60
#print("Zero argument    :",sum())
# print("Extra arguments  :",sum(10,20,30,40))

def sum(n1 = 100, n2 = 500, n3 = 1000):
    res = n1 + n2 + n3
    return res

print("Zero argument     :", sum())
print("One argument     :", sum(10))
print("Two argument     :", sum(10, 20))
print("Three argument   :", sum(10, 20, 30))


def sum(n2, n1=1, n3=1000):
    res = n1 + n2 + n3
    print("Sum is : ",res)


# FUNCTION OVERLOADING
sum(10)


# 3. Keyword arguments (Named argument)
'''
Keyword arguments
* Keyword arguments are related to the function calls. 
When you use keyword arguments in a function call, 
the caller identifies the arguments by the parameter name.
* This allows you to skip arguments or place them out of order because the Python interpreter is able 
to use the keywords provided to match the values with parameters. 
'''


print("--------3. Keyword arguments-------------")
def sum(n1, n2, n3):
    res = n1 + n2 + n3
    print("Sum1 is : ", res)

sum(10, 20, 30)          # 1.Positional/Required
sum(n2=10, n3=20, n1=30)
sum(n1=30, n2=10, n3=20)

def get_order_info(mobile, ref_no, order_no, quanity, price):
    print("Order details :")
    print(order_no, ref_no, quanity, price, mobile)

get_order_info(8975435643, 9865432132, 1234, 40, 65876) # positional args
get_order_info(ref_no=9865432132, order_no=1234, quanity=40, price=65876, mobile=8975435643)
get_order_info(mobile=8975435643, quanity=40, price=65876, order_no=1234, ref_no=9865432132)



def sum(n1, n2, n3 = 45):
    res = n1 + n2 + n3
    print("Sum is : ", res)

sum(10, 20)     #  Positional
sum(n2=10, n3=20, n1=30) # Keyword
sum(n2=10, n1=30)          # Default + Keyword
sum(20,n3=30, n2=10)          # Positional + Default + Keyword


list1 = [1, 2, 3, 4]
list1.insert(1, 1000)   # insert(index, value)
# list1.insert(1000)
print(list1)

list1.pop()             # def pop(index = -1): body
list1.pop(2)
print(list1)