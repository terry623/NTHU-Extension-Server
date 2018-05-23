from flask import Flask, request, render_template, jsonify
from .models import Course
from .days import getCountDown, getCurrentPhase
from flask_cors import CORS
from datetime import date
from random import *
import json
app = Flask(__name__)
cors = CORS(app, resources={'/api/*': {'origins': '*'}})


@app.route('/api/getSimilarities', methods=['GET'])
def getSimilarities():
    course_id = request.args.get('course_id')
    try:
        result = Course(course_id).findRelationship()
        response = result.data()
    except:
        print('Get Similarities Error!')
    return jsonify(response)


@app.route('/api/getCurrentStateOfNTHU', methods=['GET'])
def getCurrentStateOfNTHU():
    try:
        currentphase = getCurrentPhase()
        countdown = getCountDown()
        response = {
            'currentPhase': currentphase,
            'countDown': countdown
        }
    except:
        print('Get Current State Of NTHU Error!')
    return jsonify(response)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')
