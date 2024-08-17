from config import app, db
from models import President, Note

PRESIDENT_NOTES = [
    {
        "fname": "George", 
        "lname": "Washington", 
        "number": 1, 
        "term_start": 1789, 
        "term_end": 1797, 
        "notes": [
            ("Election Year: 1788-1789"),
            ("Election Year: 1792"),
            ("Party: Unaffiliated"),
        ],
    },    
    {
        "fname": "John", 
        "lname": "Adams", 
        "number": 2, 
        "term_start": 1797, 
        "term_end": 1801, 
        "notes": [
            ("Election Year: 1796"),
            ("Party: Federalist"),
        ],
    },    
    {
        "fname": "Thomas", 
        "lname": "Jefferson", 
        "number": 3, 
        "term_start": 1801, 
        "term_end": 1809, 
        "notes": [
            ("Election Year: 1800"),
            ("Election Year: 1801"),
            ("Party: Democratic-Republican"),
        ],
    },    
    {
        "fname": "James", 
        "lname": "Madison", 
        "number": 4, 
        "term_start": 1809, 
        "term_end": 1817, 
        "notes": [
            ("Election Year: 1808"),
            ("Election Year: 1812"),
            ("Party: Democratic-Republican"),
        ],
    },    
    {
        "fname": "James", 
        "lname": "Monroe", 
        "number": 5, 
        "term_start": 1817, 
        "term_end": 1825, 
        "notes": [
            ("Election Year: 1816"),
            ("Election Year: 1820"),
            ("Party: Democratic Republican"),
        ],
    },    
]

with app.app_context():
    db.drop_all()
    db.create_all()
    for data in PRESIDENT_NOTES:
        new_president = President(fname=data.get("fname"), lname=data.get("lname"), 
                                  number=data.get("number"), 
                                  term_start=data.get("term_start"), term_end=data.get("term_end"))
        for content in data.get("notes", []):
            new_president.notes.append(Note(content=content))

        db.session.add(new_president)
    db.session.commit()

