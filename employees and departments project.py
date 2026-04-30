import mysql.connector
conn=mysql.connector.connect(
  host="localhost",
  user="root",
  password="karunasri@123",
  database="companys_db"
)
cursor=conn.cursor()
  # view employees and department
def view_employees():
    query=""" select 
    e.emp_name,d.dept_name from employees e inner join
    departmentS d on e.dept_id=d.dept_id"""
    cursor.execute(query)
    print("-----view_employes departments-----")
    for row in cursor.fetchall():
        print("employee:",row[0],"|department:",row[1])
        # view all
def view_all():
    query=""" select
    e.emp_name,d.dept_name from employees e left join
    departmentS d on e.dept_id=d.dept_id"""
    cursor.execute(query)
    print("------view_all------")
    for row in cursor.fetchall():
        print("employees:",row[0],"|deparments:",row[1])
        #without departments
def without_departments():
    query=""" select
    e.emp_name from employees e left join departmentS d
    on e.dept_id=d.dept_id
    where d.dept_id  is null"""
    cursor.execute(query)
    print("-----without_deparments-----") 
    for row in cursor.fetchall():
        print("employees:",row[0]) 
while True:
    print("\n======menu=======") 
    print ("1.employees_deparments")
    print("2.view_all") 
    print("3.without_deparments")  
    print("4.exist") 
    choice=int(input("enter the choice:,"))
    if choice==1:
        view_employees()
    elif choice==2:
        view_all()
    elif choice==3:
        without_departments()
    elif choice==4:
        break
    else:
        print("invalid choice")

