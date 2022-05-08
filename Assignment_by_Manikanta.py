
'''
#length of the string
str1 = "Welcome to  VN2 Python Tutorials"
print("The length of the string  is :", len(str1))
'''



'''
#Count characters in string

str1 = "Welcome to VN2 Tutorials!"
str_count1 = str1.count('o')  # counting the character “o” in the given string
print("The count of 'o' is", str_count1)
'''

'''
#String slicing
String = 'Mohan'

s1 = slice(0,5)
print(String[s1])

#string[start:end:step]

'''


'''
#Length of longest string in python
list1 = ['apple', 'banana', 'watermelon', 'orange']
res = max(list1, key=len)
print("Longest String is  : ", res)
'''


'''
#First last chars swapping

def swap(string):
    # storing the first character
    start = string[0]

    # storing the last character
    end = string[-1]

    swapped_string = end + string[1:-1] + start
    print(swapped_string)

swap("Python")
'''

'''
#Remove odd index values

def odd_values_string(str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

print(odd_values_string('abcdef'))
print(odd_values_string('python'))

'''

'''
#Count words in a string
test_string = "Hello guys this is VN2 assignment by manikanta"

# printing original string
print("The original string is : " + test_string)

# using split()
# to count words in string
res = len(test_string.split())

# printing result
print("The number of words in string are : " + str(res))
'''

'''
#To check the string is lower and upper or not
#Upper lower case of a string
string = 'A Mohan Narayana'
print(string.isupper())

string = 'A Mohan Narayana'
print(string.islower())
'''


'''
#Upper lower case of a string
string = 'Assignment by manikanta'
print(string.upper())

string = 'Assignment by manikanta'
print(string.lower())
'''
'''
#Last part of string
str1 = 'Assignment-by manikanta'
print(str1.rsplit('-', 1)[0])
print(str1.rsplit(' ', 1)[0])
'''

'''
#Convert a given string to all uppercase

normal = "Assignment by manikanta"
print(normal.upper())
print(normal.lower())
'''

'''
#program to remove a newline in Python
str1='Manikanta Assignment\n'
print(str1)
print(str1.rstrip())
#When we use rstrip() then it will remove all the spaces after the string 
'''

'''
#program to check whether a string starts with specified characters
string = "Assignment with manikanta"
print(string.startswith("@345"))    #false boolean
print(string.startswith("Assi"))    #True
'''

'''
#to display a number with a comma separator
initial_num = 1000000000

thousand_sep = (format(initial_num, ',d'))

print("Number before inserting commas : " + str(initial_num))
print("Number after inserting commas: " + str(thousand_sep))

'''

'''
#to format a number with a percentage
x = 1
y = 2
print("Original Number: ", x)
print("Formatted Number with percentage: "+"{:.2%}".format(x))
print("Original Number: ", y)
print("Formatted Number with percentage: "+"{:.2%}".format(y))
'''

'''
#to count occurrences of a substring in a string
message = 'Assignment by manikanta'

# number of occurrence of 'n'
print('Number of occurrence of n:', message.count('n'))

'''

'''
#print the index of the character in a string
str1 = "Assignment by manikanta"
for index, char in enumerate(str1):
    print("Current character", char, "position at", index )
'''

'''
#convert a string in a list

def Convert(string):
    li = list(string.split(" "))
    return li


str1 = "Assignment with Manikanta"
print(Convert(str1))
'''

'''
#swap comma and dot in a string
#For swapping the , to . we need to use a function cllaed "maketrans"

amount = "12.345,678"
maketrans = amount.maketrans
amount = amount.translate(maketrans(',.', '.,'))
print(amount)
'''


'''
#count and display the vowels of a given text

def Check_Vow(string, vowels):
    final = [each for each in string if each in vowels]
    print(len(final))
    print(final)


string = "Assignment by manikanta"
vowels = "AaEeIiOoUu"
Check_Vow(string, vowels)

'''

'''
#remove spaces from a given string

def remove(string):
    return string.replace(" ", "")

string = 'A s s i g n m e n t B y M a n i k a n t a '
print(remove(string))
'''

'''
#capitalize first and last letters of each word of a given string
def capitalize_first_last_letters(str1):
    str1 = result = str1.title()
    result = ""
    for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
    return result[:-1]


print(capitalize_first_last_letters("Assignment by Manaikanta"))
'''


















