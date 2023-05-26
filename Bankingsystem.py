import tkinter as tk
import sqlite3

# Create a database connection
conn = sqlite3.connect('bank.db')
c = conn.cursor()

# Create a table to store account details
c.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        account_number INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        balance REAL DEFAULT 0
    )
''')
conn.commit()


def create_account():
    name = name_entry.get()
    initial_balance = float(balance_entry.get())

    # Insert account details into the database
    c.execute('INSERT INTO accounts (name, balance) VALUES (?, ?)', (name, initial_balance))
    conn.commit()

    status_label.config(text='Account created successfully.')


def deposit():
    account_number = int(account_entry.get())
    amount = float(amount_entry.get())

    # Check if the account exists
    c.execute('SELECT * FROM accounts WHERE account_number = ?', (account_number,))
    account = c.fetchone()

    if account:
        new_balance = account[2] + amount

        # Update the account balance in the database
        c.execute('UPDATE accounts SET balance = ? WHERE account_number = ?', (new_balance, account_number))
        conn.commit()

        status_label.config(text='Amount deposited successfully.')
    else:
        status_label.config(text='Account not found.')


def withdraw():
    account_number = int(account_entry.get())
    amount = float(amount_entry.get())

    # Check if the account exists
    c.execute('SELECT * FROM accounts WHERE account_number = ?', (account_number,))
    account = c.fetchone()

    if account:
        if account[2] >= amount:
            new_balance = account[2] - amount

            # Update the account balance in the database
            c.execute('UPDATE accounts SET balance = ? WHERE account_number = ?', (new_balance, account_number))
            conn.commit()

            status_label.config(text='Amount withdrawn successfully.')
        else:
            status_label.config(text='Insufficient balance.')
    else:
        status_label.config(text='Account not found.')


def check_balance():
    account_number = int(account_entry.get())

    # Check if the account exists
    c.execute('SELECT * FROM accounts WHERE account_number = ?', (account_number,))
    account = c.fetchone()

    if account:
        balance_label.config(text=f'Account balance: {account[2]}')
    else:
        status_label.config(text='Account not found.')


# Create the main window
window = tk.Tk()
window.title('Banking System')

# Create labels and entry fields
name_label = tk.Label(window, text='Name:')
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

balance_label = tk.Label(window, text='Initial Balance:')
balance_label.pack()
balance_entry = tk.Entry(window)
balance_entry.pack()

account_label = tk.Label(window, text='Account Number:')
account_label.pack()
account_entry = tk.Entry(window)
account_entry.pack()

amount_label = tk.Label(window, text='Amount:')
amount_label.pack()
amount_entry = tk.Entry(window)
amount_entry.pack()

status_label = tk.Label(window, text='')
status_label.pack()

# Create buttons
create_account_btn = tk.Button(window, text='Create Account', command=create_account)
create_account_btn.pack()

deposit_btn = tk.Button(window, text='Deposit', command=deposit)
deposit_btn.pack()

withdraw_btn = tk.Button(window, text='Withdraw', command=withdraw)
withdraw_btn.pack()

balance_btn = tk.Button(window, text='Check Balance', command=check_balance)
balance_btn.pack()

# Start the main window loop
window.mainloop()

# Close the database connection
conn.close()
