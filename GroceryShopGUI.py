import tkinter as tk
import sqlite3

# Database initialization
conn = sqlite3.connect("inventory.db")
cur = conn.cursor()

# Create table if it doesn't exist
cur.execute("CREATE TABLE IF NOT EXISTS products (product_id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER)")

# Function to add a product to the inventory
def add_product():
    product_id = int(id_entry.get())
    name = name_entry.get()
    quantity = int(quantity_entry.get())
    cur.execute("INSERT INTO products (product_id, name, quantity) VALUES (?, ?, ?)", (product_id, name, quantity))
    conn.commit()
    status_label.config(text="Product added successfully.")

# Function to display all products in the inventory
def display_products():
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    if products:
        for product in products:
            print(product)
    else:
        print("No products in the inventory.")

# Function to search for a product in the inventory
def search_product():
    product_id = int(id_entry.get())
    cur.execute("SELECT * FROM products WHERE product_id=?", (product_id,))
    product = cur.fetchone()
    if product:
        print(product)
    else:
        print("Product not found.")

# GUI initialization
root = tk.Tk()
root.title("EMart Grocery Shop - Inventory Management System")

# ID Label and Entry
id_label = tk.Label(root, text="Product ID:")
id_label.grid(row=0, column=0, padx=10, pady=10)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=10, pady=10)

# Name Label and Entry
name_label = tk.Label(root, text="Name:")
name_label.grid(row=1, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=10)

# Quantity Label and Entry
quantity_label = tk.Label(root, text="Quantity:")
quantity_label.grid(row=2, column=0, padx=10, pady=10)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=2, column=1, padx=10, pady=10)

# Add Button
add_button = tk.Button(root, text="Add Product", command=add_product)
add_button.grid(row=3, column=0, padx=10, pady=10)

# Display Button
display_button = tk.Button(root, text="Display Products", command=display_products)
display_button.grid(row=3, column=1, padx=10, pady=10)

# Search Button
search_button = tk.Button(root, text="Search Product", command=search_product)
search_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Status Label
status_label = tk.Label(root, text="")
status_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

# Close database connection
conn.close()
