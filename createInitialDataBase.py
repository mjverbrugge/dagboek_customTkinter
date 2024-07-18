"""
Create a new database and tables
"""
import os
import sqlite3

def validateDB():
    if os.path.isfile("diary.db") == False:
        createDatabase()
    return

def createDatabase():
    # Create to table
    con = sqlite3.connect("diary.db")
    cur = con.cursor()

    # Create table
    cur.execute("CREATE TABLE day(date, entry)")

    # Commit and close
    con.commit()
    con.close()

    return
