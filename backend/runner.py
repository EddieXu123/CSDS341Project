import mysql.connector
#edit this according to your local configuration
#python -m pip install mysql-connector-python 
#^ make sure this package is installed using terminal so that you can run everything else

#create connection to database
#modify this according to your setup
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="mysql",
  database = "gethub"
)


mycursor = mydb.cursor()

#sample SQL query format
#sql = "INSERT INTO Login_Info (Email_address, Password) VALUES (%s, %s)"
#val = ("pthik2000@gmail.com", "1234")
#mycursor.execute(sql, val)

#list of methods for register
def get_first_name():
    return input('Please enter your first name')

def get_last_name():
    return input('Please enter your last name')

def get_gpa():
    return input('Please Enter your GPA on a 4.0 scale: ')

def create_student():
    first_name = get_first_name()
    last_name = get_last_name()







#application starts here
key = 1
print("Welcome to Gethub, the real antisocial social club")
while( key >= 1):
    print("press 1 to login")
    print("press 2 to register")
    print("press 0 to quit")
    val = input()
    if(int(val) > 2):
        print("invalid value, try again")
    elif(int(val) == 0):
        key = int(val)
    else:
        key = int(val)
        if(key == 1):
            #login()
        else:
            #register()


    


