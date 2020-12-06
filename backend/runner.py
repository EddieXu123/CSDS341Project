import mysql.connector
#edit this according to your local configuration
#python -m pip install mysql-connector-python 
#^ make sure this package is installed using terminal so that you can run everything else

#create connection to database
#modify this according to your setup
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="orhanisbae",
  database = "test"
)


mycursor = mydb.cursor()


#sample SQL query format
#sql = "INSERT INTO Login_Info (Email_address, Password) VALUES (%s, %s)"
#val = ("pthik2000@gmail.com", "1234")
#mycursor.execute(sql, val)

#mydb.commit()

#print(mycursor.rowcount, "record inserted.")

#list of methods for register
def get_first_name():
    return input('Please enter your first name: ')

def get_last_name():
    return input('Please enter your last name: ')

def get_gpa():
    return input('Please Enter your GPA on a 4.0 scale: ')

def create_student():
    first_name = get_first_name()
    last_name = get_last_name()

def get_registration_email():
    email = input('Please enter your email: ')
    while (check_email(email)):
        print("This email already exists in the Database")
        email = input('Please enter your email: ') 
    return email

def check_email(email):
    cursor = mydb.cursor()
    em = (email, )
    cursor.execute("SELECT * FROM Login_Info WHERE Email_address = %s", em)
    myresult = cursor.fetchall()
    if (len(myresult) > 0):
        return True
    else:
        return False

def get_DOB():
    return input("Please enter your Date of Birth (MM/DD/YYYY): ")

def get_gender():
    return input("Please enter your gender: ")

def get_phone_num():
    return input("Please enter your phone number (xxx-xxx-xxxx): ")

def get_major():
    return input('Please enter is your major: ')

def get_year():
    return input('Please enter is your Academic Year: ')

#def enter_class():

def get_password():
    return input ('Please enter in a password: ') #Don't need to check because doesn't need to match when registering

def get_class_num():
    return input('Please enter your class Number: ')

def get_class_dept():
    return input('Please enter the department of your class: ')

def get_class_sem():
    return input('Please enter the semester you are taking this class [Fall, Winter, Spring, Summer]: ')

def matching(classNum, classDept, classSem):
    em = (classNum, classDept, classSem)
    mycursor.execute("SELECT User_ID FROM Takes WHERE ClassNum = %s and ClassDept = %s and ClassSem = %s", em)
    myresult = mycursor.fetchall()

    for x in myresult:
        id = x[0]
        get_main_info(id)

def get_main_info(User_ID):
    em = (User_ID,)
    mycursor.execute("SELECT First_Name, Last_Name, gender, PhoneNum FROM Students WHERE User_ID = %s", em)
    myresult = mycursor.fetchall()
    fname = myresult[0][0]
    lname = myresult[0][1]
    gender =  myresult[0][2]
    phoneNum =  myresult[0][3]

    em = (User_ID,)
    mycursor.execute("SELECT interests FROM Interests WHERE User_ID = %s", em)
    myresult = mycursor.fetchall()
    interests = myresult[0][0]

    em = (User_ID,)
    mycursor.execute("SELECT major, AcademicYear, GPA FROM Academics WHERE User_ID = %s", em)
    myresult = mycursor.fetchall()
    major = myresult[0][0]
    yr = myresult[0][1]
    gpa = myresult[0][2]

    #print everything out
    print("--------------------------------------")
    print("name:" + fname + " " + lname)

def get_user_id(email):
    em = (email, )
    mycursor.execute("SELECT User_ID FROM Login_Info WHERE Email_address = %s", em)
    myresult = mycursor.fetchall()
    return myresult[0][0]

# Only add if the username (email address) doesn't exist
def register():
    email = get_registration_email()
    first = get_first_name()
    last = get_last_name()
    password = get_password()
    sql = "INSERT INTO Login_Info (Email_address, Password) VALUES (%s, %s)"
    val = (str(email), str(password))
    mycursor.execute(sql, val)
    mydb.commit()
    user_id = get_user_id(email)
    print("Success")
    
def get_login_info():
    email = input("Please enter in the email you registered with: ")
    cursor = mydb.cursor()
    em = (email, )
    cursor.execute("SELECT Password FROM Login_Info WHERE Email_address = %s", em)
    myresult = cursor.fetchall()
    while(len(myresult) == 0):
        print("Incorrect Email. Try Again...")
        email = input("Please enter in the email you registered with: ")
        cursor = mydb.cursor()
        em = (email, )
        cursor.execute("SELECT Password FROM Login_Info WHERE Email_address = %s", em)
        myresult = cursor.fetchall()

    password = input("Please enter your password: ")
    while (password != myresult[0][0]):
        print("Incorrect Password. Try again")
        password = input("Please enter your password: ")
    print("Logging In...")
    return [email, password]

def enter_info(user_id):
    if (not has_info(user_id)):
        class_sem = str(get_class_sem())
        class_num = str(get_class_num())
        class_dept = str(get_class_dept())
        add_class_info = """INSERT INTO Takes (User_id, ClassNum, ClassDept, ClassSem) VALUES (%s, %s, %s, %s)"""
        user_class_info = (user_id, class_num, class_dept, class_sem)
        mycursor.execute(add_class_info, user_class_info)

        major = str(get_major())
        year = int(get_year())
        gpa = get_gpa()
        add_academic_info = """INSERT INTO Academics 
              (User_ID, major, AcademicYear, GPA) 
              VALUES (%s, %s, %s, %s)"""
        user_info = (user_id, major, year, gpa)
        mycursor.execute(add_academic_info, user_info)
        mydb.commit()
        mydb.close()
        print("success")


# WRite a query to get the sem, num, dept of a user_id
def get_sem_num_dept(user_id):
    print("Hello")
    u_id = (user_id, )
    print("Works")
    print("TestAgain")
    print(u_id)
    print(type(u_id))
    print(u_id[0])
    print(type(u_id[0]))
    print("SELECT ClassNum, ClassDept, ClassSem FROM Takes WHERE User_ID = {u_id[0]}")
    #query = "SELECT ClassNum, ClassDept, ClassSem FROM Takes WHERE User_ID = %s"
    #info = str(u_id[0])
    #mycursor.execute(query, info)
    mycursor.execute("SELECT ClassNum, ClassDept, ClassSem FROM Takes WHERE User_ID = {u_id[0]}")
    myresult = mycursor.fetchall()
    print("THERE")
    print(myresult[0][1])
    return myresult[0][0], myresult[0][1], myresult[0][2]

def has_info(user_id):
    cursor = mydb.cursor()
    u_id = (user_id, )
    cursor.execute("SELECT User_ID FROM Academics WHERE User_ID = %s", u_id)
    myresult = cursor.fetchall()
    return len(myresult) > 0

def log_in():
    email_and_password = get_login_info() 
    cursor = mydb.cursor()
    em = (email_and_password[0], )
    cursor.execute("SELECT User_ID FROM Login_Info WHERE Email_address = %s", em)
    user_id = cursor.fetchall()
    print(user_id[0][0])
    u_id = user_id[0][0]
    enter_info(u_id)
    print("WORK TO HERE")
    sem, num, dept = get_sem_num_dept(u_id)
    #matching(num, dept, sem)


def get_matched():
    print("Welcome back! Here are the users who you can match with: ")



def run():
    #application starts here
    key = 1
    print("Welcome to Gethub, the real antisocial social club")
    while(key >= 1):
        print("press 1 to login")
        print("press 2 to register")
        print("press 0 to quit")
        val = input()
        if val != "1" and val != "2" and val != "0":
            print("Enter a valid input please!")
            continue
        elif(int(val) == 0):
            key = int(val)
        else:
            key = int(val)
            if(key == 1):
                log_in()
                get_matched()

                print("Thanks for checking out GetHub! Come back soon!")
                key = 0
            else:
                register()

run()