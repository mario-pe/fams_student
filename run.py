from flask import Flask
from flask_restx import Api
from gstudent.resources.student_resource import ns as student_api
from database import init_db

def create_app(config_path):
    app = Flask(__name__)
    app.config.from_object(config_path)
    db = init_db(app)
    api = Api(title="student_api", verison="0.1", description="Student manager")
    api.add_namespace(student_api)
    api.init_app(app)
    return app, db, api
