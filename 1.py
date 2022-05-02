
import psycopg2

conn = psycopg2.connect(dbname='postgres', user='postgres', password='2huaweiszb', host='localhost')
cursor = conn.cursor()
cursor.execute("SELECT * FROM t2")
results = cursor.fetchall()
print(results)
