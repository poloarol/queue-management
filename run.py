""" Entry point of program """

from UTILS.structures import Job
# from UTILS.structures import Queue
from UTILS.db import DB
from UTILS.forms import RegistrationForm

from typing import Tuple
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

# q: Type[Queue] = Queue()
db = DB()
conn = db.get_connection()
job = None

app = Flask(__name__, template_folder="templates")

def insert(name: str, faculty: int, role: int, status: int, desc: str):  # noqa
    job = Job(name, faculty, role, status, desc)
    index = job.todb()
    job.set_id(index)
    # q.enqueue(job)


@app.route("/", methods=['GET', 'POST'])
def home(lang: str):
    form = RegistrationForm()
    if request.method == 'GET':
        cursor = conn.cursor()
        value: int = 1 if lang == 'EN' else '2'
        fa: str = "SELECT FACULTY.NAMES FROM FACULTY WHERE FACULTY.LANG = (%s);"  # noqa
        rl: str = "SELECT ROLES.NAMES FROM ROLES WHERE ROLES.LANG = (%s); "
        st: str = "SELECT STATUS.NAMES FROM STATUS WHERE STATUS.LANG = (%s); "
        fty: Tuple = cursor.execute(fa, (value))
        rl: Tuple = cursor.execute(rl, (value))
        ss: Tuple = cursor.execute(st, (value))
        conn.commit()
        return render_template('index.html', fty=fty, rl=rl, ss=ss, form=form)
    else:
        name = form.name.data
        fty = form.fty.data
        rl = form.rl.data
        ss = form.ss.data
        desc = form.desc.data
        insert(name, fty, rl, ss, desc)
        return redirect("https://www.uottawa.ca/en/employees", code=302)


@app.route("/waitlist", methods=["GET"])
def waitlist(lang: str):
    value: int = 1 if lang == 'EN' else '2'
    results: Tuple = get_data(value)
    return render_template('waitlist.html', res=results)


@app.route("/admin/waitlist", methods=["GET", "PUT"])
def update_waitlist(id: int, lang: str) -> None:
    value: int = 1 if lang == 'EN' else '2'
    job.update(id)
    results: Tuple = get_data(value)
    return render_template('admin_waitlist.html', res=results)


def get_data(value: int):
    cursor = conn.cursor()
    query = "SELECT JOB.NAME, FACULTY.NAMES FROM JOB \
                INNER JOIN FACULTY ON JOB.FACULTY_ID = FACULTY.ID \
                WHERE JOB.COMPLETE = FALSE AND FACULTY.LANG = (%s) \
                AND JOB.TODAY::date = NOW() ORDER BY TODAY DESC;"
    results: Tuple = cursor.execute(query, (value))
    conn.commit()
    return results


if __name__ == "__main__":
    app.run(debug=True)
