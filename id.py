import sqlite3

# Connect to database (temporary in online compiler)
conn = sqlite3.connect("result.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    marks INTEGER
)
""")

# Insert students (sample data)
students = [
    ("Anil", 85),
    ("Sunil", 55),
    ("Vinay", 66),
    ("veeru", 33)
]
students.append(('ravi', 44))

cursor.executemany(
    "INSERT INTO students (name, marks) VALUES (?, ?)",
    students
)

# Save changes
conn.commit()

# Read and print all students
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("ID | Name  | Marks")
print("-------------------")
for row in rows:
    print(row)
    
students.append(('ravi', 44))


# Close connection
conn.close()

