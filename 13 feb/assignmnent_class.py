class Weapon():
    bore = 0.45
    no_of_rounds_in_magazine = 13
    def shoot(self):
        print("Pistol Shoots a round ")

Beretta = Weapon()
print("Calling Shoot Function using an object")
Beretta.shoot()
print("Bore: ", Beretta.bore)
print("No of rounds in magazine:- ", Beretta.no_of_rounds_in_magazine)
print("Calling Shoot Function using class")
Weapon.shoot(Beretta)
print("##################################################################")

class Face():
    Nose = 1
    ears = 2
    mouth = 1
    eyes = 2
    def identification(self):
        print("Our Face is used as an identity ")

arsh = Face()
arsh.identification()
print("eyes", arsh.eyes)
print("Nose",arsh.Nose)
print("ears",arsh.ears)
print("Mouth",arsh.mouth)
print("##################################################################")


class Student():
    name = "Arsh"
    roll_no = 1011
    branch = "CSE"

    def study(self):
        print("Students are studying in their classes ")

Arshdeep = Student()
Arshdeep.study()
print("Name:-", Arshdeep.name)
print("Roll No:-", Arshdeep.roll_no)
print("Branch:- ", Arshdeep.branch)
print("##################################################################")


class Employee():
    name = "Arsh"
    department = "Python-developer"
    def works(self):
        print(self.name, " works in ", self.department)

print("Employee class ")
deep = Employee()
deep.works()
print("##################################################################")


class Car():
    wheel = 4
    gear = 6
    
    def drives(self):
        print("Car is driven by driver ")

print("Car class ")
jeep = Car()
jeep.drives()
print("##################################################################")