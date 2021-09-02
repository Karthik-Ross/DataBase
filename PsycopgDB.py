import psycopg2

def createtable():
    conn = psycopg2.connect("dbname='data2' user='postgres' password='postgre' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE data(Roll_No INTEGER,First_Name TEXT,Last_Name TEXT,Marks REAL)")
    conn.commit()
    conn.close()

def insert(roll,fname,lname,mark):
    conn = psycopg2.connect("dbname='data2' user='postgres' password='postgre' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(%s,%s,%s,%s)",(roll,fname,lname,mark))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='data2' user='postgres' password='postgre' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(mark):
    conn = psycopg2.connect("dbname='data2' user='postgres' password='postgre' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("DELETE FROM data WHERE Marks=%s",(mark,))
    conn.commit()
    conn.close()

def update(roll,mark,lname,fname):
    conn = psycopg2.connect("dbname='data2' user='postgres' password='postgre' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("UPDATE data SET Roll_No=%s , Marks=%s , Last_Name=%s WHERE First_Name=%s",(roll,mark,lname,fname))
    conn.commit()
    conn.close()

print(view())
