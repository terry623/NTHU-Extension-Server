# import pandas as pd
# from py2neo import Graph, Node, Relationship
# import os

# folder = os.environ.get('NEO4J_FOLDER')
# url = os.environ.get('GRAPHENEDB_URL', 'http://localhost:7474')
# username = os.environ.get('NEO4J_USERNAME')
# password = os.environ.get('NEO4J_PASSWORD')
# graph = Graph(url + '/db/data/', username=username, password=password)


# def sim_to_csv():
#     print("Sim to CSV")
#     df = pd.read_pickle('data/course_similarities')
#     df.index.name = 'id'
#     df.to_csv(folder + '/import/sim.csv')


# def csv_to_neo():
#     csvToNeo_createNode()
#     print('Neo Create Node Finish')

#     all_course = pd.read_pickle('data/course_similarities')
#     length = len(all_course.index)
#     for col in range(0, length):
#         select = all_course[int(col)]
#         result = select.sort_values(ascending=False).iloc[0:21]
#         for row in list(result.index.values):
#             if(row != col):
#                 percent = result.loc[row]
#                 csvToNeo_createRel(row.item(), col, percent)
#     print('Neo Create Relationship Finish')


# def csvToNeo_createNode():
#     print('Neo Create Node ...')
#     query = '''
#     LOAD CSV WITH HEADERS FROM {file} AS row
#     CREATE (a:Course)
#     SET a.course_id = toInteger(row.id)
#     '''

#     return graph.run(query, file="file:///sim.csv")


# def csvToNeo_createRel(a, b, per):
#     # a -> table left, b -> table top
#     print('Neo Create Relationship Between', a, 'and', b, '=>', per)
#     query = '''
#     MATCH (a:Course),(b:Course)
#     WHERE a.course_id = {a_id} AND b.course_id = {b_id}
#     CREATE (a)-[r:similarity { percent : {percent} }]->(b)
#     RETURN a.course_id, b.course_id, r.percent
#     '''

#     return graph.run(query, a_id=a, b_id=b, percent=per)
