from gstudent.database.entities.student_entity import StudentEntity
from gstudent.mapper.student_mapper import to_student_model
from gstudent.models.student import Student
from database import db
# from main import api


class StudentRepository:
    def get_students_list(self, params: dict) -> list:
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

    def get_student_by_id(self, id: str) -> Student:
        student_entity = StudentEntity.query.filter_by(id=id).one_or_none()
        if student_entity:
            return to_student_model(student_entity)

    def update_student(self, student: Student) -> Student:
        student_entity = StudentEntity.query.filter_by(id=student.id).one_or_none()
        if student_entity:
            student_entity.name = student.name
            student_entity.surname = student.surname
            student_entity.specialization = student.specialization
            db.session.commit()
            return to_student_model(student_entity)

    def delete_student(self, id: str) -> None:
        student = StudentEntity.query.filter_by(id=id).one_or_none()
        if student:
            db.session.delete(student)
            db.session.commit()
