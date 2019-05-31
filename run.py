""" Entry point of program """

from UTILS.structures import Job
from UTILS.structures import Queue
from UTILS.db import DB

from typing import Type
from flask import Flask
from flask import render_template

q: Type[Queue] = Queue()
db = DB()
conn = db.get_connection()

app = Flask(__name__, template_folder="templates")

def insert(name: str, faculty: int, role: int, status: int, desc: str):  # noqa
    job = Job(name, faculty, role, status, desc)
    index = job.todb()
    job.set_id(index)
    q.enqueue(job)


def update(id: int) -> None:
    job = q.pop()
    job.update(id)


@app.route("/")
def home(lang: str):
    cursor = conn.cursor()
    query = "SELECT "
    return "Ho! Ho! Ho!"


if __name__ == "__main__":
    app.run(debug=True)
