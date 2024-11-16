import csv
import datetime


class StudentRecordSystem:
    def __init__(self, file_name='student_records.csv'):
        """Initialize the system with a CSV file for storing student records."""
        self.file_name = file_name
        self.headers = [
            "Name", "Department", "Roll", "Session",
            "Admission Fee", "Department Development Fee", "Examination Fee"
        ]
        self.initialize_file()

    def initialize_file(self):
        """Ensure the CSV file exists and has the correct headers."""
        try:
            with open(self.file_name, 'x', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.headers)
        except FileExistsError:
            pass  # File already exists

    def add_student(self, name, department, roll, session, admission_fee, dev_fee, exam_fee):
        """Add a new student record."""
        with open(self.file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, department, roll, session, admission_fee, dev_fee, exam_fee])
        print(f"Student record for {name} added successfully!")

    def view_summary(self):
        """Display all student records."""
        try:
            with open(self.file_name, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        except FileNotFoundError:
            print("No records found. Please add some records first.")

    def edit_student(self, roll):
        """Edit a student record by roll."""
        records = []
        found = False
        try:
            with open(self.file_name, 'r') as file:
                reader = csv.reader(file)
                records = list(reader)

            for i, record in enumerate(records):
                if i > 0 and record[2] == roll:
                    found = True
                    print(f"Editing record: {record}")
                    for j, field in enumerate(self.headers):
                        new_value = input(f"Enter new value for {field} (leave blank to keep '{record[j]}'): ")
                        if new_value.strip():
                            record[j] = new_value
                    records[i] = record
                    break

            if found:
                with open(self.file_name, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(records)
                print("Record updated successfully.")
            else:
                print("Roll number not found.")
        except FileNotFoundError:
            print("No records found. Please add some records first.")

    def delete_student(self, roll):
        """Delete a student record by roll."""
        records = []
        found = False
        try:
            with open(self.file_name, 'r') as file:
                reader = csv.reader(file)
                records = list(reader)

            records = [record for record in records if record[2] != roll or records.index(record) == 0]

            with open(self.file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(records)

            print("Record deleted successfully.")
        except FileNotFoundError:
            print("No records found.")

    def calculate_total_amount(self):
        """Calculate the total fees collected."""
        total_amount = 0.0
        try:
            with open(self.file_name, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip headers
                for row in reader:
                    total_amount += sum(float(row[i]) for i in range(4, 7))
            print(f"Total amount collected: ${total_amount:.2f}")
        except FileNotFoundError:
            print("No records found.")
        except ValueError:
            print("Error in data format. Please check the file for invalid entries.")


def main():
    system = StudentRecordSystem()

    while True:
        print("\nStudent Record Management Menu")
        print("1. Add Student's Names")
        print("2. Add Department")
        print("3. Add Roll")
        print("4. Add Session")
        print("5. Add Admission Fee")
        print("6. Add Department Development Fee")
        print("7. Add Examination Fee")
        print("8. View Summary")
        print("9. Edit Option")
        print("10. Delete Option")
        print("11. Total Amount")
        print("12. Exit")

        choice = input("Choose an option (1-12): ")

        if choice == '1':
            name = input("Enter student's name: ")
            department = input("Enter department: ")
            roll = input("Enter roll number: ")
            session = input("Enter session: ")
            try:
                admission_fee = float(input("Enter admission fee: "))
                dev_fee = float(input("Enter department development fee: "))
                exam_fee = float(input("Enter examination fee: "))
                system.add_student(name, department, roll, session, admission_fee, dev_fee, exam_fee)
            except ValueError:
                print("Invalid input. Fees should be numeric.")
        elif choice == '8':
            system.view_summary()
        elif choice == '9':
            roll = input("Enter roll number to edit: ")
            system.edit_student(roll)
        elif choice == '10':
            roll = input("Enter roll number to delete: ")
            system.delete_student(roll)
        elif choice == '11':
            system.calculate_total_amount()
        elif choice == '12':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
