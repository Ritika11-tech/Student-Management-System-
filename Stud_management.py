student_list = []


def add_student():
    record = {
        "ID": input("Enter ID: "),
        "Name": input("Enter Name: "),
        "Age": input("Enter Age: "),
        "Course": input("Enter Course: "),
        "Marks": input("Enter Marks: ")
    }

    student_list.append(record)
    print("Student added successfully.")


def view_students():
    if not student_list:
        print("No students found.")
    else:
        for record in student_list:
            print(record)


def search_student():
    key = input("Enter ID or Name: ")

    for record in student_list:
        if record["ID"] == key or record["Name"].lower() == key.lower():
            print(record)
            return

    print("Student not found.")


def update_student():
    sid = input("Enter Student ID: ")

    for record in student_list:
        if record["ID"] == sid:
            record["Name"] = input("Enter new Name: ")
            record["Age"] = input("Enter new Age: ")
            record["Course"] = input("Enter new Course: ")
            record["Marks"] = input("Enter new Marks: ")
            print("Student updated successfully.")
            return

    print("Student not found.")


def delete_student():
    sid = input("Enter Student ID: ")

    for record in student_list:
        if record["ID"] == sid:
            student_list.remove(record)
            print("Student deleted successfully.")
            return

    print("Student not found.")


while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")