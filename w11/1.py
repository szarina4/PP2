from subprocess import call
import psycopg2,re
import csv
import psycopg2.extras
#for accesing as dict from column name
hostname='localhost'
database='phone'
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

    
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    #1
    #cur.callproc('search',['Ai%',])
    #print(cur.fetchall())
    
    #2,#5
    #cur.execute('CALL new_user(%s,%s)',['Aidos', '676-454-3434'])
    #cur.execute('CALL delete_by_phone(%s)',['557-933-5191',])
    #cur.execute('CALL delete_by_name(%s)',['Pip',])
    
    """cur.execute('SELECT * FROM phonebook ORDER BY phonebook.first_name')
    for record in cur.fetchall():
        print(record['first_name'],record['phone_num'])"""

    def procedure(a):
        b=[]
        for x in a:
            z=re.search('[0-9]{3}-[0-9]{3}-[0-9]{4}',x[1])
            if z:
                insert_script='''INSERT INTO phonebook(first_name,phone_num) VALUES(%s,%s)'''
                cur.execute(insert_script,(x[0],x[1]))
            else:
                b.append((x[0],x[1]))
        cur.execute('SELECT * FROM phonebook ORDER BY phonebook.first_name')
        for record in cur.fetchall():
            print(record['first_name'],record['phone_num'])
        if b:
            print('Incorrect data',b)

   #3
    my_list=[('Jake','577-565-2323'),('Hayzy','564-232-6534'),('Jamal','454-44')]
    procedure(my_list)


    
    #4
    #cur.callproc('paginated_func',[3,4])
    #print(cur.fetchall())

    

    
    
    
    conn.commit()
    

    conn.commit()


except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()