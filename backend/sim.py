import pandas as pd


def loadDataFromSIM(course_id):

    all_other_course = pd.read_pickle(
        'data/course_similarities')[int(course_id)]
    result = all_other_course.sort_values(ascending=False).iloc[0:10]

    response = [{'c_id': c_id, 'percent': percent}
                for c_id, percent in zip(result.index.tolist(), result.tolist())]

    return response
