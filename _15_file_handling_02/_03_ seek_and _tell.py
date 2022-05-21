'''
seek and tell:

seek():
-------
To move file pointer from one point to another, use seek() method.it makes two arguments

f.seek(offset, fromwhere)

offset - represents how many bytes to move
fromwhere- represents 0, 1, 2   (10, 0)
f.seek(10, 0)
This will move pointer to 11th byte 10+1  from beginning

f.seek(-10, 2)  -10, -9----------------2
This will move the pointer to 9th byte (-10+1) from ending
2 represents ending of file
-10 represents moving back in the file


To know the position of pointer, use tell() method.
n = f.tell()
n - represents the byte position
f - represents file object
'''


fi = open("text.txt", "r")
# the second parameter of the seek method is by default 0
fi.seek(30)
# now, we will print the current position
print("current position: ", fi.tell())

print("pointer will start at next position:", fi.readline())
fi.close()




print()
fi = open("text.txt", "r+")
print("Name of the file: ", fi.name)
print("mode: ",fi.mode )

line_1 = fi.readline()
print("Read Line: %s" % (line_1))

# Again, set the pointer to the beginning
fi.seek(0, 1)
line_2 = fi.readline()
print("Read Line: %s" % (line_2))

# Close opend file
fi.close()




print("__negative offset__")
fi = open("text.txt", "rb")

# the user is setting the reference point to thirtieth position to the left from
# end
fi.seek(-70, 2)

# now print the current position
print(fi.tell())

# now the user will Convert the binary to string
print(fi.readline().decode('utf-8'))

fi.close()




print("_________________")

'''
tell() Function in Python
The tell() function, returns the current position of the file pointer(cursor) in a stream.
'''

f = open("text.txt", "r")
cursor_position = f.tell()
print("Cursor Position is :",cursor_position)
data = f.read(5)
print("After reading 5 data from file")
cursor_position = f.tell()
print("Cursor Position is :",cursor_position)




print("Seek() Function in Python")
'''
As we have seen in the above example that when we open a file, 
cursor is at beginning (0 position). 
Sometimes, it is required that perform the operation (read / write) from the specific position,
 and move this cursor around without making any variable read or write, 
 for this purpose there is a seek() function available to move the cursor 
 to the desired location within a file.

Syntax :
                    
f.seek(offset, [start_from])
                
In the above syntax, offset tells how may number of bytes to move forward and 
start_from is optional, it tells from which place we want to start.

There are three possible values for start_from --

0 :beginning of file
1 :current position of file
2 :end of file
If the argument start_from is not specified, by default it is 0.

Reference point(start_from) at current position / end of file cannot be set 
in text mode except when offset is equal to 0.

EXAMPLE : Let's suppose there is file text.txt which contains the following text.

If you want to earn something, first learn something.
'''
f = open("text.txt", "r")
f.seek(35, 10)
print("Cursor Position :",f.tell())
data = f.read()
print(data)


print("Seek() function with negative value:")

# Seek() function with negative offset value will work, if file is open in binary mode.


f = open("abc.txt", "rb")
f.seek(-10, 2)
print("Cursor Position :",f.tell())
data = f.read().decode('utf-8')
print(data)
