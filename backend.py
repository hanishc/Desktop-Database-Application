import sqlite3

def connect():
    conn=sqlite3.connect("BookStore.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title text ,author text ,year INTEGER ,ISBN INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,ISBN):
    conn=sqlite3.connect("BookStore.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,ISBN))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("BookStore.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",ISBN=""):
    conn=sqlite3.connect("BookStore.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR ISBN=?",(title,author,year,ISBN))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id=""):
    conn=sqlite3.connect("BookStore.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id="",title="",author="",year="",ISBN=""):
    conn=sqlite3.connect("BookStore.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET year=?, ISBN=? WHERE author=?",(year,ISBN,author,))
    conn.commit()
    conn.close()

connect()
#insert(1,'Jooe Watres',1234,13554675)
update("",'John Vander',2012,123243143)
print(search(0,'Jooe Watres',0,0))
print("\n")
#print(search (1,0,0,0))
print(view())
