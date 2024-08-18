# notes.py

from flask import abort, make_response

from config import db
from models import Note, note_schema, President

def read_one(note_id):
    note = Note.query.get(note_id)

    if note is not None:
        return note_schema.dump(note)
    else:
        abort(404, f"Note with ID {note_id} not found")

def update(note_id, new_note):
    existing_note = Note.query.get(note_id)
    if existing_note:
        update_note = note_schema.load(new_note, session=db.session)
        existing_note.content = update_note.content
        db.session.merge(existing_note)
        db.session.commit()
        return note_schema.dump(existing_note), 201
    else:
        abort(404, f"Note with ID: {note_id} not found")

def delete(note_id):
    existing_note = Note.query.get(note_id)
    if existing_note:
        db.session.delete(existing_note)
        db.session.commit()
        return make_response(f"Note with id: {note_id} successfuly removed"), 204
    else:
        abort(404, f"Note with ID: {note_id} not found")

def create(note):
    president_num = note.get("president_num")
    president = President.query.get(president_num)

    if president:
        new_note = note_schema.load(note, session=db.session)
        president.notes.append(new_note)
        db.session.commit()

        return note_schema.dump(new_note), 201
    else:
        abort(404, f"President #:{president_num} not found")
