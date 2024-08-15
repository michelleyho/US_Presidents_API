from flask import abort

PRESIDENTS = {
    1: {
        "number": 1, 
        "fname": "George",
        "lname": "Washington", 
        "term_start": 1789, 
        "term_end": 1797,
    },
    2: {
        "number": 2, 
        "fname": "John",
        "lname": "Adams", 
        "term_start": 1797, 
        "term_end": 1801,
    },
    3: {
        "number": 3, 
        "fname": "Thomas",
        "lname": "Jefferson", 
        "term_start": 1801, 
        "term_end": 1809,
    },
    4: {
        "number": 4, 
        "fname": "James",
        "lname": "Madison", 
        "term_start": 1809, 
        "term_end": 1817,
    },
    5: {
        "number": 5, 
        "fname": "James",
        "lname": "Monroe", 
        "term_start": 1817, 
        "term_end": 1825,
    },
    6: {
        "number": 6, 
        "fname": "John",
        "lname": "Quincy", 
        "term_start": 1825, 
        "term_end": 1829,
    },
}

def read_all():
    return list(PRESIDENTS.values())

def create(president):
    number = president.get("number")
    fname = president.get("fname")
    lname = president.get("lname")
    term_start = president.get("term_start")
    term_end = president.get("term_end")

    if number and number not in PRESIDENTS:
        PRESIDENTS[number] = {
            "number": number, 
            "fname": fname, 
            "lname": lname,
            "term_start": term_start,
            "term_end": term_end,

        }
        return PRESIDENTS[number], 201
    else:
        abort(406, f"President Number:{number} already exists")

def read_one(number):
    if number in PRESIDENTS:
        return PRESIDENTS[number]
    else:
        abort(404, f"President number:{number} not found")

def read_one_by_full_name(full_name):
    for president in PRESIDENTS.values():
        if full_name == f"{president['fname']}_{president['lname']}":
            return president
    
    abort(404, f"President: {full_name} not found")
