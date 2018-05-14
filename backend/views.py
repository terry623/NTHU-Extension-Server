from flask import Flask, request, render_template, jsonify
from .models import Course
from flask_cors import CORS
from random import *
import json
app = Flask(__name__)
cors = CORS(app, resources={'/api/*': {'origins': '*'}})


@app.route('/api/calculateUserGrade', methods=['POST'])
def calculateUserGrade():
    # print(request.form['stu_no'])
    # print(json.loads(request.form['userGrade']))

    try:
        response = {'message': 'I receive your grade ~'}
    except:
        print('Calculate User Grade Error!')
    return jsonify(response)


@app.route('/api/getSimilarities', methods=['GET'])
def getSimilarities():
    course_id = request.args.get('course_id')
    try:
        result = Course(course_id).findRelationship()
        response = result.data()
    except:
        print('Get Similarities Error!')
    return jsonify(response)


@app.route('/api/getNewsFromServer', methods=['GET'])
def getNewsFromServer():
    try:
        response = [
            {
                'time': 'Today at 5: 42PM',
                'message': '快要選課了啦嗚嗚'
            },
            {
                'time': 'Yesterday at 12:30AM',
                'message': '大家要記得選課歐'
            },
            {
                'time': '5 days ago',
                'message': '不要忘記了啦'
            },
            {
                'time': '7 days ago',
                'message': '在幹嘛 = ='
            },
            {
                'time': '11 days ago',
                'message': '你這個垃圾'
            }
        ]
    except:
        print('Get News From Server Error!')
    return jsonify(response)


@app.route('/api/getCurrentPhase', methods=['GET'])
def getCurrentPhase():
    # 0  第 1 次選課
    # 1  第 1 次選課 log 記錄
    # 2  第 1 次選課亂數結果
    # 3  第 2 次選課
    # 4  第 2 次選課 log 記錄
    # 5  第 2 次選課結束(已亂數處理)
    # 6  第 3 次選課
    # 7  第 3 次選課 log 記錄
    # 8  第 3 次選課結束(已亂數處理)
    # 9 加退選開始前(含擋修、衝堂)
    # 10 加退選 log 記錄
    # 11 加退選結束(已處理)
    # 12 停修 log 記錄
    try:
        response = {'currentPhase': '5'}
    except:
        print('Get Current Phase Error!')
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
