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
