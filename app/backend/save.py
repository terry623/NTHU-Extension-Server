from pymongo import MongoClient
client = MongoClient('192.168.99.100:32768')
db = client.nthuCourse_database
userGrades = db.userGrade_collection
keywords = db.keyword_collection


def toSaveUserGrade(stu_no, userGrade):
    resultID = userGrades.insert_one(
        {'stu_no': stu_no, 'userGrade': userGrade}).inserted_id
    response = {'message': 'Save Grade Success!'}

    return response


def toSaveKeyword(stu_no, search_topic, keyword, other_keyword)
    resultID = keywords.insert_one(
        {'stu_no': stu_no, 'topic': search_topic, 'keyword': keyword, 'other_keyword': other_keyword}).inserted_id
    response = {'message': 'Save Keyword Success!'}

    return response
