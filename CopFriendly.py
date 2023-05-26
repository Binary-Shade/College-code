import tkinter as tk
import sqlite3

# Database initialization
conn = sqlite3.connect("eseva.db")
cur = conn.cursor()

# Create table if it doesn't exist
cur.execute("CREATE TABLE IF NOT EXISTS citizens (citizen_id INTEGER PRIMARY KEY, name TEXT, address TEXT)")

# Function to add a citizen
def add_citizen():
    citizen_id = int(id_entry.get())
    name = name_entry.get()
    address = address_entry.get()
    cur.execute("INSERT INTO citizens (citizen_id, name, address) VALUES (?, ?, ?)", (citizen_id, name, address))
    conn.commit()
    status_label.config(text="Citizen added successfully.")

# Function to display all citizens
def display_citizens():
    cur.execute("SELECT * FROM citizens")
    citizens = cur.fetchall()
    if citizens:
        for citizen in citizens:
            print(citizen)
    else:
        print("No citizens in the database.")

# Function to search for a citizen
def search_citizen():
    citizen_id = int(id_entry.get())
    cur.execute("SELECT * FROM citizens WHERE citizen_id=?", (citizen_id,))
    citizen = cur.fetchone()
    if citizen:
        print(citizen)
    else:
        print("Citizen not found.")

# GUI initialization
root = tk.Tk()
root.title("Cop Friendly App - Eseva Database Application")

# ID Label and Entry
id_label = tk.Label(root, text="Citizen ID:")
id_label.grid(row=0, column=0, padx=10, pady=10)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=10, pady=10)

# Name Label and Entry
name_label = tk.Label(root, text="Name:")
name_label.grid(row=1, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=10)

# Address Label and Entry
address_label = tk.Label(root, text="Address:")
address_label.grid(row=2, column=0, padx=10, pady=10)
address_entry = tk.Entry(root)
address_entry.grid(row=2, column=1, padx=10, pady=10)

# Add Button
add_button = tk.Button(root, text="Add Citizen", command=add_citizen)
add_button.grid(row=3, column=0, padx=10, pady=10)

# Display Button
display_button = tk.Button(root, text="Display Citizens", command=display_citizens)
display_button.grid(row=3, column=1, padx=10, pady=10)

# Search Button
search_button = tk.Button(root, text="Search Citizen", command=search_citizen)
search_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Status Label
status_label = tk.Label(root, text="")
status_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

# Close database connection
conn.close()
