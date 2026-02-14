import logging
from student import Student
from manager import StudentManager

logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'
)

def show_menu():
    logging.info("\n===== Student Management System=====")
    logging.info("1. Add Student")
    logging.info("2. View Students")
    logging.info("3. Search Student")
    logging.info("4. Update Student")
    logging.info("5. Delete Student")
    logging.info("6. Exit\n")
    
def main():
    manager = StudentManager()
    
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            sid = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            course = input("Enter Course: ")
            
            student = Student(sid, name, age, course)
            manager.add_student(student)
            logging.info("Student added successfully.")
            
        elif choice == '2':
            students = manager.list_students()
            if not students:
                logging.info("No students found.")
            for student in students:
                logging.info(f"ID: {student.student_id}, Name: {student.name}, Age: {student.age}, Course: {student.course}")

        elif choice == '3':
            key = input("Enter name or ID to search: ")
            results = manager.find_student(key)
            if not results:
                logging.info("No matching student found.")
            for student in results:
                logging.info(f"ID: {student.student_id}, Name: {student.name}, Age: {student.age}, Course: {student.course}")
                
        elif choice == '4':
            sid = input("Enter Student ID to update: ")
            if not manager.find_student(sid):
                logging.info("Student not found.")
                continue
            name = input("New name (leave blank to keep unchanged): ")
            age = input("New age (leave blank to keep unchanged): ")
            course = input("New course (leave blank to keep unchanged): ")
            
            update = manager.update_student(sid, name or None, int(age) if age else None, course or None)
            
            if update:
                logging.info("Student updated successfully.")
            else:
                logging.info("Student not found.")
                
        elif choice == '5':
            sid = input("Enter Student ID to delete: ")
            if not manager.find_student(sid):
                logging.info("Student not found.")
                continue
            delete = manager.delete_student(sid)
            if delete:
                logging.info("Student deleted successfully.")
            else:
                logging.info("Student not found.")
        
        elif choice == '6':
            logging.info("Exiting the system. Goodbye!!")
            break
        
        else:
            logging.warning("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()
        
        