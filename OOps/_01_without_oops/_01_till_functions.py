# OOPs concepts:



'''
1. Data structures  - 3. STATE
2. CRUD operation   - 4. BEHAVIOR
'''

# REQ: Find length of the given string
print("-------1. Using builtin function-------")
str1 = 'hello world'
print("Length of string : ", len(str1))

print("-------2. Using algorithm i.e, Without functions-------")

    # 1. STATE
str1 = 'hello world'

    # 2. BEHAVIOR
le = 0
for char in str1:
    le += 1
print("Length of string : ", le)

print("-------2. With functions-------")

    # 1. STATE
str1 = 'hello world'

    # 2. BEHAVIOR
def find_length(in_str=None):
    le = 0
    for char in in_str:
        le += 1
    return le

print("Length of string : ", find_length(str1)) # 1. single time usage  print(10)
str_len = find_length(str1)                     # 2. multiple places    x = 10 print(x)
print("Length of string : ", str_len)

# 3. print responsibility is taken by function only
def find_length(in_str):
    le = 0
    for char in in_str:
        le += 1
    print("Length of string : ", le)
find_length(str1)

print("Value of x : ", 10)
x = 10
print("Value of x : ", x)




