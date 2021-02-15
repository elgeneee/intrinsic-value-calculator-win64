import sqlite3
import datetime

def connect():
    conn = sqlite3.connect("intrinsic.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS stock (id INTEGER PRIMARY KEY, date_added text,ticker text, intrinsic_value text) ")
    conn.commit()
    conn.close()
    print("Connected to database successfully")

def insert(ticker, intrinsic_value):
    current_day = datetime.date.today()
    date_added =(str)(current_day.day )+ "-" + (str)(current_day.month) + "-" + (str)(current_day.year)
    conn = sqlite3.connect("intrinsic.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO stock VALUES (NULL, ?,?,?) ", (date_added, ticker, intrinsic_value))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("intrinsic.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM stock")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("intrinsic.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM stock WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    
connect()
