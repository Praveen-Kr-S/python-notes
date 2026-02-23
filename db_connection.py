#db connection
import pymysql as ps

db = ps.connect(user="root",host="localhost",port=3306,password="root",database="praveen")
cur = db.cursor()
# cur.execute(""" create database praveen """)
# cur.execute(""" create table info(name varchar(50),dept varchar(50),age int, phone int) """)
# cur.execute(""" insert into info values("Pradeepa","Cse",3,96325) """)
# cur.execute(""" insert into info values("Sahana","Cse",1,85623) """)
# cur.execute(""" insert into info values("Kumar","Ece",4,32104) """)
# cur.execute(""" delete from info where name = "Kumar" """)
# cur.execute(""" update info set dept="mech",age=5 where name = "Praveen" """)
# cur.execute(""" alter table info drop column phone """)
# cur.execute(""" alter table info add column city varchar(255) """)
cur.execute(""" select * from info """)
data = cur.fetchall()
print(data)
for row in data:
    print(row)
db.commit()
db.close()
# print("DB Connected!")
