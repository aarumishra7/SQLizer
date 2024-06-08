import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
CREATE TABLE STUDENT (
    STUDENT_ID INT,
    NAME VARCHAR(25),
    SECTION VARCHAR(25),
    Maths INT,
    Hindi INT,
    English INT,
    SST INT,
    science INT,
    CITY VARCHAR(50),
    GENDER VARCHAR(10),
    PHONE_NUMBER VARCHAR(15)
);


"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''INSERT INTO STUDENT VALUES (0, 'Krish', 'A', 90, 85, 80, 75, 70, 'Jaipur', 'Male', '1234567890')''')
cursor.execute('''INSERT INTO STUDENT VALUES (1, 'Sudhanshu', 'B', 100, 95, 90, 85, 80, 'Udaipur', 'Male', '9876543210')''')
cursor.execute('''INSERT INTO STUDENT VALUES (2, 'Darius', 'A', 86, 81, 76, 71, 66, 'Jodhpur', 'Male', '7890123456')''')
cursor.execute('''INSERT INTO STUDENT VALUES (3, 'Vikash', 'A', 50, 45, 40, 35, 30, 'Ajmer', 'Male', '8901234567')''')
cursor.execute('''INSERT INTO STUDENT VALUES (4, 'Dipesh', 'A', 35, 30, 25, 20, 15, 'Kota', 'Male', '9012345678')''')
cursor.execute('''INSERT INTO STUDENT VALUES (5, 'Priya', 'B', 95, 90, 85, 80, 75, 'Jaipur', 'Female', '2345678901')''')
cursor.execute('''INSERT INTO STUDENT VALUES (6, 'Ravi', 'A', 88, 83, 78, 73, 68, 'Udaipur', 'Male', '3456789012')''')
cursor.execute('''INSERT INTO STUDENT VALUES (7, 'Aisha', 'B', 92, 87, 82, 77, 72, 'Jodhpur', 'Female', '4567890123')''')
cursor.execute('''INSERT INTO STUDENT VALUES (8, 'Rahul', 'A', 60, 55, 50, 45, 40, 'Ajmer', 'Male', '5678901234')''')
cursor.execute('''INSERT INTO STUDENT VALUES (9, 'Manisha', 'B', 75, 70, 65, 60, 55, 'Kota', 'Female', '6789012345')''')
cursor.execute('''INSERT INTO STUDENT VALUES (10, 'Ananya', 'A', 91, 86, 81, 76, 71, 'Jaipur', 'Female', '7890123456')''')
cursor.execute('''INSERT INTO STUDENT VALUES (11, 'Sachin', 'B', 87, 82, 77, 72, 67, 'Udaipur', 'Male', '8901234567')''')
cursor.execute('''INSERT INTO STUDENT VALUES (12, 'Neha', 'A', 94, 89, 84, 79, 74, 'Jodhpur', 'Female', '9012345678')''')
cursor.execute('''INSERT INTO STUDENT VALUES (13, 'Pankaj', 'B', 65, 60, 55, 50, 45, 'Ajmer', 'Male', '1234567890')''')
cursor.execute('''INSERT INTO STUDENT VALUES (14, 'Kavita', 'A', 70, 65, 60, 55, 50, 'Kota', 'Female', '2345678901')''')
cursor.execute('''INSERT INTO STUDENT VALUES (15, 'Siddharth', 'A', 89, 84, 79, 74, 69, 'Jaipur', 'Male', '3456789012')''')
cursor.execute('''INSERT INTO STUDENT VALUES (16, 'Amit', 'B', 83, 78, 73, 68, 63, 'Udaipur', 'Male', '4567890123')''')
cursor.execute('''INSERT INTO STUDENT VALUES (17, 'Tanvi', 'A', 96, 91, 86, 81, 76, 'Jodhpur', 'Female', '5678901234')''')
cursor.execute('''INSERT INTO STUDENT VALUES (18, 'Rohan', 'B', 72, 67, 62, 57, 52, 'Ajmer', 'Male', '6789012345')''')
cursor.execute('''INSERT INTO STUDENT VALUES (19, 'Shreya', 'A', 78, 73, 68, 63, 58, 'Kota', 'Female', '7890123456')''')


## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()