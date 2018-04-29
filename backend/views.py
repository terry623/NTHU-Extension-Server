from flask import Flask, request, render_template, jsonify
from .models import User, Course
from flask_cors import CORS
from random import *
app = Flask(__name__)
cors = CORS(app, resources={"/api/*": {"origins": "*"}})


@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    user1 = data['user1']
    user2 = data['user2']

    try:
        User(user1).add_people(user2)
        response = {'status': 'Good Job!'}
    except:
        print("Register Error!")
        response = {'status': 'No~~'}
    return jsonify(response)


@app.route('/api/loadCourseData', methods=['POST'])
def loadCourseData():
    data = request.get_json()
    courseID = data['courseID']

    try:
        response = Course(courseID).loadCourseData()
    except:
        print("Load Course Data Error!")
    return jsonify(response)


@app.route('/api/calculateUserGrade', methods=['POST'])
def calculateUserGrade():
    # data = request.get_json()
    print(request.form['stu_no'])
    print(request.form['userGrade'])

    try:
        # response = Course(courseID).loadCourseData()
        response = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    except:
        print("Calculate User Grade Error!")
    return jsonify(response)


@app.route('/api/collectGradeDistribution', methods=['POST'])
def collectGradeDistribution():
    # data = request.get_json()
    print(request.form['course_no'])
    print(request.form['distribution'])

    try:
        # response = Course(courseID).loadCourseData()
        response = {'a': 6, 'b': 7, 'c': 8, 'd': 9, 'e': 10}
    except:
        print("Collect Grade Distribution Error!")
    return jsonify(response)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
