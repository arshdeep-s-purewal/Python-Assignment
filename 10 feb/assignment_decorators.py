words_name = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven',8:'eight',9:'nine', 10:'ten',
            11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen',17:'seventeen',18:'eighteen', 19:'ninteen',
            20:'twenty', 30:'thirty', 40:'fourty', 50:'fifty', 60:'sixty',70:'seventy',80:'eighty',90:'ninty', 100:'hundred', 1000:'thousand'
           }
amount = int(input('Enter the amount [1-100]: '))
def format_amount(amount):
    """
    This function is used to format the amount
    ex :25
    Rs: 25.00
    :param amount
    :return
    """
    return f"{amount}.00"
def convert_to_words(func,amt):
        for_amount = func(amt)  # other function with argument
        for_amount = float(for_amount)
        # print("for amount",for_amount)
        if for_amount in words_name:
            result = words_name.get(for_amount)
        else:
            rem = for_amount%10
            last_digit = words_name.get(rem)
            first_digit = for_amount //10
            first_ten = first_digit * 10
            digit = words_name.get(first_ten)
            result = digit+" "+ last_digit
        return result
div = convert_to_words(format_amount, amount)
print(div)