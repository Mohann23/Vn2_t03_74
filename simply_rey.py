class Mohan:
    def __init__(self, emp_id, name, sal):
        self.emp_id = emp_id
        self.name = name
        self.sal = sal

    def details(self):
        print("Hello People, My name is {} and My employee ID is {} and I get a salary of {}".format(self.name,
                                                                                                     self.emp_id,
                                                                                                     self.sal))

    @classmethod
    def class_method(cls, car, model):
        cls.car = car
        cls.model = model
        print("Hello car details: ", cls.car, cls.model)

    @staticmethod
    def static_method(a, b):
        print("Bye guys ", a, b)


m = Mohan("Mohan", 143, 10000)
m.details()
m.class_method("kia", 2000)
m.static_method(10, 20)
