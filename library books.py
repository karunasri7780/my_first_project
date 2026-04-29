import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="karunasri@123",
    database="library_db"
)

cursor = conn.cursor()

# ➕ Add Book
def add_book():
    name = input("Book name: ")
    author = input("Author: ")
    qty = int(input("Quantity: "))
    
    query = "INSERT INTO books (name, author, quantity) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, author, qty))
    conn.commit()
    print("Book added!")

# 📋 View Books
def view_books():
    cursor.execute("SELECT * FROM books")
    for row in cursor.fetchall():
        print(row)

# 📤 Issue Book
def issue_book():
    book_id = int(input("Enter book id: "))
    user = input("Enter user name: ")

    cursor.execute("SELECT quantity FROM books WHERE id=%s", (book_id,))
    result = cursor.fetchone()

    if result and result[0] > 0:
        cursor.execute("INSERT INTO issued_books (book_id, user_name) VALUES (%s, %s)", (book_id, user))
        cursor.execute("UPDATE books SET quantity = quantity - 1 WHERE id=%s", (book_id,))
        conn.commit()
        print("Book issued!")
    else:
        print("Book not available!")

# 📥 Return Book
def return_book():
    book_id = int(input("Enter book id: "))
    
    cursor.execute("DELETE FROM issued_books WHERE book_id=%s LIMIT 1", (book_id,))
    cursor.execute("UPDATE books SET quantity = quantity + 1 WHERE id=%s", (book_id,))
    conn.commit()
    
    print("Book returned!")

# 🔁 Menu
while True:
    print("\n1.Add Book  2.View Books  3.Issue  4.Return  5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        add_book()
    elif choice == 2:
        view_books()
    elif choice == 3:
        issue_book()
    elif choice == 4:
        return_book()
    elif choice == 5:
        break
    else:
        print("Invalid choice")