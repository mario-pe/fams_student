from flask_restx import Resource, reqparse
from flask_restx._http import HTTPStatus

from gstudent.models.student import Student
from gstudent.namespace_models import ns, student_create_update
from gstudent.namespace_models import student as student_model
from gstudent.services.student_service import StudentService

parser = reqparse.RequestParser()
parser.add_argument("name", location="args")
parser.add_argument("surname", location="args")
parser.add_argument("specialization", location="args")


@ns.route("/")
class StudentList(Resource):
    """Shows a list of all students, and lets you POST to add new student"""

    @ns.doc("list_students")
    @ns.marshal_list_with(student_model)
    def get(self, **kwargs):
        """List all students"""
        params = parser.parse_args()
        student_service = StudentService()
        students = student_service.get_students_list(params)
        return students

    @ns.doc("create_student")
    @ns.marshal_list_with(student_model)
    @ns.expect(student_create_update)
    def post(self):
        """Create a new student"""
        student_service = StudentService()
        student = Student(
            id=None,
            name=ns.payload["name"],
            surname=ns.payload["surname"],
            specialization=ns.payload["specialization"],
        )
        saved_student = student_service.create_student(student)
        return saved_student, 201


@ns.route("/<string:id>")
@ns.response(HTTPStatus.NOT_FOUND, HTTPStatus.NOT_FOUND.description)
@ns.response(HTTPStatus.BAD_REQUEST, HTTPStatus.BAD_REQUEST.description)
@ns.param("id", "The student identifier")
class StudentDetails(Resource):
    @ns.doc("get_student_by_id")
    @ns.response(HTTPStatus.NOT_FOUND, HTTPStatus.NOT_FOUND.description)
    @ns.marshal_with(student_model)
    def get(self, id):
        student_service = StudentService()
        student = student_service.get_student_details(id)
        if student:
            return student, 200
        else:
            return HTTPStatus.NOT_FOUND.description, 404


    @ns.doc("update_student_by_id")
    @ns.marshal_with(student_model)
    @ns.expect(student_create_update)
    def put(self, id):
        student_service = StudentService()
        student = Student(
            id=id,
            name=ns.payload["name"],
            surname=ns.payload["surname"],
            specialization=ns.payload["specialization"],
        )
        updated_student = student_service.update_student(student)
        if updated_student:
            return updated_student
        else:
            return HTTPStatus.NOT_FOUND.description, 404

    @ns.doc("delete_student_by_id")
    @ns.response(200, "Student deleted")
    def delete(self, id):
        student_service = StudentService()
        student_service.delete_student(id)
        return "", 200
