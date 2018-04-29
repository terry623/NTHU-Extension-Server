from flask import Flask, request, render_template, jsonify
from .models import User, Course
from flask_cors import CORS
from random import *
import json
app = Flask(__name__)
cors = CORS(app, resources={'/api/*': {'origins': '*'}})


@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    user1 = data['user1']
    user2 = data['user2']

    try:
        User(user1).add_people(user2)
        response = {'status': 'Good Job!'}
    except:
        print('Register Error!')
        response = {'status': 'No~~'}
    return jsonify(response)


@app.route('/api/loadCourseData', methods=['POST'])
def loadCourseData():
    data = request.get_json()
    courseID = data['courseID']

    try:
        response = Course(courseID).loadCourseData()
    except:
        print('Load Course Data Error!')
    return jsonify(response)


@app.route('/api/calculateUserGrade', methods=['POST'])
def calculateUserGrade():
    # print(request.form['stu_no'])
    # print(json.loads(request.form['userGrade']))

    try:
        # response = Course(courseID).loadCourseData()
        response = {'message': 'I receive your grade ~'}
    except:
        print('Calculate User Grade Error!')
    return jsonify(response)


@app.route('/api/collectionOfCourse', methods=['GET'])
def collectionOfCourse():
    try:
        # response = Course(courseID).loadCourseData()
        response = {'message': '999'}
    except:
        print('All Course Name Error!')
    return jsonify(response)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')

# JS 的抓取成績分佈，要把它改成從 Server 這邊抓
# function getGradeDistribution(acix, course_no) {
#   request(
#     {
#       url:
#         'https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/JH/8/8.3/8.3.3/JH83302.php?ACIXSTORE=' +
#         acix +
#         '&c_key=' +
#         course_no +
#         '&from=prg8R63',
#       encoding: null
#     },
#     function(err, response, body) {
#       if (!err && response.statusCode == 200) {
#         var str = iconv.decode(new Buffer(body), 'big5');
#         var temp = document.createElement('div');
#         temp.innerHTML = str;
#         // console.log.apply(console, $(temp));

#         var gradeDistributionOfCourse = $(
#           'form > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td',
#           temp
#         );

#         var gradeDistributionMap = new Map();
#         $(gradeDistributionOfCourse).each(function(index) {
#           if (index > 0) {
#             var grade = $(this).text();
#             var words = grade.split('%');
#             var num = 0;
#             var patt = /\d+/;

#             if (words[1] != undefined) num = words[1].match(patt);
#             gradeDistributionMap.set(index, num);
#           }
#         });

#         console.log('Get Grade Distribution...\n');
#         for (var [key, value] of gradeDistributionMap) {
#           console.log(key + ' : ' + value);
#         }
#       }
#     }
#   );
# }
