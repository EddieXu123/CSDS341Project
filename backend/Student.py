import mysql.connector
#edit this according to your local configuration
#python -m pip install mysql-connector-python 
#^ make sure this package is installed using terminal so that you can run everything else

#create connection to database
#modify this according to your setup
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql",
  database = "gethub"
)



def matching(classNum, classDept, classSem):
    cursor = mydb.cursor()
    em = (classNum, classDept, classSem)
    cursor.execute("SELECT User_ID FROM Takes WHERE classNum = %s and ClassDept = %s and ClassSem = %s", em)
    myresult = cursor.fetchall()

    for x in myresult:
        id = x[0]
        get_main_info(id)

def get_main_info(User_ID):
    cursor = mydb.cursor()
    em = (User_ID,)
    cursor.execute("SELECT First_Name, Last_Name, gender, PhoneNum FROM Students WHERE User_ID = %s", em)
    myresult = cursor.fetchall()
    fname = myresult[0][0]
    lname = myresult[0][1]
    gender =  myresult[0][2]
    phoneNum =  myresult[0][3]

    cursor = mydb.cursor()
    em = (User_ID,)
    cursor.execute("SELECT interests FROM Interests WHERE User_ID = %s", em)
    myresult = cursor.fetchall()
    interests = myresult[0][0]

    cursor = mydb.cursor()
    em = (User_ID,)
    cursor.execute("SELECT major, AcademicYear, GPA FROM Academics WHERE User_ID = %s", em)
    myresult = cursor.fetchall()
    major = myresult[0][0]
    yr = myresult[0][1]
    gpa = myresult[0][2]

    #print everything out
    print("--------------------------------------")
    print("name:" + fname + " " + lname)




