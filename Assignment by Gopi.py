'''
# sum of multiple numbers in a list

def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return print(total)


sum_numbers([1, 2, 3, 4, 5, 6, 7, 8])
'''

'''
#Write a function to accept 2 numbers as input and return sum
# Python program to add two numbers using function
def add_num(a, b):
    sum = a + b
    return sum


num1 = int(input("input the number one: "))
num2 = int(input("input the number one :"))
print("The sum is", add_num(num1, num2))
'''

'''
#Write a function to check whether the given number is even or odd

num = int(input("Enter a number for check odd or even: "))


def find_Evenodd(num):
    if (num % 2 == 0):
        print(num, " Is an even")
    else:
        print(num, " is an odd")


find_Evenodd(num)
'''

'''
# Write a function to find factorial of given number?

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Input a number to compute the factiorial : "))
print(factorial(n))
'''

'''
#Returning multiple values from a function

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,-,*,/: ")

result = 0
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
else:
    print("Input character is not recognized!")

print(num1, ch , num2, ":", result)
'''
'''
#positional arguments

def add(a,b,c):
    return a + b + c

print (add(10,20,30))
'''

'''
#keyword arguments

def add(a,b=5,c=10):
    return (a+b+c)


print (add(b=10,c=15,a=20))

'''
'''
#default arguments

def add(a,b=5,c=10):
    return (a+b+c)

print(add(3))

'''

'''
#Variable length arguments

def add(*b):
    result=0
    for i in b:
         result=result+i
    return result

print (add(1,2,3,4,5))

'''

'''
#Table of the given number

n=int(input("Enter the number to print the tables for:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)


'''
'''
#Table of the given number using functions;;;

def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

n=int(input("Enter the number to print the tables for:"))
table(n)
    
'''

'''
#sum all the numbers in a list,set,tuple

#sum of list
listA = [1,2,3,4,5,6]
result = 0
for i in listA:
    result += i
print(result)



#print(sum(listA))
'''



'''
#sum of tuple
tuple1 = (1,2,3,4,5,6)
print(sum(tuple1))
'''

'''
#sum of set
set1 = {1,2,3,4,5,6}
print(sum(set1))
'''

'''
#multiply all the numbers in a list

def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result


list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))
'''

'''
#multiply all the numbers in a tuple

def multiplytuple(val):
    res = 1
    for ele in val:
        res *= ele
    return res

test_tup = (7, 8, 9, 1, 10, 7)
res = multiplytuple(list(test_tup))  #here i have converted the tuple to list

print("The product of tuple elements are : " + str(res))

'''

'''
#Accepts a string and calculate the numbers of upper-case letter and lower case letters

string=input("Enter string:")
count1=0
count2=0
for i in string:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
print("The number of lowercase characters is:", count1)
print()
print("The number of uppercase characters is:", count2)
print()
'''

'''
#Take a list and return a new list with unique elements of the first list

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5]))
'''

'''
#Print given Pascal's triangle
n = 5

for i in range(n):
    print(' ' * (n - i), end='')

    print(' '.join(map(str, str(11 ** i))))
'''

'''
# Function to check whether a string is a palindrome or not


string = input(("Enter a string:"))
if string == string[::-1]:
    print("The string is a palindrome")
else:
    print("Not a palindrome")
'''
'''
#check whether a number is in a given range

def test_range(n):
    if n in range(3,9):
        print(n,"is in the range",)
    else :
        print("The number is outside the given range.")
test_range(4)
'''



n=[[1,2,3],[4,5,6],[7,8,9]]
# for i in n[0]:
#     print(i,end=' ',)
# print()
# for i in n[1]:
#     print(i,end=' ')
# print()
# for i in n[2]:
#     print(i,end=' ')


# for list1 in n:
#     for elements in list1:
#         print(elements, end=' ')
#     print()















