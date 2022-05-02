import psycopg2

hostname='localhost'
database='snake_db'
username='postgres'
pwd='2huaweiszb4'
port_id=5432
cur,conn=None,None
name=input("Enter the name:")
    
conn=psycopg2.connect(
    host=hostname,
    dbname=database,
    user=username,
    password=pwd,
    port=port_id 
) 
#tells curso to read 
cur=conn.cursor()
#makes sure when comand is executed it will drop the table first then create it (fisrt_name is primary key)
cur.execute('DROP TABLE IF EXISTS user_table')
create_script='''CREATE TABLE IF NOT EXISTS user_table(
                        first_name        VARCHAR(20) PRIMARY KEY,
                        user_level  INT       )'''

cur.execute(create_script)

   
"""for record in cur.fetchall():
    #print(record[0],record[1])
    print(record[0],666)"""
    
delete_script='DELETE FROM user_table where first_name=%s'
delete_record=('py snake.py',)
cur.execute(delete_script,delete_record)    
    #saving all transaction we have done to a database
conn.commit()

if cur is not None:
    cur.close()
if conn is not None:
    conn.close()

    #after name check the level select it that is it 