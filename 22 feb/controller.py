from model import User, Blog
import view


def user_start():
    n = input("Do you want to enter data in the file:- \n")
    if n == 'y':
        view.inputdata_user()
    else:
        print("byeee byeeeee!")


def show_user_data():
    user_data = User.getAll()
    # print(user_data)
    return view.showData_user(user_data)


def blog_start():
    n = input("Do you want to create a new blog \n")
    if n == 'y':
        view.input_data_blog()
    else:
        print("byeee byeeeee!")

def show_blog_data():
    blog_data = Blog.getAllBlog()
    # print(blog_data)
    return view.showAllBlog(blog_data)

if __name__ == "__main__":
    user_start()
    blog_start()
    # show_user_data()
    # show_blog_data()
