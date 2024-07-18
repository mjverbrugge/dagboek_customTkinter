"""
The basic functions to save and load data from the gui to database
"""

import sqlite3

def savePage(saveDate, saveText):

    # Connect to table
    con = sqlite3.connect("diary.db")
    cur = con.cursor()

    # Add data
    cur.execute("INSERT INTO day VALUES('%s', '%s')"%(saveDate, saveText))

    # Commit and close
    con.commit()
    con.close()

    return


def getEntries():
    
    # Connect to table
    con = sqlite3.connect("diary.db")
    cur = con.cursor()

    # Get data
    cur.execute("SELECT * FROM day")
    allData = cur.fetchall()

    # Commit and close
    con.commit()
    con.close()

    return allData


def deleteEntry(name):
    # Connect to table
    con = sqlite3.connect("diary.db")
    cur = con.cursor()

    # Delete data
    cur.execute("DELETE FROM day WHERE date LIKE ?", (name,))

    # Commit and close
    con.commit()
    con.close()

    return 