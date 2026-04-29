import mysql.connector

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="karunasri@123",
    database="bank_db"
)

cursor = conn.cursor()

#  Create Account
def create_account():
    id = int(input("Enter Account ID: "))
    name = input("Enter Name: ")
    balance = float(input("Enter Initial Balance: "))
    pin = int(input("Set 4-digit PIN: "))

    query = "INSERT INTO accounts (id, name, balance, pin) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (id, name, balance, pin))
    conn.commit()

    print("Account created successfully!")

#  Login
def login():
    id = int(input("Enter Account ID: "))
    pin = int(input("Enter PIN: "))

    cursor.execute(
        "SELECT * FROM accounts WHERE id=%s AND pin=%s",
        (id, pin)
    )

    result = cursor.fetchone()

    if result:
        print("Login successful!")
        return id
    else:
        print("Invalid ID or PIN")
        return None

#  Deposit
def deposit_amount(user_id):
    amount = float(input("Enter amount: "))

    cursor.execute(
        "UPDATE accounts SET balance = balance + %s WHERE id=%s",
        (amount, user_id)
    )

    cursor.execute(
        "INSERT INTO transactions (acc_id, type, amount) VALUES (%s, %s, %s)",
        (user_id, 'deposit', amount)
    )

    conn.commit()
    print("Amount deposited successfully!")

#  Withdraw
def withdraw_amount(user_id):
    amount = float(input("Enter amount: "))

    cursor.execute("SELECT balance FROM accounts WHERE id=%s", (user_id,))
    balance = cursor.fetchone()[0]

    if balance >= amount:
        cursor.execute(
            "UPDATE accounts SET balance = balance - %s WHERE id=%s",
            (amount, user_id)
        )

        cursor.execute(
            "INSERT INTO transactions (acc_id, type, amount) VALUES (%s, %s, %s)",
            (user_id, 'withdraw', amount)
        )

        conn.commit()
        print("Amount withdrawn successfully!")
    else:
        print("Insufficient balance!")

#  Balance Check
def balance_check(user_id):
    cursor.execute("SELECT balance FROM accounts WHERE id=%s", (user_id,))
    result = cursor.fetchone()

    if result:
        print("Balance:", result[0])
    else:
        print("Account not found")

# Transaction History
def transaction_history(user_id):
    cursor.execute(
        "SELECT type, amount FROM transactions WHERE acc_id=%s",
        (user_id,)
    )

    result = cursor.fetchall()

    print("\n--- Transaction History ---")
    for row in result:
        print("Type:", row[0], "| Amount:", row[1])

# Transfer Money
def transfer_money(user_id):
    to_id = int(input("Enter receiver ID: "))
    amount = float(input("Enter amount: "))

    # sender balance
    cursor.execute("SELECT balance FROM accounts WHERE id=%s", (user_id,))
    sender_balance = cursor.fetchone()[0]

    # receiver exists check
    cursor.execute("SELECT * FROM accounts WHERE id=%s", (to_id,))
    receiver = cursor.fetchone()

    if receiver:
        if sender_balance >= amount:
            # deduct
            cursor.execute(
                "UPDATE accounts SET balance = balance - %s WHERE id=%s",
                (amount, user_id)
            )

            # add
            cursor.execute(
                "UPDATE accounts SET balance = balance + %s WHERE id=%s",
                (amount, to_id)
            )

            # transactions
            cursor.execute(
                "INSERT INTO transactions VALUES (NULL, %s, %s, %s)",
                (user_id, 'transfer_out', amount)
            )

            cursor.execute(
                "INSERT INTO transactions VALUES (NULL, %s, %s, %s)",
                (to_id, 'transfer_in', amount)
            )

            conn.commit()
            print("Money transferred successfully!")
        else:
            print("Insufficient balance!")
    else:
        print("Receiver not found!")

# Main Program
while True:
    print("\n--- BANK SYSTEM ---")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        create_account()

    elif choice == 2:
        user_id = login()

        if user_id:
            while True:
                print("\n--- MENU ---")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Balance Check")
                print("4. Transaction History")
                print("5. Transfer Money")
                print("6. Logout")

                ch = int(input("Enter choice: "))

                if ch == 1:
                    deposit_amount(user_id)
                elif ch == 2:
                    withdraw_amount(user_id)
                elif ch == 3:
                    balance_check(user_id)
                elif ch == 4:
                    transaction_history(user_id)
                elif ch == 5:
                    transfer_money(user_id)
                elif ch == 6:
                    print("Logged out")
                    break
                else:
                    print("Invalid choice")

    elif choice == 3:
        print("Thank you!")
        break

    else:
        print("Invalid choice")