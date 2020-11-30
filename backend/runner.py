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

def get_email():
    email = input('Please enter your email: ')
    while (check_email(email)):
        print("This email already exists in the Database. Try again...")
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

def get_user_id(email):
    cursor = mydb.cursor()
    em = (email, )
    cursor.execute("SELECT User_ID FROM Login_Info WHERE Email_address = %s", em)
    myresult = cursor.fetchall()
    return myresult[0][0]

# Only add if the username (email address) doesn't exist
def register():
    email = get_email()
    first = get_first_name()
    last = get_last_name()
    sql = "INSERT INTO Login_Info (Email_address, Password) VALUES (%s, %s)"
    val = (str(email), str(last))
    mycursor.execute(sql, val)
    mydb.commit()
    print(get_user_id(email))
    print("Success")


register()






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
            print(key)
        else:
            print(key)


    


