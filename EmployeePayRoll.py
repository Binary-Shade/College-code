import tkinter as tk
import sqlite3

# Database initialization
conn = sqlite3.connect("payroll.db")
cur = conn.cursor()

# Create table if it doesn't exist
cur.execute("CREATE TABLE IF NOT EXISTS employees (employee_id INTEGER PRIMARY KEY, name TEXT, salary REAL)")

# Function to add an employee
def add_employee():
    employee_id = int(id_entry.get())
    name = name_entry.get()
    salary = float(salary_entry.get())
    cur.execute("INSERT INTO employees (employee_id, name, salary) VALUES (?, ?, ?)", (employee_id, name, salary))
    conn.commit()
    status_label.config(text="Employee added successfully.")

# Function to display all employees
def display_employees():
    cur.execute("SELECT * FROM employees")
    employees = cur.fetchall()
    if employees:
        for employee in employees:
            print(employee)
    else:
        print("No employees in the database.")

# Function to calculate total salary
def calculate_total_salary():
    cur.execute("SELECT SUM(salary) FROM employees")
    total_salary = cur.fetchone()[0]
    status_label.config(text="Total Salary: $%.2f" % total_salary)

# GUI initialization
root = tk.Tk()
root.title("Employee Payroll System")

# ID Label and Entry
id_label = tk.Label(root, text="Employee ID:")
id_label.grid(row=0, column=0, padx=10, pady=10)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=10, pady=10)

# Name Label and Entry
name_label = tk.Label(root, text="Name:")
name_label.grid(row=1, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=10)

# Salary Label and Entry
salary_label = tk.Label(root, text="Salary:")
salary_label.grid(row=2, column=0, padx=10, pady=10)
salary_entry = tk.Entry(root)
salary_entry.grid(row=2, column=1, padx=10, pady=10)

# Add Button
add_button = tk.Button(root, text="Add Employee", command=add_employee)
add_button.grid(row=3, column=0, padx=10, pady=10)

# Display Button
display_button = tk.Button(root, text="Display Employees", command=display_employees)
display_button.grid(row=3, column=1, padx=10, pady=10)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate Total Salary", command=calculate_total_salary)
calculate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Status Label
status_label = tk.Label(root, text="")
status_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

# Close database connection
conn.close()
