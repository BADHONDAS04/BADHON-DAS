import csv
from datetime import datetime

class Student:
    def __init__(self):
        """Initialize a new student record with placeholders for details and fees."""
        self.name = ""
        self.department = ""
        self.roll = ""
        self.session = ""
        self.admission_fee = 0.0
        self.dept_dev_fee = 0.0
        self.exam_fee = 0.0
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def add_name(self, name):
        """Set the student's name."""
        self.name = name

    def add_department(self, department):
        """Set the student's department."""
        self.department = department

    def add_roll(self, roll):
        """Set the student's roll number."""
        self.roll = roll

    def add_session(self, session):
        """Set the student's session."""
        self.session = session

    def add_admission_fee(self, fee):
        """Set the student's admission fee after validation."""
        if fee >= 0:
            self.admission_fee = fee
        else:
            print("Admission fee must be a positive number.")

    def add_dept_dev_fee(self, fee):
        """Set the student's department development fee after validation."""
        if fee >= 0:
            self.dept_dev_fee = fee
        else:
            print("Department development fee must be a positive number.")

    def add_exam_fee(self, fee):
        """Set the student's examination fee after validation."""
        if fee >= 0:
            self.exam_fee = fee
        else:
            print("Examination fee must be a positive number.")

    def view_summary(self):
        """Display a summary of the student's details and fees."""
        print("\nStudent Summary:")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Roll: {self.roll}")
        print(f"Session: {self.session}")
        print(f"Admission Fee: ${self.admission_fee:.2f}")
        print(f"Department Development Fee: ${self.dept_dev_fee:.2f}")
        print(f"Examination Fee: ${self.exam_fee:.2f}")
        print(f"Record Created At: {self.created_at}")

    def to_csv_row(self):
        """Convert student data to a list format suitable for CSV writing."""
        return [self.name, self.department, self.roll, self.session,
                self.admission_fee, self.dept_dev_fee, self.exam_fee, self.created_at]

def save_to_csv(student, filename="students_records.csv"):
    """Save student data to a CSV file."""
    headers = ["Name", "Department", "Roll", "Session", "Admission Fee",
               "Department Development Fee", "Examination Fee", "Created At"]
    try:
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            # Check if the file is empty to write headers
            if file.tell() == 0:
                writer.writerow(headers)
            writer.writerow(student.to_csv_row())
        print("Student data has been saved to CSV.")
    except IOError:
        print("An error occurred while saving to CSV.")

def main():
    student = Student()
    
    while True:
        print("\nStudent Registration System Menu")
        print("1. Add Student's Name")
        print("2. Add Department")
        print("3. Add Roll")
        print("4. Add Session")
        print("5. Add Admission Fee")
        print("6. Add Department Development Fee")
        print("7. Add Examination Fee")
        print("8. View Summary")
        print("9. Save to CSV")
        print("10. Exit")

        choice = input("Choose an option (1-10): ")
        
        if choice == '1':
            name = input("Enter student's name: ")
            student.add_name(name)
        elif choice == '2':
            department = input("Enter department: ")
            student.add_department(department)
        elif choice == '3':
            roll = input("Enter roll number: ")
            student.add_roll(roll)
        elif choice == '4':
            session = input("Enter session: ")
            student.add_session(session)
        elif choice == '5':
            try:
                fee = float(input("Enter admission fee: $"))
                student.add_admission_fee(fee)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '6':
            try:
                fee = float(input("Enter department development fee: $"))
                student.add_dept_dev_fee(fee)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '7':
            try:
                fee = float(input("Enter examination fee: $"))
                student.add_exam_fee(fee)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '8':
            student.view_summary()
        elif choice == '9':
            save_to_csv(student)
        elif choice == '10':
            print("Thank you for using the student registration system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
