create table Login_Info 
( 
    Email_address char(30) null,
    Password char(20) null,
    Security_PIN int null,
    User_ID int 
        primary key
)

create table User
(
    User_ID int    
        primary key,
    First_Name char(30) null,
    Last_Name char(30) null,
    DOB char(10) null,
    gender char(20) null,
    PhoneNum int null,
        foreign key User_ID references Login_Info
            on update cascade on delete cascade
)

create table Academics
(
    User_ID int 
        primary key,
    major char(20) null,
    AcademicYear int null,
    GPA int null,
        foreign key User_ID references Login_Info
            on update cascade on delete cascade
)

create table Interests
(
    User_ID int 
        primary key,
    interests char(100) null,
        foreign key User_ID references Login_Info
            on update cascade on delete cascade
)

create table Class
(
    ClassName char(30) null,
    ClassNum int null
        primary key,
    ClassDept char(30) null
        primary key,
    ClassSem char(30) 
        primary key,
)

create table Takes
(
    User_ID int 
        primary key,
    ClassNum int null  
        primary key,
        foreign key User_ID references Login_Info
            on update cascade on delete cascade
        foreign key ClassNum references Class
            on update cascade on delete cascade
)