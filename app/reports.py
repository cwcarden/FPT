import sqlite3
import csv

#By Area 4 query
def seedfield():
    conn = sqlite3.connect('prodplan.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Seedfield')
    data = c.fetchall()
    conn.close()

def budget():
    conn = sqlite3.connect('prodplan.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Budget')
    data = c.fetchall()
    conn.close()

