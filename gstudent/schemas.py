from marshmallow import Schema, fields


class StudentSchema(Schema):
    uuid = fields.UUID()
    name = fields.String()
    surname = fields.String()
    specialization = fields.String()


class StudentUpdateSchema(Schema):
    name = fields.String()
    surname = fields.String()
    specialization = fields.String()


student_schema = StudentSchema()
student_schemas = StudentSchema(many=True)
student_update_schema = StudentUpdateSchema()
student_update_schemas = StudentUpdateSchema(many=True)
