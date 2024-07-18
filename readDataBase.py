# Read database
import sqlite3


# Connect to database and create cursor
connection = sqlite3.connect('diary.db')
c = connection.cursor()

# Fetch all database
c.execute("SELECT * FROM day")
totalTokens = c.fetchall()
print('totalTokens: ', totalTokens) 


# Commit command and close
connection.commit()
connection.close()