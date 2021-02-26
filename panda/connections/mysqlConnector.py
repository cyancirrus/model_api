import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="proto",
  password="dreamhope",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

mycursor.execute("select id_demographic from person where id_person = 1")
myresult = mycursor.fetchall()
print(myresult)