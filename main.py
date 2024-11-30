
class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    def __str__(self):
        return f"Roll Number: {self.roll_number}, Name: {self.name}, Grade: {self.grade}"

    def update_grade(self, new_grade):
        self.grade = new_grade
        print(f"{self.name}'s grade has been updated to {self.grade}")


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter student's name: ")
        while True:
            try:
                roll_number = int(input("Enter student's roll number: "))
                break
            except ValueError:
                print("Invalid input! Roll number must be an integer.")

        grade = input("Enter student's grade (A, B, C, etc.): ").upper()
        student = Student(name, roll_number, grade)
        self.students.append(student)
        print(f"Student {name} has been added successfully.")

    def display_all_students(self):
        if not self.students:
            print("No students in the system.")
        else:
            for student in self.students:
                print(student)

    def search_student_by_roll_number(self):
        try:
            roll_number = int(input("Enter student's roll number to search: "))
            found = False
            for student in self.students:
                if student.roll_number == roll_number:
                    print(student)
                    found = True
                    break
            if not found:
                print(f"No student found with roll number {roll_number}.")
        except ValueError:
            print("Invalid input! Roll number must be an integer.")

    def update_student_grade(self):
        try:
            roll_number = int(input("Enter student's roll number to update grade: "))
            found = False
            for student in self.students:
                if student.roll_number == roll_number:
                    new_grade = input(f"Enter new grade for {student.name}: ").upper()
                    student.update_grade(new_grade)
                    found = True
                    break
            if not found:
                print(f"No student found with roll number {roll_number}.")
        except ValueError:
            print("Invalid input! Roll number must be an integer.")

    def exit_system(self):
        print("Exiting the system...")
        exit()


def main():
    system = StudentManagementSystem()

    while True:
        print("\nStudent Management System Menu:")
        print("1. Add a new student")
        print("2. View all students")
        print("3. Search student by roll number")
        print("4. Update student grade")
        print("5. Exit")

        option = input("Choose an option (1-5): ")

        if option == "1":
            system.add_student()
        elif option == "2":
            system.display_all_students()
        elif option == "3":
            system.search_student_by_roll_number()
        elif option == "4":
            system.update_student_grade()
        elif option == "5":
            system.exit_system()
        else:
            print("Invalid option! Please select a number between 1 and 5.")


if __name__ == "__main__":
    main()


