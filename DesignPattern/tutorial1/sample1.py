class Person(object):
    def __init__(self, name, age):      # constructor
        self.name = name
        self.age  = age

    def get_person(self,):              # member function
        return "<Person (%s, %s) >" % (self.name, self.age)


p = Person("John", 32)
print("Type of Object :" , type(p), "Memory Address:", id(p))

class Adder:
    def __init__(self):
        self.sum = 0

    def add(self, value):
        self.sum += value

acc = Adder()
for i in range(99):
    acc.add(i)

print(acc.sum)



