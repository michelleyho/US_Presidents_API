from flask import abort, make_response
from config import db
from models import President, president_schema, presidents_schema

def read_all():
    presidents = President.query.all()
    return presidents_schema.dump(presidents)
    #return list(PRESIDENTS.values())

def read_one(number):
    president = President.query.filter(President.number == number).one_or_none()
    
    if president is not None:
        return president_schema.dump(president)
    else:
        abort(404, f"President number:{number} not found")

def read_one_by_full_name(full_name):
    first_last_name = full_name.split("_")
    president = President.query.filter(President.fname == first_last_name[0], President.lname == first_last_name[1]).one_or_none()

    if president is not None:
        return president_schema.dump(president)

    abort(404, f"President: {full_name} not found")

def create(president):
    number = president.get("number")
    existing_president = President.query.filter(President.number == number).one_or_none()

    if existing_president is None:
        new_president = president_schema.load(president, session=db.session)
        db.session.add(new_president)
        db.session.commit()

        return president_schema.dump(new_president), 201
    else:
        abort(406, f"President Number:{number} already exists")


def update(number, president):
    existing_president = President.query.filter(President.number == number).one_or_none()
    if existing_president:
        update_president = president_schema.load(president, session=db.session)
        existing_president.fname = update_president.fname
        existing_president.lname = update_president.lname
        existing_president.number = update_president.number
        existing_president.term_start = update_president.term_start
        existing_president.term_end  = update_president.term_end

        db.session.merge(existing_president)
        db.session.commit()

        return president_schema.dump(existing_president), 201

    else:
        abort(404, f"President #{number} not found")

def delete(number):
    existing_president = President.query.filter(President.number == number).one_or_none()

    if existing_president:
        db.session.delete(existing_president)
        db.session.commit()
        return make_response(f"President #{number} successfully deleted", 200)
    else:
        abort(404, f"President #{number} not found")
