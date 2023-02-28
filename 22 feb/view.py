from model import User, Blog

def inputdata_user():
    first_Name = input("Enter your First Name \n")
    last_Name = input("Enter your Last Name \n")
    emaiL = input("Enter your email id \n")
    phone_Number = input("Enter your phone number")
    user = User(first_Name,last_Name,emaiL,phone_Number)
    user.set_user()

def input_data_blog():
    title = input("Enter Blog's title \n")
    body = input("Enter Body of the Blog \n")
    date_of_release = input("Enter date of release \n")
    blog = Blog(title, body, date_of_release)
    blog.set_blog()

def showData_user(list):
    for item in list:
        print(item)


def showAllBlog(list):
#    print('We have %i blogs' % len(list))
   for i in list:
      print(i)