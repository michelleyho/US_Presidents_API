# models.py

from config import db, ma
from marshmallow_sqlalchemy import fields

class Note(db.Model):
    __tablename__ = "note"
    id = db.Column(db.Integer, primary_key=True)
    president_num = db.Column(db.Integer, db.ForeignKey("president.number"))
    content = db.Column(db.String, nullable=False)

class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Note
        load_instance = True
        sqla_session = db.session
        include_fk = True # include foreign key

class President(db.Model):
    __tablename__ = "president"
    number = db.Column(db.Integer, primary_key = True, unique = True)
    fname = db.Column(db.String(32))
    lname = db.Column(db.String(32))
    term_start = db.Column(db.Integer)
    term_end = db.Column(db.Integer)
    notes = db.relationship(Note, backref="president", cascade="all, delete, delete-orphan", single_parent=True)

class PresidentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = President
        load_instance = True
        sqla_session = db.session
        include_relationships = True
    notes = fields.Nested(NoteSchema, many=True)

president_schema = PresidentSchema()
presidents_schema = PresidentSchema(many=True)
note_schema = NoteSchema()

