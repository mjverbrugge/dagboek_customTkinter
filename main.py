"""
Main file to run the application
"""

# Database
import createInitialDataBase as cIDB
cIDB.validateDB()

# Main run
from windowFrame import root
root.mainloop()