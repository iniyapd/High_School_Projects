import csv
file_name = "students.csv"

def add_student():
    name = input("Enter name:")
    roll = input("Enter roll number:")
    marks = input("Enter marks:")
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, roll, marks])
    print("Student added successfully")

def view_students():
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def search_student():
    find_roll = input("Enter roll number to search:")
    found = False
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[1] == find_roll:
                print("Student Found:", row)
                found = True
                break
    if not found:
        print("Student not found.")

def delete_student():
    delete_roll = input("Enter roll number to delete:")
    lst = []
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        lst = list(reader)
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        for row in lst:
            if row[1] != delete_roll:
                writer.writerow(row)
    print("Deletion completed")


def main():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")
main()
