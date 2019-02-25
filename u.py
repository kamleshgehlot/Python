import pymysql

  
#user= input ("Enter Your Username = ")

#as = input ("Enter Your Passwors = ")

db = pymysql.connect(host="localhost", user="kamlesh", passwd="123", database="gehlot")


cursor = db.cursor()

id1 = 1
name= 'yogesh'


cursor.execute('insert into emp(id,Name) values(:id,:Name)',{'id':id1,'Name':name})


data = cursor.fetchone()

print ( data)

db.close()
