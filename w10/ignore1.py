import psycopg2
hostname='localhost'
database='demo'
username='postgres'
pwd='2huaweiszb4'
port_id=5432
cur,conn=None,None
try:
    conn=psycopg2.connect(
    host=hostname,
    dbname=database,
    user=username,
    password=pwd,
    port=port_id 
)
    cur=conn.cursor()
    #makes sure when comand is executed it will drop the table first then create it (id is primary key)
    cur.execute('DROP TABLE IF EXISTS employee')
    create_script='''CREATE TABLE IF NOT EXISTS employee(
                        id      INT PRIMARY KEY,
                        first_name    VARCHAR(40) NOT NULL,
                        salary  INT,
                        dept_id VARCHAR(30))'''

    cur.execute(create_script)

    insert_script='''INSERT INTO employee (id,first_name,salary,dept_id) VALUES(%s,%s,%s,%s)'''
    insert_value=[(1,'James',12000,'D1'),(2,'Anne',34000,'A2'),(3,'Robin',34000,'A2')]
    for record in insert_value:
        cur.execute(insert_script,record)
    
    #fetches all the record from employee table,it read data and places in cur
    cur.execute('SELECT * FROM employee')
    for record in cur.fetchall():
        print(record)
        #print(record[0],record[1])
    
    
    
    #saving all transaction we have done to a database
    conn.commit()


except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()