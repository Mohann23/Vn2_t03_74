# PROGRAM TO READ AND WRITE  DATA FROM A FILE

out_data = open("names.txt", "w")
out_data.write("Welcome to the \nworld of Python")
print("---After writing to file DATA : ", out_data)
out_data.close()

obj = open("names.txt", "r")
in_data = obj.read()
print(type(in_data))
print("---Reading from file--------  : ", in_data)
obj.close()
