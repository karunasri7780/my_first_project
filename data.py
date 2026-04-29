import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password"
)

print("Connected successfully!")