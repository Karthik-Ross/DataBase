import sqlite3

def createTable():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE data(Roll_No INTEGER,Name TEXT,Marks REAL)")
    conn.commit()
    conn.close()

def insert(x1,x2,x3):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(?,?,?)",(x1,x2,x3))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(x1):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM data where Roll_No=?",(x1,))
    conn.commit()
    conn.close()

def update(roll,name,mark):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("UPDATE data SET Roll_No=? , Name=? WHERE Marks=?",(roll,name,mark))
    conn.commit()
    conn.close()

update(4,'Bannysingh',94.0)
print(view())
