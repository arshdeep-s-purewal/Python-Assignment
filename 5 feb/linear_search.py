def linear_search(lst_numbers, inp):
    for i in range(len(lst_numbers)):
        if lst_numbers[i] == inp:
            print("Element Found at index", i)
            break

numbers = [12, 45, 65, 75, 24]
ip = int(input("Enter the number you want to search:- \n"))
linear_search(numbers, ip)