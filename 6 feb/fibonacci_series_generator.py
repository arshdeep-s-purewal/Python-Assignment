def fibonacci_series(n):
    x = 0
    print(x)
    y = 1
    print(y)
    for i in range(n-2):
        temp = y
        y = x + y
        # print(y)
        x = temp
        yield y

def square():
    for i in fibonacci_series(10):
        print (i**2)

print(square())
# num = int(input("Enter any number:- "))
# fibonacci_series(num)