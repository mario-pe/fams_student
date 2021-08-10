from gstudent.database.entities.student_entity import StudentEntity
from gstudent.models.student import Student


def to_student_model(entity: StudentEntity):
    return Student(
        id=entity.id,
        name=entity.name,
        surname=entity.surname,
        specialization=entity.specialization,
    )


def to_student_entity(model: Student):
    return StudentEntity(
        id=model.id,
        name=model.name,
        surname=model.surname,
        specialization=model.specialization,
    )
