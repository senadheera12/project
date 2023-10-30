# Initialize an empty list to store student details
student_records = []


# Function to add a new student
def add_student():
    name = input("Enter student name: ")
    reg_number = input("Enter register number: ")
    address = input("Enter address: ")
    student_class = input("Enter class: ")
    guardian = input("Enter guardian name: ")
    guardian_contact = input("Enter guardian contact number: ")

    student = {
        "Name": name,
        "Register Number": reg_number,
        "Address": address,
        "Class": student_class,
        "Guardian": guardian,
        "Guardian Contact": guardian_contact
    }

    student_records.append(student)
    print("Student record added successfully!")


# Function to display all student details
def display_students():
    if not student_records:
        print("No student records found.")
        return

    print("Student Details:")
    for student in student_records:
        print(
            f"Name: {student['Name']}, Register Number: {student['Register Number']}, Address: {student['Address']}, Class: {student['Class']}, Guardian: {student['Guardian']}, Guardian Contact: {student['Guardian Contact']}")


# Function to search for a student by register number
def search_student(reg_number):
    for student in student_records:
        if student["Register Number"] == reg_number:
            print(
                f"Student found - Name: {student['Name']}, Register Number: {student['Register Number']}, Address: {student['Address']}, Class: {student['Class']}, Guardian: {student['Guardian']}, Guardian Contact: {student['Guardian Contact']}")
            return
    print(f"Student with register number {reg_number} not found.")


# Function to insert a new student record
def insert_student():
    index = int(input("Enter the index where you want to insert the student: "))
    if index >= 0 and index <= len(student_records):
        add_student()
        student_records.insert(index, student_records[-1])
        del student_records[-1]
        print("Student record inserted successfully!")
    else:
        print("Invalid index. Please enter a valid index.")


# Function to delete a student record
def delete_student(reg_number):
    for student in student_records:
        if student["Register Number"] == reg_number:
            student_records.remove(student)
            print(f"Student with register number {reg_number} deleted successfully.")
            return
    print(f"Student with register number {reg_number} not found.")


# Function to modify and update a student record
def update_student(reg_number):
    for student in student_records:
        if student["Register Number"] == reg_number:
            print("Enter the new information for the student:")
            add_student()
            student_records.remove(student)
            student_records.append(student_records[-1])
            del student_records[-1]
            print(f"Student record with register number {reg_number} updated successfully.")
            return
    print(f"Student with register number {reg_number} not found.")


# Main program loop
while True:
    print("\nStudent Details Management System")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student by Register Number")
    print("4. Insert Student")
    print("5. Delete Student")
    print("6. Update Student Record")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        reg_number = input("Enter the register number to search: ")
        search_student(reg_number)
    elif choice == '4':
        insert_student()
    elif choice == '5':
        reg_number = input("Enter the register number to delete: ")
        delete_student(reg_number)
    elif choice == '6':
        reg_number = input("Enter the register number to update: ")
        update_student(reg_number)
    elif choice == '7':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
