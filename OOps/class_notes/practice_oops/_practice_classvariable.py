# without class variables
# instance variable - it has own /personal/ not sharable data eg. name, eid
# class variable - it is sharable/ global data eg. college

class Student:
    def __init__(self, name, eid, college):
        self.name = name
        self.eid = eid
        self.college = college

    def get_studentdata(self):
        print("student information:", self.name, self.eid, self.college)


s1 = Student("Manikanta.D", "124g1a0121", "SRIT")
s1.get_studentdata()

# with class variables

class Student:

    college = "SRIT"

    def __init__(self, name, sid):
        self.name = name
        self.sid = sid

    def get_studentdata(self):
        print("student details:", self.name, self.sid, Student.college)


mustafa = Student("Mustafa", "124g1a0124")
mustafa.get_studentdata()

lizith = Student("lizith", "124g1a0154")
lizith.get_studentdata()



