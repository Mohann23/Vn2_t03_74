# lambda, map, filter, reduce
# REQ: Find square of given value

# 1mark : Find square of given value 5
print("Square of value : ", 5*5)
# 2 mark : Find square of given value 5
val = 5
print("Square of value : ", val*val)

# 5 marks : Find square of given value 5
x = 6

def find_square(in_no):
    res = in_no * in_no
    return res

#sq_val = find_square(val)
print("Square of value : ", find_square(x))


# Use lambda functions  ==> map filter reduce
# https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/

sq_val = lambda num: num * num

print("Lambda  : Square of value : ", sq_val(5))

# Covert to function
def sq_val(num):
    return num*num

print("Function : Square of value : ", sq_val(5))


# scope of variable
x = 100
print("Value of x :", x)
def get_data():
    # print("Value of x :", x)
    x = 25
    print("Value of x :", x)
get_data()
print("Value of x :", x)

# Function memory allocation
x = 10
print("x details : ", x, id(x))

def get_data():
    print("Welocome to my method")
    return "Hello World"
print("__________________________")
get_data()
res = get_data()   # Function calling
print("Result is : ", res)

print("Function details ", get_data)  # Get function body address



# Mutable,Immutable :: Pass by value ,Pass by reference
# Pass by value refers to a mechanism of copying the function parameter value to another variable
# while the pass by reference refers to a mechanism of passing the actual parameters to the function.

# The main difference between pass by value and pass by reference is that,
# in a pass by value, the parameter value copies to another variable
# while, in a pass by reference, the actual parameter passes to the function.

'''
using Lambda and filter in Python :
=============================================

'''

# We can use Lambda function inside the filter() built-in function to find all the numbers

# In Python, anonymous function means that a function is without a name.

# The filter() function in Python takes in a function and a list as arguments.
# This offers an elegant way to filter out all the elements of a sequence “sequence”,
# for which the function returns True.

# divisible by 13 in the list.
print("1.Take a list of numbers")
my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70]

result = list(filter(lambda x: (x % 13 == 0), my_list))
print(result)



print("__2. checking palindromes or not__")
# palindrome == string matches with reversed string

my_list = ["mani", "madam", "xerox", "pip", "practice", "aa"]
result = list(filter(lambda x: (x == "".join(reversed(x))), my_list))
print(result)



print("3.Given a list of strings and a string str, print all anagrams of str")
# An anagram of a string is another string that contains same characters,
# only the order of characters can be different.

from collections import Counter

my_list = ["buec", "cueb", "buce", "cuba"]
str = "cube"

result = list(filter(lambda x: (Counter(str) == Counter(x)), my_list))
# print(str.count('e'))
print(result)


# using function:

def anagram(input1, input2):
    # Counter() returns a dictionary data structure which contains characters
    # of input as key and their frequencies as it's corresponding value
    return Counter(input1) == Counter(input2)
print("using normal function call")
print(anagram('abcd', 'xyza'))

print("using Driver function")
if __name__ == "__main__":
    input1 = 'abcd'
    input2 = 'dcab'
    print(anagram(input1, input2))
