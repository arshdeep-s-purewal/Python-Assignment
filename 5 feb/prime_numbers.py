def prime_number(n):
    if n == 1:
        print("1 is not a prime number\n")
    elif(n>1):
        for i in range(2,n):
            if n%i == 0:
                    print(n, " is not a prime number")
                    break
        else:
            print(n, " is a prime number")

    

ip = int(input("Enter any number:- \n"))
prime_number(ip)


