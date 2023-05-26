import tkinter as tk
import sqlite3

# Database initialization
conn = sqlite3.connect("stock.db")
cur = conn.cursor()

# Create table if it doesn't exist
cur.execute("CREATE TABLE IF NOT EXISTS stock (item TEXT, quantity INTEGER)")

# Function to add an item to the stock
def add_item():
    item = item_entry.get()
    quantity = int(quantity_entry.get())
    cur.execute("INSERT INTO stock VALUES (?, ?)", (item, quantity))
    conn.commit()
    status_label.config(text="Item added successfully.")

# Function to display all items in the stock
def display_items():
    cur.execute("SELECT * FROM stock")
    items = cur.fetchall()
    if items:
        for item in items:
            print(item)
    else:
        print("No items in stock.")

# Function to delete an item from the stock
def delete_item():
    item = item_entry.get()
    cur.execute("DELETE FROM stock WHERE item=?", (item,))
    conn.commit()
    status_label.config(text="Item deleted successfully.")

# GUI initialization
root = tk.Tk()
root.title("Super Market Stock Maintenance System")

# Item Label and Entry
item_label = tk.Label(root, text="Item:")
item_label.grid(row=0, column=0, padx=10, pady=10)
item_entry = tk.Entry(root)
item_entry.grid(row=0, column=1, padx=10, pady=10)

# Quantity Label and Entry
quantity_label = tk.Label(root, text="Quantity:")
quantity_label.grid(row=1, column=0, padx=10, pady=10)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=1, column=1, padx=10, pady=10)

# Add Button
add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.grid(row=2, column=0, padx=10, pady=10)

# Display Button
display_button = tk.Button(root, text="Display Items", command=display_items)
display_button.grid(row=2, column=1, padx=10, pady=10)

# Delete Button
delete_button = tk.Button(root, text="Delete Item", command=delete_item)
delete_button.grid(row=2, column=2, padx=10, pady=10)

# Status Label
status_label = tk.Label(root, text="")
status_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()

# Close database connection
conn.close()
