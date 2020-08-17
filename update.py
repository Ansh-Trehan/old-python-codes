import sqlite3
conn=sqlite3.connect('Data.db')
print('Opened database successfully')
conn.execute("UPDATE BANKS set SALARY = 25000.00 where ID=14")
conn.commit()
print("Total number of rows updated ", conn.total_changes)
cursor=conn.execute("SELECT id, name, address, salary from BANKS")
for row in cursor:
    print ("ID = ",row[0])
    print ("NAME = ", row[1])
    print ("ADDRESS = ", row[2])
    print ("SALARY = ", row[3], "\n")
print ("Operation done successfully")
conn.close()
