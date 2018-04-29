from flask import Flask, request, render_template, jsonify
from .models import User,Course
from random import *
app = Flask(__name__)

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
        response = Course(courseID).loadCourseData();
    except:
        print("Load Course Data Error!")
    return jsonify(response)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
