print("==========================================")
print("      STUDENT ATTENDANCE MANAGEMENT")
print("==========================================")

students = {}

while True:
    print("\n============== MENU ==============")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Search Student")
    print("5. Attendance Summary")
    print("6. Exit")
    print("==================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")

        if student_id in students:
            print("Student ID already exists.")
        else:
            students[student_id] = {
                "name": name,
                "present": 0,
                "absent": 0
            }
            print("Student added successfully.")

    elif choice == "2":
        student_id = input("Enter student ID: ")

        if student_id not in students:
            print("Student not found.")
        else:
            print("Student:", students[student_id]["name"])
            status = input("Enter attendance (P/A): ").upper()

            if status == "P":
                students[student_id]["present"] += 1
                print("Attendance marked as Present.")
            elif status == "A":
                students[student_id]["absent"] += 1
                print("Attendance marked as Absent.")
            else:
                print("Invalid attendance status.")

    elif choice == "3":
        if not students:
            print("No students available.")
        else:
            print("\n========== ATTENDANCE DETAILS ==========")

            for student_id, details in students.items():
                total = details["present"] + details["absent"]

                if total > 0:
                    percentage = (details["present"] / total) * 100
                else:
                    percentage = 0

                print("\nStudent ID:", student_id)
                print("Name:", details["name"])
                print("Present:", details["present"])
                print("Absent:", details["absent"])
                print("Attendance:", f"{percentage:.2f}%")

    elif choice == "4":
        student_id = input("Enter student ID to search: ")

        if student_id in students:
            details = students[student_id]
            print("\nStudent Found")
            print("Student ID:", student_id)
            print("Name:", details["name"])
            print("Present:", details["present"])
            print("Absent:", details["absent"])
        else:
            print("Student not found.")

    elif choice == "5":
        if not students:
            print("No students available.")
        else:
            total_present = 0
            total_absent = 0

            for details in students.values():
                total_present += details["present"]
                total_absent += details["absent"]

            total_classes = total_present + total_absent

            print("\n========== ATTENDANCE SUMMARY ==========")
            print("Total Students:", len(students))
            print("Total Present Records:", total_present)
            print("Total Absent Records:", total_absent)

            if total_classes > 0:
                percentage = (total_present / total_classes) * 100
                print("Overall Attendance:", f"{percentage:.2f}%")
            else:
                print("Overall Attendance: 0%")

    elif choice == "6":
        print("\nThank you for using the Attendance Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
