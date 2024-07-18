"""
Create a new dictionary frame
"""
import os
import sqlite3

# Check if database is present and delete
if os.path.isfile("diary.db"):
    os.remove("diary.db")

# Create to table
con = sqlite3.connect("diary.db")
cur = con.cursor()

# Create table
cur.execute("CREATE TABLE day(date, entry)")

# Commit and close
con.commit()
con.close()



def addTestData():
    # Connect to table
    con = sqlite3.connect("diary.db")
    cur = con.cursor()

    # Add data
    cur.execute("INSERT INTO day VALUES('%s', '%s')"%('17 - 07 - 2024', 'test 17'))
    cur.execute("INSERT INTO day VALUES('%s', '%s')"%('16 - 07 - 2024', 'test 17'))
    cur.execute("INSERT INTO day VALUES('%s', '%s')"%('17 - 06 - 2024', 'test 1732'))
    cur.execute("INSERT INTO day VALUES('%s', '%s')"%('17 - 05 - 2024', 'test 17234'))
    cur.execute("INSERT INTO day VALUES('%s', '%s')"%('17 - 07 - 2023', 'test 17234'))
    cur.execute("INSERT INTO day VALUES('%s', '%s')"%('17 - 06 - 2023', 'test asdf'))
    cur.execute("INSERT INTO day VALUES('%s', '%s')"%('15 - 07 - 2024', 'test fdas asdf'))
    cur.execute("INSERT INTO day VALUES('%s', '%s')"%('12 - 07 - 2022', 'test \ntest\ntest'))

    # Commit and close
    con.commit()
    con.close()

addTestData()