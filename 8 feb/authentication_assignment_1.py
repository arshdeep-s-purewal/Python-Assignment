import datetime
from datetime import date
import re

registration_data = []

def email_validation(inp_email):
    reg_exp = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(reg_exp,inp_email):
        print("Valid email ")
    else:
        print("Invalid Email please enter a valid email address \n")

def password_validation(inp_pswd):
    pswd_lower = 0
    pswd_upper = 0
    pswd_digit = 0
    pswd_special_char = 0
    if len(inp_pswd) >= 8:
        for i in inp_pswd:
            if i.islower():
                pswd_lower += 1
            
            if i.isupper():
                pswd_upper += 1 
            
            if i.isdigit():
                pswd_digit += 1
            
            if (i == '@' or i == '$' or i == "_"):
                pswd_special_char += 1
    else:
        print("At least 8 digit passwprd is required!")

    if pswd_lower >=1 and pswd_upper >= 1 and pswd_digit >= 1 and pswd_special_char >=1 and pswd_lower+pswd_upper+pswd_digit+pswd_special_char == len(inp_pswd):
        print("valid Password")
    else:
        print("Invalid Password")
    

def login_credentials():
    inp_email_login = input("Enter email id:- \n")
    inp_password_login = input("Enter password:- \n")
    for i in registration_data:
        # breakpoint()
        if i['email_id'] == inp_email_login:
            if i['password'] == inp_password_login:
                print("Login Successful \n")
                print("1. Update Your profile \n")
                print("2. Delete your profile \n")
                option_up_del = int(input("Choose option \n"))
                if option_up_del == 1:
                    print("1. Update First name \n")
                    print("2. Update Second name \n")
                    print("3. Update DOB \n")
                    print("4. Update password \n")
                    option_update = int(input("Choose Option \n"))
                    if option_update == 1:
                        updated_first_name = input("Enter updated name:- \n")
                        i['first_name'] = updated_first_name
                        # print(i['first_name'])
                    
                    elif option_update == 2:
                        updated_last_name = input("Enter updated last name: \n")
                        i['last_name'] = updated_last_name
                    
                    elif option_update == 3:
                        updated_birth_date = input("Enter your date of birth: \n")
                        birthday = datetime.datetime.strptime(updated_birth_date,"%d/%m/%Y").date()
                        today = date.today()
                        age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
                        i['age'] = age
                        print(i)

                    elif option_update == 4:
                        updated_password = input("Enter your updated password \n")
                        password_validation(updated_password)
                        i['password'] = updated_password

                if option_up_del == 2:
                    registration_data.remove(i)
                    print(registration_data)

            else:
                print("Invalid Password")
        else:
            print("Email not registered \n")
            print("1. Try again \n")
            print("2. Register Yourself \n")
            print("3. Exit \n")
            inp_op = int(input("Choose your option:- \n"))
            if inp_op == 1:
                login_credentials()
            elif inp_op == 2:
                register_credentials()
            else:
                exit()

def register_credentials():
    temp = {
        "first_name": "",
        "last_name": "",
        "age": "",
        "email_id": "",
        "password": "",
    }
    inp_first_name = input("Enter First Name: \n")
    inp_last_name = input("Enter Second Name \n")
    inp_birth_date = input("Enter your birth date(dd/mm/yy)")
    birthday = datetime.datetime.strptime(inp_birth_date,"%d/%m/%Y").date()
    today = date.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day)) 
    # print("Your birthday is on:- ", birthday.strftime('%d/%m/%Y'))
    inp_email_id = input("Enter your email id:- \n")
    email_validation(inp_email_id)
    inp_password = input("Enter password:- \n")
    password_validation(inp_password)
    temp.update({"first_name":inp_first_name, "last_name":inp_last_name, "age":inp_birth_date, "email_id":inp_email_id, "password":inp_password})
    registration_data.append(temp)
    print(registration_data)

while True:
    print("1. Login \n")
    print("2. Register \n")
    print("3. Exit \n")
    num = int(input("Choose option:- \n"))
    if num == 1:
        login_credentials()

    if num == 2:
        register_credentials()

    if num == 3:
        exit()