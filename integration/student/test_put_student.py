import uuid

import requests


def tests_should_return_status_code_200_and_update_students(create_student, update_student_data):
    student_id = create_student["id"]

    response = requests.put(f"http://127.0.0.1:5000/student/{student_id}",json=update_student_data)

    assert response.status_code == 200
    assert response.json()["name"] == update_student_data["name"]
    assert response.json()["surname"] == update_student_data["surname"]
    assert response.json()["specialization"] == update_student_data["specialization"]


def tests_should_return_status_code_400(create_student, update_student_data):
    student_id = create_student["id"]
    corrupted_data = update_student_data.pop("name")

    response = requests.put(f"http://127.0.0.1:5000/student/{student_id}", json=corrupted_data)

    assert response.status_code == 400


def tests_put_student_when_not_exists_returns_404(update_student_data):
    fake_id = uuid.uuid4()

    response = requests.put(f"http://127.0.0.1:5000/student/{fake_id}", json=update_student_data)

    assert response.status_code == 404
