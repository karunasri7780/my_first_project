import tkinter as tk
from tkinter import messagebox
import mysql.connector

# database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="karunasri@123",
    database="bank_db"
)
cursor = conn.cursor()

# Login Function
def login():
    user_id = id_entry.get()
    pin = pin_entry.get()

    cursor.execute(
        "SELECT * FROM accounts WHERE id=%s AND pin=%s",
        (user_id, pin)
    )
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Success", "Login Successful")
        open_dashboard(user_id)
    else:
        messagebox.showerror("Error", "Invalid ID or PIN")

# Dashboard
def open_dashboard(user_id):
    dash = tk.Toplevel(root)
    dash.title("Dashboard")
    dash.geometry("400x350")

    tk.Label(dash, text="Welcome", font=("Arial", 14)).pack(pady=10)

    amount_entry = tk.Entry(dash)
    amount_entry.pack(pady=10)

    # Deposit
    def deposit():
        amount = float(amount_entry.get())

        cursor.execute(
            "UPDATE accounts SET balance = balance + %s WHERE id=%s",
            (amount, user_id)
        )

        cursor.execute(
            "INSERT INTO transactions (acc_id, type, amount) VALUES (%s,%s,%s)",
            (user_id, 'deposit', amount)
        )

        conn.commit()
        messagebox.showinfo("Success", "Amount Deposited")

    # Withdraw
    def withdraw():
        amount = float(amount_entry.get())

        cursor.execute(
            "SELECT balance FROM accounts WHERE id=%s",
            (user_id,)
        )
        balance = cursor.fetchone()[0]

        if balance >= amount:
            cursor.execute(
                "UPDATE accounts SET balance = balance - %s WHERE id=%s",
                (amount, user_id)
            )

            cursor.execute(
                "INSERT INTO transactions (acc_id, type, amount) VALUES (%s,%s,%s)",
                (user_id, 'withdraw', amount)
            )

            conn.commit()
            messagebox.showinfo("Success", "Amount Withdrawn")
        else:
            messagebox.showerror("Error", "Insufficient Balance")

    # Balance Check
    def check_balance():
        cursor.execute(
            "SELECT balance FROM accounts WHERE id=%s",
            (user_id,)
        )
        balance = cursor.fetchone()[0]
        messagebox.showinfo("Balance", f"Balance: {balance}")

    # Buttons
    tk.Button(dash, text="Deposit", command=deposit).pack(pady=5)
    tk.Button(dash, text="Withdraw", command=withdraw).pack(pady=5)
    tk.Button(dash, text="Check Balance", command=check_balance).pack(pady=5)

# Main Window
root = tk.Tk()
root.title("Bank System")
root.geometry("400x300")

tk.Label(root, text="Login", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Enter ID").pack()
id_entry = tk.Entry(root)
id_entry.pack()

tk.Label(root, text="Enter PIN").pack()
pin_entry = tk.Entry(root, show="*")
pin_entry.pack()

tk.Button(root, text="Login", command=login).pack(pady=20)

# Run App
root.mainloop()