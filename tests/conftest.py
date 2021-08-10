import pytest
from run import create_app
from manage import create_test_db


@pytest.fixture
def client():
    """Creating test application"""
    app, db, _ = create_app("test_settings")
    with app.test_client() as client:
        with app.app_context():
            create_test_db(app, db)
        yield client
    db.close_all_sessions()
    return app


@pytest.fixture
def update_student_data():
    return {
        "name": "test_name",
        "surname": "test_surname",
        "specialization": "test_specialization",
    }
