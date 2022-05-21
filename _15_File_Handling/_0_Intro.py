'''
UI  --->   PYTHON    ---> Database
          C  S   D

            remote machine directory path
              http://devhost:80/opt/dev/naukri/madhunettem/

File attributes -
==================
filename       'myfile'
fextension     'txt'
fcontent       base64 encoded
size           '60kb'
uploaded by    'madhunettem'
datetime       '2020-03-15'
filepath       'http://devhost:80/opt/dev/naukri/madhunettem/'

txt*, excel*,csv* word  ppt image jpg pdf audio video

file: empty file
      content
          - append more content
          - delete existing content and add from scratch




FILE HANDLING :
==================
Advantages of storing data in file: cronjobs
------------------------------------
 - Data can be stored permanently
 - We can update the data in file whenever required
 - File can be shared to multiple users when required
 - To store huge amount of data, files are very helpful

 Types of files in python:
 -------------------------
 1. Text files   : Stores data in form of characters
 2. Binary files : Stores data in form of bytes

                   Can be used to store text,audio,video,images etc.,

To open a file :  open,  with open
----------------
file_handler = open("filename", "open mode", "buffering")
filehandler.close

with open("file name" as file1)  # it will auto close the file which opened
File openmode   Description :
---------------------------------
w         Writes data into file.            If data exists already, it will be deleted and new data will be written
r         Reads data from file.             File pointer is positioned at beginning of file
a         Appends data into file.           If data already exists it will start appending from last line of file

w+        Writes and reads data of file     Previous data in the file will be deleted
r+        Reads and writes data into file   Previous data in the file will not be deleted
a+        Appends and reads data of file    File pointer will be at end of file
                                            If file does not exists,will create new file and writes data
x   Opens file in exclusive creation mode   If file already exists,file creation fails


To close a file :
-----------------
file_handler.close()


Context Manager in python : Mainly it avoids code duplication
-----------------------------

A context manager usually takes care of setting up some resource,
e.g. opening a connection, and
automatically handles the clean up when we are done with it.
Probably, the most common use case is opening a file.
The code above will open the file and will keep it open until we are out of the
with statement.



with  statement:
https://www.geeksforgeeks.org/context-manager-in-python/
http://book.pythontips.com/en/latest/context_managers.html
https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/

Assignemnt :
Importance of Context Manager in python
How with statement internally works in python
Text file : Create Read Write Append Delete
            C      R    U     U        D
Excel file:
Zip file :


file1 = open(".txt", )
file1.close()


with open(file.txt, w as file2)


w, r, a  w+, r+, a+   x







'''


