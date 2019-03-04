import cgi

import pymysql

print ("<Welcome to Python Web Program>")
print("<hr/>")
print("<Using Input Tags< h/>>")


form = cgi.FieldStorage()


First_Name=form.getvalue("First_Name")
Last_Name=form.getvalue("Last_Name")
Mobile=form.getvalue("Mobile")
EMail=form.getvalue("EMail")
Password=form.getvalue("Password")
Confrom_Password=form.getvalue("Confrom_Password")
Sex=form.getvalue("Sex")

db = pymysql.connect(host="localhost", user="kamlesh", passwd="123", database="gehlot")

cursor = db.cursor()

cursor.execute("insert into Register values (%s,%s,%s,%s,%s,%s,%s)",(First_Name,Last_Name,Mobile,EMail,Password,Confrom_Password,Sex))

#cursor.execute("insert into Register (First_Name,Last_Name,Mobile,EMail,Password,Confrom_Password,Sex) values (?,?,?,?,?,?,?)",(First_Name,Last_Name,Mobile,EMail,Password,Confrom_Password,Sex))

#cursor.execute("""
 #   INSERT INTO  Register
    #(First_Name, Last_Name,Mobile,EMail,Password,Confrom_Password,Sex) VALUES
    #(%s, %s,%s,%s,%s,%s,%s)""" , (First_Name, Last_Name,Mobile,EMail,Password,Confrom_Password,Sex))

print(" Data Insert ")

db.commit()
db.close()