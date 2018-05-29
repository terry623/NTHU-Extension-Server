# import os
# from py2neo import Graph, Node, Relationship
# from .graph import graph
import pandas as pd


# class Course:
#     def __init__(self, course_id):
#         self.course_id = course_id

#     def findRelationship(self):
#         # print("Find The Relationship Of", self.course_id)
#         query = '''
#         MATCH (a:Course { course_id: toInt({c_id}) } )<-[r]-(b:Course)
#         WITH {
#             other: b.course_id,
#             percent: r.percent
#         } AS sim
#         RETURN sim
#         ORDER BY sim.percent DESC
#         LIMIT 10
#         '''

#         return graph.run(query, c_id=self.course_id)


def loadDataFromFile(course_id):

    all_other_course = pd.read_pickle(
        'data/course_similarities_10710')[int(course_id)]
    result = all_other_course.sort_values(ascending=False).iloc[0:10]
    
    response = [{'other': c_id, 'percent': percent}
                for c_id, percent in zip(result.index.tolist(), result.tolist())]

    return response
