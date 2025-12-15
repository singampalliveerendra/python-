import sqlite3
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
name_input = (input("Enter name: "))
cursor.execute("select id, name, marks from students where name = ?", (name_input,))
row = cursor.fetchall()
if row:
    for rollno, name, marks in row:
            print("Name :", name)
            print("Marks :", marks)
else:
    print("No students found")
conn.close()
