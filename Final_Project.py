import csv
import datetime

class StudentFeeManager:
    def __init__(self, csv_file="student_fees.csv"):
        """Initialize the manager and ensure the CSV file exists."""
        self.csv_file = csv_file
        self.headers = [
            "Name", "Department", "Roll", "Session", 
            "Admission Fee", "Department Development Fee", 
            "Examination Fee", "Total Fee"
        ]
        self._initialize_csv()

    def _initialize_csv(self):
        """Ensure the CSV file exists with the proper headers."""
        try:
            with open(self.csv_file, mode='x', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.headers)
        except FileExistsError:
            pass  # File already exists, no need to create it.

    def add_student(self, name, department, roll, session, admission_fee, dept_dev_fee, exam_fee):
        """Add a new student's fee details."""
        total_fee = admission_fee + dept_dev_fee + exam_fee
        with open(self.csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, department, roll, session, admission_fee, dept_dev_fee, exam_fee, total_fee])
        print(f"Added record for {name} successfully.")

    def view_summary(self):
        """View all records in the CSV file."""
        print("\nSummary of Student Fees:")
        try:
            with open(self.csv_file, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(", ".join(row))
        except FileNotFoundError:
            print("No data found. Add student details first.")

    def calculate_total_amount(self):
        """Calculate the total fees collected."""
        total = 0
        try:
            with open(self.csv_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    total += float(row["Total Fee"])
            print(f"Total amount collected: ${total:.2f}")
        except FileNotFoundError:
            print("No data found. Add student details first.")


def main():
    manager = StudentFeeManager()

    while True:
        print("\nStudent Fee Management System")
        print("1. Add Student's Names")
        print("2. Add Department")
        print("3. Add Roll")
        print("4. Add Session")
        print("5. Add Admission Fee")
        print("6. Add Department Development Fee")
        print("7. Add Examination Fee")
        print("8. View Summary")
        print("9. Total Amount")
        print("10. Exit")

        choice = input("Choose an option (1-10): ")

        if choice == '1':
            name = input("Enter student's name: ")
            department = input("Enter department: ")
            roll = input("Enter roll: ")
            session = input(f"Enter session (e.g., {datetime.datetime.now().year}): ")
            try:
                admission_fee = float(input("Enter admission fee: "))
                dept_dev_fee = float(input("Enter department development fee: "))
                exam_fee = float(input("Enter examination fee: "))
                manager.add_student(name, department, roll, session, admission_fee, dept_dev_fee, exam_fee)
            except ValueError:
                print("Invalid fee input. Please enter valid numeric values.")
        elif choice == '8':
            manager.view_summary()
        elif choice == '9':
            manager.calculate_total_amount()
        elif choice == '10':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
