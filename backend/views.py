from flask import Flask, request, render_template, jsonify
# from .models import Course
# from .days import getCountDown, getCurrentPhase
# from .search import toSearchOnlyKeyword, toSearchDoubleKeyword, toSearchBySingleCourseNo, toSearchByID_Group
from flask_cors import CORS
from datetime import date
from random import *
import json
app = Flask(__name__)
cors = CORS(app, resources={'/api/*': {'origins': '*'}})


@app.route('/api/testAWS', methods=['GET'])
def testAWS():
    try:
        response = "Please Success !"
    except:
        print('Test AWS Error!')
    return response

# @app.route('/api/getSimilarities', methods=['GET'])
# def getSimilarities():
#     course_id = request.args.get('course_id')
#     try:
#         result = Course(course_id).findRelationship()
#         response = result.data()
#     except:
#         print('Get Similarities Error!')
#     return jsonify(response)


# @app.route('/api/getCurrentStateOfNTHU', methods=['GET'])
# def getCurrentStateOfNTHU():
#     try:
#         currentphase = getCurrentPhase()
#         countdown = getCountDown()
#         response = {
#             'currentPhase': currentphase,
#             'countDown': countdown
#         }
#     except:
#         print('Get Current State Of NTHU Error!')
#     return jsonify(response)


# @app.route('/api/searchOnlyKeyword', methods=['GET'])
# def searchOnlyKeyword():
#     search_topic = request.args.get('search_topic')
#     keyword = request.args.get('keyword')
#     try:
#         response = toSearchOnlyKeyword(search_topic, keyword)
#         # print(response)
#     except:
#         print('Search Only Keyword Error!')
#     return jsonify(response)


# @app.route('/api/searchDoubleKeyword', methods=['GET'])
# def searchDoubleKeyword():
#     search_topic = request.args.get('search_topic')
#     keyword = request.args.get('keyword')
#     other_keyword = request.args.get('other_keyword')
#     try:
#         response = toSearchDoubleKeyword(search_topic, keyword, other_keyword)
#         # print(response)
#     except:
#         print('Search Double Keyword Error!')
#     return jsonify(response)


# @app.route('/api/searchBySingleCourseNo', methods=['GET'])
# def searchBySingleCourseNo():
#     course_no = request.args.get('course_no')
#     try:
#         response = toSearchBySingleCourseNo(course_no)
#         # print(response)
#     except:
#         print('Search By Single CourseNo Error!')
#     return jsonify(response)


# @app.route('/api/searchByID_Group', methods=['GET'])
# def searchByID_Group():
#     id_0 = request.args.get('id_0')
#     id_1 = request.args.get('id_1')
#     id_2 = request.args.get('id_2')
#     try:
#         response = toSearchByID_Group(id_0, id_1, id_2)
#         # print(response)
#     except:
#         print('Search By ID Group Error!')
#     return jsonify(response)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')
