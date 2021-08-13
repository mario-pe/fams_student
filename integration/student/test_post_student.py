import requests


def tests_should_return_status_code_201_and_create_students(create_student_data):
    response = requests.post("http://127.0.0.1:5000/student/", json=create_student_data)

    assert response.status_code == 201
    assert response.json()["name"] == create_student_data["name"]
    assert response.json()["surname"] == create_student_data["surname"]
    assert response.json()["specialization"] == create_student_data["specialization"]


def tests_should_return_status_code_400_if_data_is_corrupted(create_student_data):
    corrupted_data = create_student_data.pop("name")

    response = requests.post("http://127.0.0.1:5000/student/",json=corrupted_data)

    assert response.status_code == 400


