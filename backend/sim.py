import pandas as pd
from py2neo import Graph, Node, Relationship
import os

folder = os.environ.get('NEO4J_FOLDER')
url = os.environ.get('GRAPHENEDB_URL', 'http://localhost:7474')
username = os.environ.get('NEO4J_USERNAME')
password = os.environ.get('NEO4J_PASSWORD')
graph = Graph(url + '/db/data/', username=username, password=password)


def sim_to_csv():
    print("Sim to CSV")
    df = pd.read_pickle('data/course_similarities')
    df.index.name = 'id'
    df.to_csv(folder + '/import/sim.csv')


def csv_to_neo():
    csvToNeo_createNode()
    print('Neo Create Node Finish')
    all_other_course = pd.read_pickle('data/course_similarities')
    length = len(all_other_course.index)
    for row in range(0, length-1):
        for col in range(0, length-1):
            if row < 30 and col < 30 and row != col:
                per = all_other_course.iloc[row, col]
                csvToNeo_createRel(row, col, per)
    print('Neo Create Relationship Finish')


def csvToNeo_createNode():
    print('Neo Create Node ...')
    query = '''
    LOAD CSV WITH HEADERS FROM {file} AS row
    CREATE (a:Course)
    SET a.course_id = toInteger(row.id)
    '''

    return graph.run(query, file="file:///sim.csv")


def csvToNeo_createRel(a, b, per):
    print('Neo Create Relationship Between', a, 'and', b)
    query = '''
    MATCH (a:Course),(b:Course)
    WHERE a.course_id = {a_id} AND b.course_id = {b_id}
    CREATE (a)-[r:similarity { percent : {percent} }]->(b)
    RETURN type(r), r.percent
    '''

    return graph.run(query, a_id=a, b_id=b, percent=per)


# def findDataUseTable(course_id):

#     all_other_course = pd.read_pickle(
#     'data/course_similarities')[int(course_id)]
#     result = all_other_course.sort_values(ascending=False).iloc[0:10]

#     response = [{'c_id': c_id, 'percent': percent}
#                 for c_id, percent in zip(result.index.tolist(), result.tolist())]

#     return response
