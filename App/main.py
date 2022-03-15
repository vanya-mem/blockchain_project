from flask import Flask
from flask import render_template, url_for, redirect
from flask import request
from blockchain_script import *
from student_list import *

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        student = request.form['student']
        lesson = request.form['lesson']
        mark = request.form['mark']
        date = request.form['date']
        add_student(student)

        write_block(student, lesson, mark, date)
        return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/check', methods=['GET'])
def check_info():
    student_folder = get_info()
    results = block_check(student_folder)
    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)