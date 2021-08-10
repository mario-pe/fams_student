from gstudent.database.repositories.student_repository import StudentRepository
from gstudent.mapper.student_mapper import to_student_entity
from gstudent.models.student import Student


class StudentService:
    def __init__(self):
        self.student_data_service = StudentRepository()

    def get_students_list(self, params):
        students = self.student_data_service.get_students_list(params)
        return students

    def create_student(self, student_model: Student) -> Student:
        student_entity = to_student_entity(student_model)
        return self.student_data_service.create_user(student_entity)

    def get_student_details(self, id):
        student = self.student_data_service.get_student_by_id(id)
        return student

    def update_student(self, student):
        student = self.student_data_service.update_student(student)
        return student

    def delete_student(self, id):
        self.student_data_service.delete_student(id)
