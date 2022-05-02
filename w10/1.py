import psycopg2
import csv
#for accesing as dict from column name
import psycopg2.extras
print('If you want csv,enter csv.If you want to enter yourself,press enter then number of people ,write [name] and [number].')
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
   #tells curso to read in dict
    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    #makes sure when comand is executed it will drop the table first then create it (id is primary key)
    cur.execute('DROP TABLE IF EXISTS phonebook')
    create_script='''CREATE TABLE IF NOT EXISTS phonebook( 
                        first_name    VARCHAR(40) NOT NULL,
                        phone_num     VARCHAR(15) PRIMARY KEY NOT NULL )'''

    cur.execute(create_script)

    txt=input('Enter yor option:')
    insert_script='''INSERT INTO phonebook(first_name,phone_num) VALUES(%s,%s)'''
    if txt=='csv':
        insert_value=[]
        with open('MOCK_DATA.csv') as f:
            csv_reader=csv.reader(f)
            next(csv_reader)
            for line in csv_reader:
                insert_value.append((line[0],line[1])) 
            for record in insert_value:
                cur.execute(insert_script,record)  
    else:
        insert_value=[]
        n=int(input('Enter num:'))
        for i in range(n):
            text=input('Enter info:')
            line=text.split()
            insert_value.append((line[0],line[1]))
        for record in insert_value:
            cur.execute(insert_script,record)

    update_script="UPDATE phonebook SET phone_num = '74745666660' WHERE first_name = 'Heddi'"
    cur.execute(update_script)

    update_script2="UPDATE phonebook SET first_name ='Aidos' WHERE phone_num ='910-295-7194'"
    cur.execute(update_script2)

    delete_script='DELETE FROM phonebook where first_name=%s'
    delete_record=('Brittne',)
    cur.execute(delete_script,delete_record)
    #fetches all the record from employee table,it read data and places in cur"""
    cur.execute('SELECT * FROM phonebook ORDER BY phonebook.first_name')
    
    
    for record in cur.fetchall():
        print(record['first_name'],record['phone_num'])
    
    
    #saving all transaction we have done to a database
    conn.commit()


except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()