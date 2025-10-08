import mysql.connector
import re


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="labexam2_labajo"
)
cursor = db.cursor()


def add_course():
    name = input("Enter course name: ").strip()
    if not name:
        print("❌ Course name cannot be empty!")
        return
    cursor.execute("INSERT INTO courses (name) VALUES (%s)", (name,))
    db.commit()
    print("✅ Course added successfully!")

def view_courses():
    cursor.execute("SELECT * FROM courses")
    rows = cursor.fetchall()
    if not rows:
        print("No courses found.")
    else:
        print("\n--- Course List ---")
        for row in rows:
            print(f"[{row[0]}] {row[1]}")

def update_course():
    view_courses()
    cid = input("\nEnter Course ID to update: ")
    new_name = input("Enter new course name: ").strip()
    cursor.execute("UPDATE courses SET name=%s WHERE id=%s", (new_name, cid))
    db.commit()
    print("✅ Course updated successfully!")

def delete_course():
    view_courses()
    cid = input("\nEnter Course ID to delete: ")
    cursor.execute("DELETE FROM courses WHERE id=%s", (cid,))
    db.commit()
    print("✅ Course deleted successfully!")


def add_student():
    name = input("Enter student name: ").strip()
    email = input("Enter student email: ").strip()



    view_courses()
    course_id = input("Enter Course ID for this student: ").strip()
    cursor.execute(
        "INSERT INTO students (name, email, course_id) VALUES (%s, %s, %s)",
        (name, email, course_id)
    )
    db.commit()
    print("✅ Student added successfully!")

def view_students():
    cursor.execute("""SELECT s.id, s.name, s.email, c.name
                      FROM students s
                      LEFT JOIN courses c ON s.course_id = c.id""")
    rows = cursor.fetchall()
    if not rows:
        print("No students found.")
    else:
        print("\n--- Student List ---")
        for row in rows:
            print(f"[{row[0]}] {row[1]} | {row[2]} | Course: {row[3]}")

def update_student():
    view_students()
    sid = input("\nEnter Student ID to update: ")
    new_name = input("Enter new name: ")
    new_email = input("Enter new email: ")
    view_courses()
    new_course_id = input("Enter new course ID: ")
    cursor.execute(
        "UPDATE students SET name=%s, email=%s, course_id=%s WHERE id=%s",
        (new_name, new_email, new_course_id, sid)
    )
    db.commit()
    print("✅ Student updated successfully!")

def delete_student():
    view_students()
    sid = input("\nEnter Student ID to delete: ")
    cursor.execute("DELETE FROM students WHERE id=%s", (sid,))
    db.commit()
    print("✅ Student deleted successfully!")


def course_menu():
    while True:
        print("""
===== Manage Courses =====
1. Add Course
2. View Courses
3. Update Course
4. Delete Course
0. Back to Main Menu
""")
        choice = input("Enter choice: ")
        if choice == "1":
            add_course()
        elif choice == "2":
            view_courses()
        elif choice == "3":
            update_course()
        elif choice == "4":
            delete_course()
        elif choice == "0":
            break
        else:
            print("❌ Invalid choice, try again.")

def student_menu():
    while True:
        print("""
===== Manage Students =====
1. Add Student
2. View Students
3. Update Student
4. Delete Student
0. Back to Main Menu
""")
        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "0":
            break
        else:
            print("❌ Invalid choice, try again.")


while True:
    print("""
===== CRUD Menu =====
1. Manage Courses
2. Manage Students
0. Exit
""")
    main_choice = input("Enter choice: ")
    if main_choice == "1":
        course_menu()
    elif main_choice == "2":
        student_menu()
    elif main_choice == "0":
        print("Goodbye!")
        break
    else:
        print("❌ Invalid choice, try again.")
