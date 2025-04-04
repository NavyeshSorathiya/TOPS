# Write a Python program to connect to an SQLite3 database, create a table, insert data, and fetch data.

import sqlite3

# Step 1: Connect to SQLite3 database (or create it if doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Step 2: Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL);''')

print("Table created successfully.")

# Step 3: Insert data into the table
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 25)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 30)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Charlie', 35)")

# Commit the chenges
conn.commit()
print("Data inserted successfully.")

# Step 4: Fetch data from the table
cursor.execute("SELECT * FROM users")

# Fetch all rows of the result
rows = cursor.fetchall()

# Display the fetched data
print("\nFetched Data:")
for row in rows:
    print(row)

# Step 5: Close the connection
conn.close()