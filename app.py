from flask import Flask
from Lupu import books
import json

app = Flask("Biblioteca")
temp = []


@app.route("/")
def data_book():
    return json.dumps([book.__dict__ for book in books])