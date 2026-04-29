import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="karunasri@123",
    database="patient_db"
)

cursor = conn.cursor()

# ➕ Add Patient
def add_patients():
    id = int(input("Enter patient id: "))
    name = input("Enter name: ")
    disease = input("Enter disease: ")
    age = int(input("Enter age: "))

    query = "INSERT INTO patient VALUES (%s,%s,%s,%s)"
    cursor.execute(query, (id, name, disease, age))
    conn.commit()

    print("Patient added ✅")


# 📋 View Patients
def view_patients():
    cursor.execute("SELECT * FROM patient")
    for row in cursor.fetchall():
        print(row)


# 🏥 Admit Patient
def admit_patient():
    patient_id = int(input("Enter patient id: "))
    room_no = int(input("Enter room no: "))

    query = "INSERT INTO admitted (patient_id, room_no) VALUES (%s,%s)"
    cursor.execute(query, (patient_id, room_no))
    conn.commit()

    print("Patient admitted ✅")


# 🚪 Discharge Patient
def discharge_details():
    patient_id = int(input("Enter patient id: "))

    cursor.execute("SELECT * FROM admitted WHERE patient_id=%s", (patient_id,))
    result = cursor.fetchone()

    if result:
        confirm = input("Are you sure (yes/no): ")

        if confirm.lower() == "yes":
            cursor.execute("DELETE FROM admitted WHERE patient_id=%s", (patient_id,))
            conn.commit()
            print("Discharged ✅")
        else:
            print("Cancelled ❌")
    else:
        print("Patient not admitted ❌")


# 🔁 MENU (OUTSIDE FUNCTIONS)
while True:
    print("\n1.Add  2.View  3.Admit  4.Discharge  5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        add_patients()
    elif choice == 2:
        view_patients()
    elif choice == 3:
        admit_patient()
    elif choice == 4:
        discharge_details()
    elif choice == 5:
        break
    else:
        print("Invalid choice")

