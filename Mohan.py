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





