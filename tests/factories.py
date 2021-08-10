import factory

from database import db
from gstudent.database.entities.student_entity import StudentEntity


class StudentFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = StudentEntity
        sqlalchemy_session = db.session

    id = factory.Faker("uuid4")
    name = factory.Faker("first_name")
    surname = factory.Faker("last_name")
    specialization = factory.Faker("word")


class CreateUpdateStudentFactory(factory.DictFactory):
    class Meta:
        model = StudentEntity

    name = factory.Faker("first_name")
    surname = factory.Faker("last_name")
    specialization = factory.Faker("word")
