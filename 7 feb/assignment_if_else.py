# data = [
#     {
#         "roll_no":1,
#         'name':'Arsh',
#         'subjects': ["Punjabi", "English", "Hindi"],
#         'class':'Sixteen' 
#     },
#         {
#         "roll_no":2,
#         'name':'Punar',
#         'subjects': ["Punjabi", "English", "Hindi"],
#         'class':'Sixteen' 
#     },
#         {
#         "roll_no":3,
#         'name':'Bani',
#         'subjects': ["Punjabi", "English", "Hindi"],
#         'class':'Fifteen' 
#     }
# ]

data = []
no_of_entries = int(input("How much entries you want to insert ?"))
for i in range(no_of_entries):
    temp = {
            "roll_no": 0,
            'name':'',
            'subjects': [],
            'class':'',
            }

    inp_roll_no = int(input("Enter roll number:- \n"))
    inp_name = input("Enter name:- \n")
    inp_class = input("Enter class:- \n")
    for i in range(3):
        inp_subject = input("Enter subject name:- \n")
        temp["subjects"].append(inp_subject)
        temp.update({"roll_no":inp_roll_no, 'name':inp_name, 'class':inp_class})
    data.append(temp)
    print(data)

def list_of_students(inp):
        name_lst = []
        for i in data:
            name_lst.append(i['name'])
        return name_lst

def search_student(inp):
    inp_search = input("Enter name:- \n")
    for i in data:
        if i['name'] == inp_search:
            # print("Element found at index:- ", i)
            return i
    # else:
    #     print("Element not found")

def update_student(inp):
    inp_search = input("Enter name:- \n")
    for i in data:
        if i['name'] == inp_search:
            print("Element found at index:- \n", i)
            print("What you want to update:- \n")
            print("1. Update Name:- \n")
            print("2. Update Subjects \n")
            print("3. Update Class:- \n")
            print("4. Exit() \n")
            a = int(input("Choose option:- \n"))
            if a == 1:
                inp_new_name = input("Enter updated name \n")
                i.update({'name':inp_new_name})
                print("Updated name is: ",i['name'])
                break

            elif a == 2:
                print(i['subjects'])
                index_var = int(input(("Which subject you want to update(Enter index ) \n")))
                updated_subject = input("Enter Updated Subject name \n")
                i['subjects'][index_var] = updated_subject
                print(i['subjects'])
                break
            
            elif a == 3:
                inp_updated_class = input("Enter Updated class name \n")
                i.update({'class':inp_updated_class})
                print(i['class'])
                break
            
            else:
                break

def delete_student():
    inp_search = input("Enter name:- \n")
    for i in data:
        if i['name'] == inp_search:
            print("Element found at index:- ", i)
            inp_del = input("Are you sure you want to delete it y/n? \n")
            if inp_del == 'y':
                del i
                print("Record Deleted \n")
                print(data)
                break
            else:
                pass
    # else:
    #     print("Element not found")


def add_new_student():
    temp = {
            "roll_no": 0,
            'name':'',
            'subjects': [],
            'class':'',
            }

    inp_roll_no = int(input("Enter roll number:- \n"))
    inp_name = input("Enter name:- \n")
    inp_class = input("Enter class:- \n")
    for i in range(3):
        inp_subject = input("Enter subject name:- \n")
        temp["subjects"].append(inp_subject)
    temp.update({"roll_no":inp_roll_no, 'name':inp_name, 'class':inp_class})
    data.append(temp)
    print(data)            







while True:
    print("1. List of Students \n ")
    print("2. Search Students \n ")
    print("3. Update Students \n ")
    print("4. Delete Students \n ")
    print("5. Add Students \n ")
    print("6. Exit  \n ")

    num = int(input("Choose Option:- \n"))

    if num == 1:
        res = list_of_students(num)
        print(res)

    elif num == 2:
        res = search_student(num)
        print(res)

    elif num == 3:
        update_student(num)

    elif num == 4:
        delete_student()

    elif num == 5:
        add_new_student()
        
    elif num == 6:
        exit()