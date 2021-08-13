import uuid

import requests


def tests_get_student_returns_200_when_exists(create_student):
    student_id = create_student["id"]

    response = requests.get(f"http://127.0.0.1:5000/student/{student_id}")

    assert response.status_code == 200
    assert response.json()["name"] == create_student["name"]
    assert response.json()["surname"] == create_student["surname"]
    assert response.json()["specialization"] == create_student["specialization"]


def tests_get_student_when_not_exists_returns_404(update_student_data):
    fake_id = uuid.uuid4()

    response = requests.get(f"http://127.0.0.1:5000/student/{fake_id}")

    assert response.status_code == 404
