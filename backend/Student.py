


def matching(classNum, classDept, classSem):
    cursor = mydb.cursor()
    em = (classNum, classDept, classSem)
    cursor.execute("SELECT User_ID FROM Takes WHERE classNum = %s and ClassDept = %s and ClassSem = %s", em)
    myresult = cursor.fetchall()

    for x in myresult:
        id = x[0]
        get_info(id)

def get_info(User_ID):
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




