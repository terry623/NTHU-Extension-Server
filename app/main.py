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
        print('Get Current State Of NTHU Error!')
    return jsonify(response)


@app.route('/api/getSimilarities', methods=['GET'])
def getSimilarities():
    course_id = request.args.get('course_id')
    try:
        response = loadDataFromFile(course_id)
        # print(response)
    except:
        print('Get Similarities Error!')
    return jsonify(response)


@app.route('/api/searchOnlyKeyword', methods=['POST'])
def searchOnlyKeyword():
    stu_no = request.form['stu_no']
    search_topic = request.form['search_topic']
    keyword = request.form['keyword']
    try:
        response = toSearchOnlyKeyword(stu_no, search_topic, keyword)
        # print(response)
    except:
        print('Search Only Keyword Error!')
    return jsonify(response)


@app.route('/api/searchDoubleKeyword', methods=['POST'])
def searchDoubleKeyword():
    stu_no = request.form['stu_no']
    search_topic = request.form['search_topic']
    keyword = request.form['keyword']
    other_keyword = request.form['other_keyword']
    try:
        response = toSearchDoubleKeyword(
            stu_no, search_topic, keyword, other_keyword)
        # print(response)
    except:
        print('Search Double Keyword Error!')
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
        print('Search Time Error!')
    return jsonify(response)


@app.route('/api/searchBySingleCourseNo', methods=['POST'])
def searchBySingleCourseNo():
    course_no = request.form['course_no']
    try:
        response = toSearchBySingleCourseNo(course_no)
        # print(response)
    except:
        print('Search By Single CourseNo Error!')
    return jsonify(response)


@app.route('/api/searchByID_Group', methods=['POST'])
def searchByID_Group():
    id_0 = request.form['id_0']
    id_1 = request.form['id_1']
    id_2 = request.form['id_2']
    try:
        response = toSearchByID_Group(id_0, id_1, id_2)
        course_no = request.form['course_no']
        # print(response)
    except:
        print('Search By ID Group Error!')
    return jsonify(response)


@app.route('/api/saveUserGrade', methods=['POST'])
def saveUserGrade():
    stu_no = request.form['stu_no']
    userGrade = json.loads(request.form['userGrade'])
    print(stu_no)
    print(userGrade)
    try:
        response = toSaveUserGrade(stu_no, userGrade)
    except:
        print('Save User Grade Error!')
    return jsonify(response)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    index_path = os.path.join(app.static_folder, 'index.html')
    return send_file(index_path)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=8080)
