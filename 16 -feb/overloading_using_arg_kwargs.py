#Function overloading using *args
def sum(*argi):
    s = 0
    for i in argi:
        s = s+i
    return s

# a = sum(3,5)
# b = sum(1,2,3,4,5,6,7,8,9)
# print(a)
# print(b)

class Calculations:
    def add(self, *argum):
        sum = 0
        for i in argum:
            sum = sum +i
        return sum

    def multiply(self, *arg):
        mul = 1
        for i in arg:
            mul = mul*i
        return mul
    
calc = Calculations()
c = calc.add(5,6,65,45)
print("Addition:- ",c)

# kargs = {"arg_1":5, "arg_2":9}
m = calc.multiply(5,9)
print("Multiplication:- ",m)