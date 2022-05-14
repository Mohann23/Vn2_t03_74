'''class Student:
    def __init__(self,name,age,roll_no):
        self.name=name
        self.age=age
        self.roll_no=roll_no

class House(Student):
    def __init__(self,name,age,roll_no,door_no,place):
        super().__init__(name, age, roll_no)
        self.door_no=door_no
        self.place=place
    def talk(self):
        print("Hello my name is {} my age is {} my roll no is {}. I live at flat no: {} in {} ".format(self.name,self.age,self.roll_no,self.door_no,self.place))


h=House("Mohan",23,11,203,"Rajahamsa Apartment, Anantapur")
h.talk()
'''

# prime number


'''
#B/W range
lower = 100
upper = 200

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):

   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

'''
'''

l1=[1,2,3,4]
l2=[4,3,2,1]
l3=[6,8,2,1]
l=[]
for each in l1:
    if each in l2:
        if each in l3:
            l.append(each)

print(l)
'''
'''

s = "Mohan"
m = s[-2:]
print(m)
'''
'''
l=[]
for i in range(100,200,2):
   l.append(i)

print(l[::-1])
'''
'''
l=[even for even in range(1,100) if even%2==0]
print(l,end=",")
'''

'''

l = "Mohan"
print(len(l))
'''
















