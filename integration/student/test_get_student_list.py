import requests

from integration.assertions import assert_if_desired_param_is_equal_to_objects_fields_in_list


def tests_get_list_of_students_returns_200(create_student):
    student_data = create_student

    response = requests.get("http://127.0.0.1:5000/student/")
    student_from_response = next(
        (c for c in response.json() if c['id'] == student_data['id']), None
    )

    assert response.status_code == 200
    assert student_from_response != None
    assert student_data["name"] == student_from_response["name"]
    assert student_data["surname"] == student_from_response["surname"]
    assert student_data["specialization"] == student_from_response["specialization"]


def test_get_return_students_filtered_by_name(create_student):
    student_data = create_student

    response = requests.get(f"http://127.0.0.1:5000/student/", params={"name": student_data["name"]})

    assert response.status_code == 200
    assert_if_desired_param_is_equal_to_objects_fields_in_list(response.json(), "name", student_data["name"])


def test_get_should_return_fitered_students_by_multiple_params(create_student):
    student_data = create_student

    response = requests.get(f"http://127.0.0.1:5000/student/", params={"name": student_data["name"], "surname": student_data["surname"]})

    assert response.status_code == 200
    assert_if_desired_param_is_equal_to_objects_fields_in_list(response.json(), "name", student_data["name"])
    assert_if_desired_param_is_equal_to_objects_fields_in_list(response.json(), "surname", student_data["surname"])
