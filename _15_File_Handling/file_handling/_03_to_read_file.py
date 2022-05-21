'''
To read from a file in Python
===================================


Read Only (‘r’) : Open text file for reading. The handle is positioned at the beginning of the file. If the file does not exists, raises I/O error. This is also the default mode in which file is opened.
Read and Write (‘r+’) : Open the file for reading and writing. The handle is positioned at the beginning of the file. Raises I/O error if the file does not exists.

'''
# Open function to open the file "MyFile1.txt"
# (same directory) in read mode and
# file1 = open("MyFile.txt", "r")

# store its reference in the variable file1
# and "MyFile2.txt" in D:\Text in file2
file2 = open(r"D:\Text\MyFile2.txt", "r+")
# Here, file1 is created as object for MyFile1 and file2 as object for MyFile2.

# Closing a file
# close() function closes the file and frees the memory space acquired by that file.
# It is used at the time when the file is no longer needed or if it is to be opened in a different file mode.



# Opening and Closing a file "MyFile.txt"
# for object name file1.
file1 = open("MyFile.txt", "r")
file1.close()

'''
Reading from a file
There are three ways to read data from a text file.

read() : Returns the read bytes in form of a string. Reads n bytes, if no n specified, reads the entire file.
File_object.read([n])
readline() : Reads a line of the file and returns in form of a string.For specified n, reads at most n bytes. 
However, does not reads more than one line, even if n exceeds the length of the line.
File_object.readline([n])
readlines() : Reads all the lines and return them as each line a string element in a list.
File_object.readlines()
Note: ‘\n’ is treated as a special character of two bytes.
'''



# Program to show various ways to
# read data from a file.

# Creating a file
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# Writing data to a file
file1.write("Hello \n")
file1.writelines(L)
file1.close()  # to change file access modes

file1 = open("myfile.txt", "r+")

print("Output of Read function is ")
file1.write("welcome")
print(file1.read())

print()


# with open open statement

# Program to show various ways to
# read data from a file.

L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# Creating a file
with open("myfile.txt", "w") as file1:
    # Writing data to a file
    file1.write("Hello \n")
    file1.writelines(L)
    file1.close()  # to change file access modes

with open("myfile.txt", "r+") as file1:
    # Reading form a file
    print(file1.read())
