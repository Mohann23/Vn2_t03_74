'''
File Handling in Python:
-------------------------
Python too supports file handling and allows users to handle files i.e., to read and write files,
along with many other file handling options, to operate on files.

1 The concept of file handling has stretched over various other languages, but the implementation is either complicated
or lengthy compare to Python which is easy and short.
2. Python treats file differently as text or binary and this is important. Each line of code includes a sequence of
characters and they form text file.
3. Each line of a file is terminated with a special character, called the EOL or End of Line characters like comma {,}
or newline character.
4.It ends the current line and tells the interpreter a new one has begun.



Let’s start with Reading and Writing files.

Working of open() function:
---------------------------
Before performing any operation on the file like read or write, first we have to open that file.
For this, we should use Python’s inbuilt function open()

But at the time of opening, we have to specify the mode, which represents the purpose of the opening file.

f = open(filename, mode)
Where the following mode is supported:

r: open an existing file for a read operation.
w: open an existing file for a write operation. If the file already contains some data then it will be overridden.
a:  open an existing file for append operation. It won’t override existing data.
r+:  To read and write data into the file. The previous data in the file will not be deleted.
w+: To write and read data. It will override existing data.
a+: To append and read data from the file. It won’t override existing data.

'''
# Take a look at the below example:

# a file named "exp1", will be opened with the reading mode.
print("read mode")
file = open('exp1.txt', 'r')
# This will print every line one by one in the file
for each in file:
    print(each)

'''
# The open command will open the file in the read mode and the 
for loop will print each line present in the file.


Working of read() mode
-----------------------
There is more than one way to read a file in Python. If you need to extract a string that contains all 
characters in the file then we can use   "file.read()"
'''
# Python code to illustrate read() mode
file = open("exp1.txt", "r")
print(file.read())

'''
Another way to read a file is to call a certain number of characters like in the following code the interpreter 
will read the first five characters of stored data and return it as a string:

# Python code to illustrate read() mode character wise
'''
file = open("file.txt", "r")
print (file.read(5))
'''


Creating a file using write() mode:
======================================
Let’s see how to create a file and how write mode works:
To manipulate the file, write the following in your Python environment:
'''
# Python code to create a file
file = open('exp2.txt','w')
file.write("This is the write command \n")
file.write("It allows us to write in a particular file \n")
file.close()
'''
#The close() command terminates all the resources in use and frees the system 
of this particular program.


Working of append() mode:
==========================
Let’s see how the append mode works:
'''
# Python code to illustrate append() mode
x = open('exp2.txt','a')
x.write("This will add this line \n")
x.close()

'''
There are also various other commands in file handling that is used to handle 
various tasks like:

rstrip(): This function strips each line of a file off spaces from the right-hand side.
lstrip(): This function strips each line of a file off spaces from the left-hand side.

It is designed to provide much cleaner syntax and exception handling when you are working with code. 
That explains why it’s good practice to use them with a statement where applicable. 
This is helpful because using this method any files opened will be closed automatically after one is done, so auto-cleanup.
Example:
'''
# Python code to illustrate with()
with open("file.txt", 'r') as file:
    data = file.read()
    print(data)


# Using write along with the with() function
# We can also use the write function along with the  with() function:

# Python code to illustrate with() alongwith write()
with open("file.txt", "w") as f:
    f.write("Hello World!!! \n")


# split() using file handling
# We can also split lines using file handling in Python.
# This splits the variable when space is encountered.
# You can also split using any characters as we wish. Here is the code:

# Python code to illustrate split() function
with open("file.text", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)


