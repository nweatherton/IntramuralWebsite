from flask import Blueprint, render_template
from .db import get_db #this is here to test db works

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/login")
def login():
    return render_template("login.html")

@bp.route("/testdata")
def testdata():
    rows = get_db().execute(
        "SELECT * FROM test_table"
    ).fetchall()
    return {"test data": [dict(r) for r in rows]}