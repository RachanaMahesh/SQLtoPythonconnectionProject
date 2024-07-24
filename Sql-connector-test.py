import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root",passwd="Dream@24",port='3306',database="test_userdetails")

mycurser = mydb.cursor()

mycurser.execute("select * from users")
for i in mycurser:
    print(i)

print("Done Done Done")