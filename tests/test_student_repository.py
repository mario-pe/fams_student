# import factory
# import pytest
# from werkzeug.exceptions import NotFound
#
# from app import db
# from gstudent.models import Student
# from gstudent.database.repositories.student_repository import StudentRepository
# from tests.factories import StudentFactory, CreateUpdateStudentFactory
#
#
# def test_should_return_student_list():
#     data = {}
#     number_of_students = 5
#     StudentFactory.create_batch(number_of_students)
#
#     result = StudentRepository.get_students_list(data)
#
#     assert len(result) == number_of_students
#
#
# def test_should_return_students_filtered_by_surname():
#     data = {"name": "name"}
#     number_of_students = 5
#     expected_result = 1
#     StudentFactory.create(name="name")
#     StudentFactory.create_batch(number_of_students)
#
#     result = StudentRepository.get_students_list(data)
#
#     assert len(result) == expected_result
#
#
# def test_should_return_students_filtered_by_surname_specialization():
#     expected_result = 1
#     number_of_students = 5
#     data = {"name": "name", "specialization": "specialization"}
#     StudentFactory.create(name="name", specialization="specialization")
#     StudentFactory.create_batch(number_of_students)
#
#     result = StudentRepository.get_students_list(data)
#
#     assert len(result) == expected_result
#
#
# def test_should_create_student_object():
#     data = factory.build(dict, FACTORY_CLASS=CreateUpdateStudentFactory)
#
#     StudentRepository.create_user(data)
#
#
# def test_should_return_student_details():
#     student = StudentFactory.create()
#
#     result = StudentRepository.get_student_by_uuid(student.uuid)
#
#     assert student.uuid == result.uuid
#     assert student.name == result.name
#     assert student.surname == result.surname
#     assert student.specialization == result.specialization
#
#
# def test_should_rise_exeption_if_uuid_not_exists():
#     fake_uuid = "c4bb0029-f4e2-436f-afd2-b3752b2b87be"
#
#     with pytest.raises(NotFound) as e:
#         StudentRepository.get_student_by_uuid(fake_uuid)
#
#
# def test_update_student():
#     student = StudentFactory.create()
#     data = factory.build(dict, FACTORY_CLASS=CreateUpdateStudentFactory)
#
#     StudentRepository.update_student(student.uuid, data)
#
#     assert student.name == data["name"]
#     assert student.surname == data["surname"]
#     assert student.specialization == data["specialization"]
#
#
# def test_should_remove_student_and_return_None():
#     created_students_number = 5
#     StudentFactory.create_batch(created_students_number)
#     student = StudentFactory.create()
#     number_of_students_befor_action = db.session.query(Student).count()
#
#     StudentRepository.delete_student(student.uuid)
#
#     assert number_of_students_befor_action - 1 == db.session.query(Student).count()
#
#
# def test_should_return_None_if_user_not_exists():
#     created_students_number = 5
#     StudentFactory.create_batch(created_students_number)
#     number_of_students_befor_action = db.session.query(Student).count()
#     fake_uuid = "c4bb0029-f4e2-436f-afd2-b3752b2b87be"
#
#     StudentRepository.delete_student(fake_uuid)
#
#     assert number_of_students_befor_action == db.session.query(Student).count()
