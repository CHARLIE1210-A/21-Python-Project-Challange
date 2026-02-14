# Student Management System

This is a simple command-line Student Management System built with Python. It allows you to add, view, search, update, and delete student records. Data is stored in a JSON file for persistence.

## Features

- Add new students with ID, name, age, and course
- View all students
- Search students by name or ID
- Update student details
- Delete student records
- Data is saved in `storage.json`

## How to Run

1. Make sure you have Python 3.x installed.
2. Open a terminal in the `student_management` directory.
3. Run the application:
   ```bash
   python main.py
   ```
4. Follow the on-screen menu to manage students.

## File Structure

```
student_management/
├── main.py           # Main application logic and menu
├── manager.py        # StudentManager class for CRUD operations
├── student.py        # Student class definition
├── storage.json      # Data file for student records
├── __pycache__/      # Python cache files
```

## Example Usage

- Add a student: Enter ID, name, age, and course when prompted.
- View students: See a list of all students with their details.
- Search: Enter a name or ID to find matching students.
- Update: Change student details by entering their ID.
- Delete: Remove a student by entering their ID.

## License

This project is licensed under the MIT License.

---

Feel free to modify and extend this application for your own learning or use!
