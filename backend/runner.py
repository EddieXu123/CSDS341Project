from random import *
from Student import student

database = []

#def __init__(self, name, major, gpa):

def get_first_name():
    return input('Please enter your first name')

def get_last_name():
    return input('Please enter your last name')

def get_user_ID(name):
    return str(name) + "_" + str(randint(0, 1000))

def get_gpa():
    return input('Please Enter your GPA on a 4.0 scale: ')


def create_student():
    first_name = get_first_name()
    last_name = get_last_name()
    user_id = get_user_ID()
    gpa = get_gpa()
    student = Student(first_name, last_name, user_id, )



student = Student(, "XU", 35, "Hello", 3, 201, "English", 36, 36, 2)
print(student)

print(create_student())
print


