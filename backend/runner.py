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



def get_user_id(email):
    cursor = mydb.cursor()
    em = (email, )
    cursor.execute("SELECT User_ID FROM Login_Info WHERE Email_address = %s", em)
    myresult = cursor.fetchall()
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
        major = str(get_major())
        year = int(get_year())
        gpa = get_gpa()
        add_info = """INSERT INTO Academics 
              (User_ID, major, AcademicYear, GPA) 
              VALUES (%s, %s, %s, %s)"""
        user_info = (user_id, major, year, gpa)
        mycursor.execute(add_info, user_info)
        mydb.commit()
        mydb.close()
        print("success")

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

#application starts here
key = 1
print("Welcome to Gethub, the real antisocial social club")
while( key >= 1):
    print("press 1 to login")
    print("press 2 to register")
    print("press 0 to quit")
    val = input()
    if(int(val) > 2 or int(val) < 0):
        print("invalid value, try again")
    elif(int(val) == 0):
        key = int(val)
    else:
        key = int(val)
        if(key == 1):
            log_in()
        else:
            register()


    













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
        major = str(get_major())
        year = int(get_year())
        gpa = get_gpa()
        add_info = """INSERT INTO Academics 
              (User_ID, major, AcademicYear, GPA) 
              VALUES (%s, %s, %s, %s)"""
        user_info = (user_id, major, year, gpa)
        mycursor.execute(add_info, user_info)
        mydb.commit()
        mydb.close()
        print("success")

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
    enter_info(u_id)def get_login_info():
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
        major = str(get_major())
        year = int(get_year())
        gpa = get_gpa()
        add_info = """INSERT INTO Academics 
              (User_ID, major, AcademicYear, GPA) 
              VALUES (%s, %s, %s, %s)"""
        user_info = (user_id, major, year, gpa)
        mycursor.execute(add_info, user_info)
        mydb.commit()
        mydb.close()
        print("success")

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
    enter_info(u_id)def get_login_info():
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
        major = str(get_major())
        year = int(get_year())
        gpa = get_gpa()
        add_info = """INSERT INTO Academics 
              (User_ID, major, AcademicYear, GPA) 
              VALUES (%s, %s, %s, %s)"""
        user_info = (user_id, major, year, gpa)
        mycursor.execute(add_info, user_info)
        mydb.commit()
        mydb.close()
        print("success")

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
    enter_info(u_id)def get_login_info():
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
        major = str(get_major())
        year = int(get_year())
        gpa = get_gpa()
        add_info = """INSERT INTO Academics 
              (User_ID, major, AcademicYear, GPA) 
              VALUES (%s, %s, %s, %s)"""
        user_info = (user_id, major, year, gpa)
        mycursor.execute(add_info, user_info)
        mydb.commit()
        mydb.close()
        print("success")

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
    enter_info(u_id)def get_login_info():
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
        major = str(get_major())
        year = int(get_year())
        gpa = get_gpa()
        add_info = """INSERT INTO Academics 
              (User_ID, major, AcademicYear, GPA) 
              VALUES (%s, %s, %s, %s)"""
        user_info = (user_id, major, year, gpa)
        mycursor.execute(add_info, user_info)
        mydb.commit()
        mydb.close()
        print("success")

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
    enter_info(u_id)def get_login_info():
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
        major = str(get_major())
        year = int(get_year())
        gpa = get_gpa()
        add_info = """INSERT INTO Academics 
              (User_ID, major, AcademicYear, GPA) 
              VALUES (%s, %s, %s, %s)"""
        user_info = (user_id, major, year, gpa)
        mycursor.execute(add_info, user_info)
        mydb.commit()
        mydb.close()
        print("success")

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
    enter_info(u_id)def get_login_info():
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
        major = str(get_major())
        year = int(get_year())
        gpa = get_gpa()
        add_info = """INSERT INTO Academics 
              (User_ID, major, AcademicYear, GPA) 
              VALUES (%s, %s, %s, %s)"""
        user_info = (user_id, major, year, gpa)
        mycursor.execute(add_info, user_info)
        mydb.commit()
        mydb.close()
        print("success")

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
    enter_info(u_id)def get_login_info():
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
        major = str(get_major())
        year = int(get_year())
        gpa = get_gpa()
        add_info = """INSERT INTO Academics 
              (User_ID, major, AcademicYear, GPA) 
              VALUES (%s, %s, %s, %s)"""
        user_info = (user_id, major, year, gpa)
        mycursor.execute(add_info, user_info)
        mydb.commit()
        mydb.close()
        print("success")

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
    enter_info(u_id)def get_login_info():
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
        major = str(get_major())
        year = int(get_year())
        gpa = get_gpa()
        add_info = """INSERT INTO Academics 
              (User_ID, major, AcademicYear, GPA) 
              VALUES (%s, %s, %s, %s)"""
        user_info = (user_id, major, year, gpa)
        mycursor.execute(add_info, user_info)
        mydb.commit()
        mydb.close()
        print("success")

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
    enter_info(u_id)def get_login_info():
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
        major = str(get_major())
        year = int(get_year())
        gpa = get_gpa()
        add_info = """INSERT INTO Academics 
              (User_ID, major, AcademicYear, GPA) 
              VALUES (%s, %s, %s, %s)"""
        user_info = (user_id, major, year, gpa)
        mycursor.execute(add_info, user_info)
        mydb.commit()
        mydb.close()
        print("success")

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
        major = str(get_major())
        year = int(get_year())
        gpa = get_gpa()
        add_info = """INSERT INTO Academics 
              (User_ID, major, AcademicYear, GPA) 
              VALUES (%s, %s, %s, %s)"""
        user_info = (user_id, major, year, gpa)
        mycursor.execute(add_info, user_info)
        mydb.commit()
        mydb.close()
        print("success")

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