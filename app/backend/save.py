# from pymongo import MongoClient
# import os
# account = os.environ["MONGO_ROLE_ACCOUNT"]
# password = os.environ["MONGO_ROLE_PASSWORD"]
# client = MongoClient('mongodb+srv://' + account + ':' + password +
#                      '@cluster0-hptar.gcp.mongodb.net/test?retryWrites=true')

# db = client['nthuCourse_database']
# userGrades = db['userGrade_collection']
# keywords = db['keyword_collection']


def toSaveUserGrade(userGrade):
    # resultID = userGrades.insert_one({'userGrade': userGrade}).inserted_id
    # response = {'message': 'Save Grade Success!'}

    # return response
    return


def toSaveKeyword(search_topic, keyword, other_keyword):
    # resultID = keywords.insert_one(
    #     {'topic': search_topic, 'keyword': keyword, 'other_keyword': other_keyword}).inserted_id
    # response = {'message': 'Save Keyword Success!'}

    # return response
    return
