from flask import Flask
from flask_restx import Api

from database import init_db


def create_app():
    from gstudent.resources.student_resource import ns as student_api
    app = Flask(__name__)
    app.config.from_object("settings")
    api = Api(title="student_api", verison="0.1", description="Student manager")
    api.init_app(app)
    api.add_namespace(student_api)
    db = init_db(app)
    return app, api, db

app, api, db = create_app()

if __name__ == '__main__':
    app.run(debug=True)