n = int(input("Enter any number:- \n"))
x = 0
print(x)
y = 1
print(y)
for i in range(n-2):
    x = y
    y = x + y
    print(y)