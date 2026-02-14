import json
import os
from student import Student

DATA_FILE = "storage.json"

class StudentManager:
    def __init__(self):
        self.students =  self.load_students()
        
    def load_students(self):
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE,'r') as file:
            data = json.load(file)
            return [Student(**student) for student in data]
        
    def save_students(self):
        with open(DATA_FILE,'w') as file:
            json.dump([student.to_dict() for student in self.students], file, indent=4)
            
    def add_student(self, student):
        self.students.append(student)
        self.save_students()
        
    def list_students(self):
        return self.students
    
    def find_student(self, keyword):
        return [student for student in self.students if keyword.lower() in student.name.lower() or keyword == student.student_id]
    
    def update_student(self, student_id, name=None, age=None, course=None):
        for student in self.students:
            if student.student_id == student_id:
                if name:
                    student.name = name
                if age:
                    student.age = age
                if course:
                    student.course = course
                self.save_students()
                return True
        return False
    
    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                self.save_students()
                return True
        return False
    