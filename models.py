# models.py

from config import db, ma

class President(db.Model):
    __tablename__ = "president"
    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(32))
    lname = db.Column(db.String(32))
    number = db.Column(db.Integer, unique = True)
    term_start = db.Column(db.Integer)
    term_end = db.Column(db.Integer)


class PresidentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = President
        load_instance = True
        sqla_session = db.session

president_schema = PresidentSchema()
presidents_schema = PresidentSchema(many=True)

