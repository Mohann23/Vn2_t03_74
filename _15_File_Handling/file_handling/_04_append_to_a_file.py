'''
Python append to a file
==========================

Basics of file handling
Access modes
While reading or writing to a file, access mode governs the type of operations possible
in the opened file. It refers to how the file will be used once it’s opened.
These modes also define the location of the File Handle in the file.
File handle is like a cursor, which defines from where the data has to be read
or written in the file.

In order to append a new line to the existing file, open the file in append mode, by using either 'a' or 'a+' as the access mode. The definition of these access modes are as follows:

Append Only (‘a’): Open the file for writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.
Append and Read (‘a+’): Open the file for reading and writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.
When the file is opened in append mode, the handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data. Let’s see the below example to clarify the difference between write mode and append mode.

Example:


# Python program to illustrate
# Append vs write mode
======================
'''
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London"]
file1.writelines(L)
file1.close()

# Append-adds at last
file1 = open("myfile.txt", "a")  # append mode
file1.write("Today \n")
file1.close()

file1 = open("myfile.txt", "r")
print("Output of Readlines after appending")
print(file1.read())
print()
file1.close()

# Write-Overwrites
file1 = open("myfile.txt", "w")  # write mode
file1.write("Tomorrow \n")
file1.close()

file1 = open("myfile.txt", "r")
print("Output of Readlines after writing")
print(file1.read())
print()
file1.close()

'''
Output:

Output of Readlines after appending
This is Delhi
This is Paris
This is LondonToday


Output of Readlines after writing
Tomorrow



Append data from new line: use \n


With statement
with statement in Python is used in exception handling to make the code cleaner 
and much more readable. 
It simplifies the management of common resources like file streams. 
Unlike the above implementations, 
there is no need to call file.close() when using with statement. 
The with statement itself ensures proper acquisition and release of resources.

Example:

'''
# Program to show various ways to
# append data to a file using
# with statement

L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# Writing to file
with open("myfile.txt", "w") as file1:
    # Writing data to a file
    file1.write("Hello \n")
    file1.writelines(L)

# Appending to file
with open("myfile.txt", 'a') as file1:
    file1.write("Today")


# Reading from file
with open("myfile.txt", "r+") as file1:
    # Reading form a file
    print(file1.read())
'''
Output:

Hello
This is Delhi
This is Paris
This is London
Today

'''
