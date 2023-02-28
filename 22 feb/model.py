import random
import csv
import os
import uuid

def generate_uuid():
        return uuid.uuid4()

# def generate_pk(func):
#     def wrapper(x):
#         if os.path.isfile('user.csv'):
#             var = open('user.csv', 'r', newline='')
#             w = csv.DictReader(var)
#             for rows in w:
#                 pri_key = rows['Primary Key']
#             new_pri=  int(pri_key)+1
#             return new_pri
#         return func(x)     
#     return wrapper  

def generate_pk():
        if os.path.isfile('user.csv'):
            var = open('user.csv', 'r', newline='')
            w = csv.DictReader(var)
            for rows in w:
                pri_key = rows['Primary Key']
            new_pri=  int(pri_key)+1
            return new_pri
        else:
            print('File created')

class User(object):
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.uuid = generate_uuid()
        self.primary_key = generate_pk()
    
    # @generate_pk
    def set_user(self):
        fieldname = ['Primary Key','First Name', "Last Name", 'Email', 'Phone no.', 'UUId']                               
        data = [{
            'Primary Key':self.primary_key,
            'First Name':self.first_name,
            "Last Name":self.last_name,
            'Email':self.email, 
            'Phone no.':self.phone_number, 
            'UUId':self.uuid
        }]
        if os.path.isfile('user.csv'):
            with open('user.csv', 'a', newline='') as my_file:
                w = csv.DictWriter(my_file, fieldnames = fieldname)
                for row in data:
                    w.writerow(row)
        else:
            # print('hello world')
            with open('user.csv', 'w', newline='') as my_file:
                w = csv.DictWriter(my_file, fieldnames = fieldname)
                w.writeheader()
                data1 = [{'Primary Key':1,'First Name':self.first_name,'Last Name':self.last_name,'Email':self.email,'Phone no.':self.phone_number,'UUId':self.uuid}]
                for row in data1:
                    w.writerow(row)

    @classmethod
    def getAll(cls):
        database = open('user.csv', 'r')
        result = []
        reader = csv.DictReader(database)
        field = reader.fieldnames
        for row in reader:
            result.extend([{field[i]:row[field[i]] for i in range(len(field))}])
        return result     

def read_pri_user():
    if os.path.isfile('user.csv'):
            var = open('user.csv', 'r', newline='')
            w = csv.DictReader(var)
            for rows in w:
                pri_key = rows['Primary Key']
            return pri_key

class Blog(object):
    def __init__(self, title, body, date_of_release):
        self.pri_key = read_pri_user()
        self.title = title
        self.body = body
        self.date_of_release = date_of_release


    def set_blog(self):
        fieldnames = ['Primary Key','Title', 'Body', 'Date_of_release']
        data = {
             'Primary Key':self.pri_key,
             'Title':self.title, 
             'Body':self.body, 
             'Date_of_release':self.date_of_release
            }
                
        if os.path.isfile('blog.csv'):
            with open('blog.csv', 'a', newline='') as my_file:
                w = csv.DictWriter(my_file, fieldnames= fieldnames)
                w.writerow(data)
        else:
            with open('blog.csv', 'w', newline='') as my_file:
                    w = csv.DictWriter(my_file, fieldnames = fieldnames)
                    w.writeheader()
                    w.writerow(data)

    @classmethod
    def getAllBlog(cls):
        values = open('blog.csv', 'r')
        result = []
        read = csv.DictReader(values)
        field = read.fieldnames
        for row in read:
            result.extend([{field[i]:row[field[i]] for i in range(len(field))}])
        return result

        
























        # data = list()
        # entry_to_be_deleted = input("Enter user name you want to delete \n")
        # with open('user.csv', 'r') as read_file:
        #     reader = csv.reader(read_file)
        #     for row in reader:
        #         data.append(row)
        #         for name in row:
        #             if name == entry_to_be_deleted:
        #                 data.remove(row)
        
        # with open('user.csv', 'w') as 


        # file.close()
        
# first_Name = input("Enter your First Name \n")
# last_Name = input("Enter your Last Name \n")
# emaiL = input("Enter your email id \n")
# phone_Number = input("Enter your phone number")
# user = User(first_Name, last_Name, emaiL, phone_Number)
# user.set_user()
