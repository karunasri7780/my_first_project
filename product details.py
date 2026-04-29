import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="karunasri@123",
    database="product_db"
)

cursor = conn.cursor()

def add_products():
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    price = int(input("Enter Price: "))
    stock = int(input("Enter Stock: "))

    query = "INSERT INTO products VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (id, name, price, stock))
    conn.commit()
    print("Added successfully")

def view_products():
    cursor.execute("SELECT * FROM products")
    result = cursor.fetchall()
    for row in result:
        print("ID:", row[0], "| Name:", row[1], "| Price:", row[2], "| Stock:", row[3])

def update_products():
    id = int(input("Enter ID: "))
    stock = int(input("Enter new stock: "))

    query = "UPDATE products SET stock=%s WHERE id=%s"
    cursor.execute(query, (stock, id))
    conn.commit()
    print("Updated successfully")

def delete_products():
    id = int(input("Enter ID: "))

    query = "DELETE FROM products WHERE id=%s"
    cursor.execute(query, (id,))
    conn.commit()
    print("Deleted successfully")

while True:
    print("\n1. Add Products")
    print("2. View Products")
    print("3. Update Products")
    print("4. Delete Products")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_products()
    elif choice == 2:
        view_products()
    elif choice == 3:
        update_products()
    elif choice == 4:
        delete_products()
    elif choice == 5:
        break
    else:
        print("Invalid choice")