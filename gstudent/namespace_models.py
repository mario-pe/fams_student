from flask_restx import Namespace, fields

ns = Namespace("students", description="students operations")

student = ns.model(
    "Student",
    {
        "id": fields.String(
            required=True,
            pattern="^[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$",
            description="The student identifier",
        ),
        "name": fields.String(required=True, description="The student name"),
        "surname": fields.String(required=True, description="The student surname"),
        "specialization": fields.String(
            required=True, description="The student specialization"
        ),
    },
)
student_create_update = ns.model(
    "Student",
    {
        "name": fields.String(required=True, description="The student name"),
        "surname": fields.String(required=True, description="The student surname"),
        "specialization": fields.String(
            required=True, description="The student specialization"
        ),
    },
)
