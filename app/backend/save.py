from pymongo import MongoClient
import os
account = os.environ["MONGO_ACCOUNT"]
password = os.environ["MONGO_PASSWORD"]
client = MongoClient('mongodb+srv://' + account + ':' + password +
                     '@cluster0-hptar.gcp.mongodb.net/test?retryWrites=true')
db = client.nthuCourse_database
userGrades = db.userGrade_collection
keywords = db.keyword_collection


def toSaveUserGrade(stu_no, userGrade):
    resultID = userGrades.insert_one(
        {'stu_no': stu_no, 'userGrade': userGrade}).inserted_id
    response = {'message': 'Save Grade Success!'}

    return response


def toSaveKeyword(stu_no, search_topic, keyword, other_keyword):
    resultID = keywords.insert_one(
        {'stu_no': stu_no, 'topic': search_topic, 'keyword': keyword, 'other_keyword': other_keyword}).inserted_id
    response = {'message': 'Save Keyword Success!'}

    return response
