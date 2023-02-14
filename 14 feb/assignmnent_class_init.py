class Weapon():
    def __init__(self, bore, no_of_rounds_in_magazine):
        self.bore = bore
        self.no_of_rounds_in_magazine = no_of_rounds_in_magazine
    
    def shoot(self):
        print("Pistol Shoots a",self.bore, "round")

Beretta = Weapon(0.45, 13)
print("Calling Shoot Function using an object")
Beretta.shoot()
print("Bore: ", Beretta.bore)
print("No of rounds in magazine:- ", Beretta.no_of_rounds_in_magazine)
print("Calling Shoot Function using class")
Weapon.shoot(Beretta)
print("##################################################################")

class Face():
    def __init__(self, nose, ears, mouth, eyes):
        self.nose = nose
        self.ears = ears
        self.mouth = mouth
        self.eyes = eyes

    def identification(self):
        print("A human face includes ", self.eyes, "eyes ", self.ears, "ears " ,self.nose, "nose and ", self.mouth, "mouth.")

arsh = Face(1, 2, 1, 2)
arsh.identification()
# print("eyes", arsh.eyes)
# print("Nose",arsh.Nose)
# print("ears",arsh.ears)
# print("Mouth",arsh.mouth)
print("##################################################################")


class Student():
    def __init__(self, name=" ", roll_no="", branch=""):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch

    def study(self):
        print("Student name", self.name," from ",self.branch, "has been studying in the library.")

Arshdeep = Student(name="Arsh", roll_no=1011, branch="CSE")
Arshdeep.study()
# print("Name:-", Arshdeep.name)
# print("Roll No:-", Arshdeep.roll_no)
# print("Branch:- ", Arshdeep.branch)
print("##################################################################")


class Employee():
    def __init__(self, name, department):
        self.name = name
        self.department = department
    def works(self):
        print(self.name, " works as ", self.department)

deep = Employee(name="Arsh", department="Python developer")
deep.works()
print("##################################################################")


class Car():
    wheel = 4
    gear = 6
    
    def drives(self):
        print("A car has ",self.wheel, "wheels and ", self.gear, "gears.")

jeep = Car()
jeep.drives()
print("##################################################################")