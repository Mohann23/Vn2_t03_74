try:
    file_obj = open("mani.txt", 'w')  # 1. Create the file # C:/Users/madhu/Destop/
    print("File content ", file_obj)
    print("File type :", type(file_obj))
    data = input("Enter text : ")
    file_obj.write(data)  # ==> TextIOWrapper.write(file_obj, data)   # 2 Perform ops on file
except FileNotFoundError as fnf:
    print("File not found at specified path")
    print(fnf)
finally:
    # condition to check whether object my_file exists or not
    file_obj.close()  # 3 Close the file

print("---Completed---")