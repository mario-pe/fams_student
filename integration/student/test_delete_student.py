import uuid

import requests


def tests_delete_student_when_exists_returns_200(create_student):
    student_id = create_student["id"]

    response = requests.delete(f"http://127.0.0.1:5000/student/{student_id}")

    assert response.status_code == 200


def tests_delete_student_when_not_exists_returns_200():
    fake_id = uuid.uuid4()

    response = requests.delete(f"http://127.0.0.1:5000/student/{fake_id}")

    assert response.status_code == 200
