import factory
from tests.factories import StudentFactory, CreateUpdateStudentFactory


def test_should_return_empty_list_if_students_not_exists(client):
    re = client.get("/students/")

    assert re.status_code == 200
    assert re.json == []


def tests_should_return_status_code_200_and_list_of_students(client):
    number_of_expected_students = 5
    StudentFactory.create_batch(number_of_expected_students)

    re = client.get("/students/")

    assert re.status_code == 200
    assert len(re.json) == number_of_expected_students

#
# def test_should_return_students_filtered_by_name(client):
#     number_of_expected_students = 1
#     number_of_students = 5
#     StudentFactory.create(name="name")
#     StudentFactory.create(specialization="specialization")
#     StudentFactory.create_batch(number_of_students)
#
#     re = client.get("/students/", query_string={"name": "name"})
#
#     assert re.status_code == 200
#     assert len(re.json) == number_of_expected_students
#
#
# def test_should_return_students_all_filtered_by_name_and_specialization(client):
#     number_of_expected_students = 1
#     number_of_students = 5
#     StudentFactory.create(name="name", specialization="specialization")
#     StudentFactory.create_batch(number_of_students)
#
#     re = client.get(
#         "/students/", query_string={"name": "name", "specialization": "specialization"}
#     )
#
#     assert re.status_code == 200
#     assert len(re.json) == number_of_expected_students
#
#
def test_should_create_student_and_return_status_code_201(client):
    student_data = factory.build(dict, FACTORY_CLASS=CreateUpdateStudentFactory)

    re = client.post(
        "/students/", json=student_data, headers={"content-type": "application/json"}
    )

    assert re.status_code == 201
    assert re.json["name"] == student_data["name"]
    assert re.json["surname"] == student_data["surname"]
    assert re.json["specialization"] == student_data["specialization"]

#
# def test_should_return_400_if_data_not_valid_on_create(client):
#     number_of_expected_errors = 3
#     test_value = 1
#     student_data = {
#         "name": test_value,
#         "surname": test_value,
#         "specialization": test_value,
#     }
#
#     re = client.post(
#         "/students/", json=student_data, headers={"content-type": "application/json"}
#     )
#
#     assert re.status_code == 400
#     assert len(re.json["errors"]) == number_of_expected_errors
#     assert re.json["errors"]["name"] == f"{test_value} is not of type 'string'"
#     assert re.json["errors"]["surname"] == f"{test_value} is not of type 'string'"
#     assert (
#         re.json["errors"]["specialization"] == f"{test_value} is not of type 'string'"
#     )
#
#
# def test_should_return_desired_student_details(client):
#     student = StudentFactory.create()
#
#     re = client.get(f"/students/{student.id}")
#
#     assert re.status_code == 200
#     assert student.name == re.json["name"]
#     assert student.surname == re.json["surname"]
#     assert student.specialization == re.json["specialization"]
#
#
# def test_should_return_200_and_update_student_info(client, update_student_data):
#     student = StudentFactory.create()
#
#     re = client.put(
#         f"/students/{student.id}",
#         json=update_student_data,
#         headers={"content-type": "application/json"},
#     )
#
#     assert re.status_code == 200
#     assert re.json["id"] == student.id
#     assert update_student_data["name"] == student.name
#     assert update_student_data["surname"] == student.surname
#     assert update_student_data["specialization"] == student.specialization
#
#
# def test_should_return_400_if_data_not_valid_on_update(client):
#     student = StudentFactory.create()
#     number_of_expected_errors = 3
#     test_value = 1
#     student_data = {
#         "name": test_value,
#         "surname": test_value,
#         "specialization": test_value,
#     }
#
#     re = client.put(
#         f"/students/{student.id}",
#         json=student_data,
#         headers={"content-type": "application/json"},
#     )
#
#     assert re.status_code == 400
#     assert len(re.json["errors"]) == number_of_expected_errors
#     assert re.json["errors"]["name"] == f"{test_value} is not of type 'string'"
#     assert re.json["errors"]["surname"] == f"{test_value} is not of type 'string'"
#     assert (
#         re.json["errors"]["specialization"] == f"{test_value} is not of type 'string'"
#     )
#
#
# def test_should_return_400_if_data_is_not_complited(client):
#     student = StudentFactory.create()
#     number_of_expected_errors = 1
#     student_data = {"name": "name", "specialization": "specialization"}
#
#     re = client.put(
#         f"/students/{student.id}",
#         json=student_data,
#         headers={"content-type": "application/json"},
#     )
#
#     assert re.status_code == 400
#     assert len(re.json["errors"]) == number_of_expected_errors
#     assert re.json["errors"]["surname"] == "'surname' is a required property"
#
#
# def test_should_return_404_if_student_not_exists(client):
#     fake_id = "c4bb0029-f4e2-436f-afd2-b3752b2b87be"
#
#     re = client.get(f"/students/{fake_id}")
#
#     assert re.status_code == 404
#
#
# def test_should_return_200_on_delete_when_student_exists(client):
#     student = StudentFactory.create()
#
#     re = client.delete(f"/students/{student.id}")
#
#     assert re.status_code == 200
#
#
# def test_should_return_200_on_delete_when_student_not_exists(client):
#     fake_id = "c4bb0029-f4e2-436f-afd2-b3752b2b87be"
#
#     re = client.delete(f"/students/{fake_id}")
#
#     assert re.status_code == 200
