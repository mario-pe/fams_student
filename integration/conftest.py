import uuid

import pytest
import requests


@pytest.fixture()
def unique_key():
    return str(uuid.uuid4())


@pytest.fixture
def update_student_data(unique_key):
    return {
        "name": "new_name",
        "surname": "new_surname",
        "specialization": "new_specialization",
    }


@pytest.fixture
def create_student_data(unique_key):
    return {
        "name": f"name_{unique_key}",
        "surname": "test_surname",
        "specialization": "test_specialization",
    }


@pytest.fixture
def create_student(create_student_data):
    response = requests.post(url=" http://127.0.0.1:5000/student/", json=create_student_data)
    return response.json()


@pytest.fixture
def create_student_with_math_specialization(create_student_data):
    create_student_data["specialization"] = "math"
    response = requests.post(url=" http://127.0.0.1:5000/student/", json=create_student_data)
    return response.json()
