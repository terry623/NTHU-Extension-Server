import os
import json
from flask import Flask, request, render_template, jsonify, send_file
from datetime import date
from backend.models import loadDataFromFile
from backend.search import toSearchOnlyKeyword, toSearchDoubleKeyword, toSearchBySingleCourseNo, toSearchByID_Group, toSearchTime
from backend.days import getCountDown, getCurrentPhase
from backend.save import toSaveUserGrade
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={'/api/*': {'origins': '*'}})


@app.route('/api/getCurrentStateOfNTHU', methods=['GET'])
def getCurrentStateOfNTHU():
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')
    today = date(int(year), int(month), int(day))
    try:
        currentphase = getCurrentPhase(today)
        countdown = getCountDown(today)
        response = {
            'currentPhase': currentphase,
            'countDown': countdown
        }
        # print(response)
    except:
        message = 'Get Current State Of NTHU Error!'
        print(message)
        response = {'message': message}
    return jsonify(response)


@app.route('/api/getSimilarities', methods=['GET'])
def getSimilarities():
    course_id = request.args.get('course_id')
    try:
        response = loadDataFromFile(course_id)
        # print(response)
    except:
        message = 'Get Similarities Error!'
        print(message)
        response = {'message': message}
    return jsonify(response)


@app.route('/api/searchOnlyKeyword', methods=['POST'])
def searchOnlyKeyword():
    search_topic = request.form['search_topic']
    keyword = request.form['keyword']
    try:
        response = toSearchOnlyKeyword(search_topic, keyword)
        # print(response)
    except:
        message = 'Search Only Keyword Error!'
        print(message)
        response = {'message': message}
    return jsonify(response)


@app.route('/api/searchDoubleKeyword', methods=['POST'])
def searchDoubleKeyword():
    search_topic = request.form['search_topic']
    keyword = request.form['keyword']
    other_keyword = request.form['other_keyword']
    try:
        response = toSearchDoubleKeyword(search_topic, keyword, other_keyword)
        # print(response)
    except:
        message = 'Search Double Keyword Error!'
        print(message)
        response = {'message': message}
    return jsonify(response)


@app.route('/api/searchTime', methods=['POST'])
def searchTime():
    search_topic = request.form['search_topic']
    keyword = request.form['keyword']
    time_group = json.loads(request.form['time_group'])
    print(time_group)
    try:
        response = toSearchTime(search_topic, keyword, time_group)
        # print(response)
    except:
        message = 'Search Time Error!'
        print(message)
        response = {'message': message}
    return jsonify(response)


@app.route('/api/searchBySingleCourseNo', methods=['POST'])
def searchBySingleCourseNo():
    course_no = request.form['course_no']
    try:
        response = toSearchBySingleCourseNo(course_no)
        # print(response)
    except:
        message = 'Search By Single CourseNo Error!'
        print(message)
        response = {'message': message}
    return jsonify(response)


@app.route('/api/searchByID_Group', methods=['POST'])
def searchByID_Group():
    id_0 = request.form['id_0']
    id_1 = request.form['id_1']
    id_2 = request.form['id_2']
    try:
        response = toSearchByID_Group(id_0, id_1, id_2)
        # print(response)
    except:
        message = 'Search By ID Group Error!'
        print(message)
        response = {'message': message}
    return jsonify(response)


@app.route('/api/saveUserGrade', methods=['POST'])
def saveUserGrade():
    userGrade = json.loads(request.form['userGrade'])
    print(userGrade)
    try:
        response = toSaveUserGrade(userGrade)
    except:
        message = 'Save User Grade Error!'
        print(message)
        response = {'message': message}
    return jsonify(response)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    index_path = os.path.join(app.static_folder, 'index.html')
    return send_file(index_path)
