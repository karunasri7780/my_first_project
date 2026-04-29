import mysql.connector

# connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="karunasri@123",
    database="student_db"
)

cursor = conn.cursor()

# add student
def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, age, course))
    conn.commit()
    print("Student added successfully ✅")

# view students
def view_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

# update student
def update_student():
    id = int(input("Enter student ID to update: "))

    cursor.execute("SELECT * FROM students WHERE id=%s", (id,))
    result = cursor.fetchone()

    if result:
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        course = input("Enter new course: ")

        query = "UPDATE students SET name=%s, age=%s, course=%s WHERE id=%s"
        cursor.execute(query, (name, age, course, id))
        conn.commit()

        print("Student updated successfully ✅")
    else:
        print("ID not found ❌")

def delete_student():
    id = int(input("Enter student ID to delete: "))

    cursor.execute("SELECT * FROM students WHERE id=%s", (id,))
    result = cursor.fetchone()

    if result:
        confirm = input("Are you sure you want to delete? (yes/no): ")

        if confirm.lower() == "yes":
            cursor.execute("DELETE FROM students WHERE id=%s", (id,))
            conn.commit()
            print("Student deleted successfully ❌")
        else:
            print("Delete cancelled 👍")
    else:
        print("ID not found ❌")

def search_student():
    name = input("Enter name to search: ")

    cursor.execute("SELECT * FROM students WHERE name=%s", (name,))
    results = cursor.fetchall()

    if results:
        for row in results:
            print(row)
    else:
        print("No student found ❌")




# menu
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4.delete_students")
    print("5. search students")
    print("6.exist")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice=="5":
        search_student()
    elif choice=="6":
        break
    else:
        print("invalid choice ❌")
