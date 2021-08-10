import uuid as uuid

from database import db
from sqlalchemy.dialects.postgresql import UUID


class StudentEntity(db.Model):
    __tablename__ = "student"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(120), nullable=False)
    specialization = db.Column(db.String(120), nullable=False)
