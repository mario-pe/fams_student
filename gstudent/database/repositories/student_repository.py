from gstudent.database.entities.student_entity import StudentEntity
from gstudent.mapper.student_mapper import to_student_model
from gstudent.models.student import Student
from database import db


class StudentRepository:
    def get_students_list(self, params):
        name = params["name"]
        surname = params["surname"]
        specialization = params["specialization"]
        query = db.session.query(StudentEntity)
        if name:
            query = query.filter(StudentEntity.name == name)
        if surname:
            query = query.filter(StudentEntity.surname == surname)
        if specialization:
            query = query.filter(StudentEntity.specialization == specialization)
        students = query.all()
        return students

    def create_user(self, student: StudentEntity) -> Student:
        db.session.add(student)
        db.session.commit()
        return to_student_model(student)

    def get_student_by_id(self, id: str) -> StudentEntity:
        student_entity = StudentEntity.query.filter_by(id=id).one_or_none()
        if student_entity:
            return student_entity
        api.abort(404, f"Student {id} doesn't exist")

    def update_student(self, student):
        student_entity = StudentEntity.query.filter_by(id=student.id).one_or_none()
        if student_entity:
            student_entity.name = student.name
            student_entity.surname = student.surname
            student_entity.specialization = student.specialization
            db.session.commit()
            return student
        api.abort(404, f"Student {student.id} doesn't exist")

    def delete_student(self, id):
        student = StudentEntity.query.filter_by(id=id).one_or_none()
        if student:
            db.session.delete(student)
            db.session.commit()
