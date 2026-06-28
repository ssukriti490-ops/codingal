class Student:
    manufecturer = "Indian Scintists"
    print("Hi I am a Robot. I was made by",manufecturer)
ob = Student()
class Student:
    manufecture = 2025
    name = "Robot 2.O"
    def introduction(self):
        print("Hi I am a new latest Robot.")
    def details(self):
        print("My name is ", self.name)
        print("I am made in the year of ", self.manufecture)
ob = Student()
ob.introduction()
ob.details()
class Parrot:
    species = "bird"
    def __init__(self,name, age):
        self.name = name
        self.age = age
blu = Parrot("Mariano", 16)
woo = Parrot("cherry", 12)
print("Mariano is a {}".format(blu.species))
print("Cherry is also a {}".format(woo.species))
print(blu.name,"is",blu.age,"year old")
print(woo.name,"is",woo.age,"year old")