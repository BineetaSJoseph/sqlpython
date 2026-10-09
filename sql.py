import pymysql

conn=pymysql.connect(
    host='localhost',
    user='root',
    password='tesro@123',
    database='aug2026'
)

cursor = conn.cursor()
#sql="insert into employee values(2,'arjun',35000,'dev')";
#sql="insert into employee values(4,'arjun',40000,'hr')";
#sql="insert into employee values(3,'aravind',35000,'Hr')";
#sql="insert into employee values(5,'arun',45000,'finance')";
#sql="insert into employee values(6,'arjun',5000,'it')";
#sql="insert into employee values(1,'arun',25000,'dev')";
#sql="create table employee (id int primary key,name varchar(20),salary int, dept varchar(20))"


sql="select * from employee"
cursor.execute(sql)

# row=cursor.fetchall()   # data in nested tuple format
# print(row)

#for i  in row:  # down by down data will come in tuple format
    # print(i) 

#for i  in row:       # one by one without nested tuple
    #print(i[0],i[1],i[2],i[3]) 

# row=cursor.fetchmany(1)   # one row full print 
# row=cursor.fetchmany(2)   #one and 2 
# row=cursor.fetchmany(3)   
#row=cursor.fetchmany(4)  

row=cursor.fetchone() # top one only get 
print(row)

conn.commit()
conn.close()


