def _factorial(ip):
    fact = 1
    if ip < 0:
        print("Factorial does not exist \n")
    elif(ip == 0):
        print("Factorial is 1 \n")
    else:
        for i in range(1, ip+1):
            fact = fact*i
        return fact

ip = int(input("Enter any number:- \n"))
f = _factorial(ip)
print("Factorial of number is:- ", f)