import pandas as pd
import sqlite3
from datetime import datetime
import os



# RUN THIS FILE TO RESET THE DATABASE OF FLASHCARDS


# Database file name
db_file = 'flashcardsTable.db'


# Check if the database file exists
if os.path.exists(db_file):
    # Delete the database file
    os.remove(db_file)
    print(f"{db_file} has been deleted.")
else:
    print(f"{db_file} does not exist.")


# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('flashcardsTable.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()


#create flashcard sqlite table
cursor.execute('''
CREATE TABLE IF NOT EXISTS flashcardsTable (
    id INTEGER PRIMARY KEY, 
    native TEXT NOT NULL,
    target TEXT NOT NULL,
    lastStudied TEXT NOT NULL,
    interval INTEGER NOT NULL, 
    cardstate TEXT NOT NULL
)
''')



# load csv with the flashcard data and save it to sql table

# Define the path to your CSV file
csv_file_path = 'flashcardsLingq.csv'

# Load the CSV into a pandas DataFrame without headers (header=None)
# You need to manually specify the column names to match the SQLite table
columns = ['native', 'target', 'lastStudied', 'interval', 'cardstate']  # Adjust this based on your table structure
df = pd.read_csv(csv_file_path, header=None, names=columns)


# Save the DataFrame to the SQLite table
df.to_sql('flashcardsTable', conn, if_exists='append', index=False)


#select first 5 rows of table to show it worked

cursor.execute('SELECT * FROM flashcardsTable LIMIT 5')


# #verify by printing to terminal
# # Fetch all results
# rows = cursor.fetchall()

# # Option 1: Print the results directly
# print("First 5 rows:")
# for row in rows:
#     print(row)