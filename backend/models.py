from py2neo import Graph, Node, Relationship
import os

url = os.environ.get('GRAPHENEDB_URL', 'http://localhost:7474')
username = os.environ.get('NEO4J_USERNAME')
password = os.environ.get('NEO4J_PASSWORD')
graph = Graph(url + '/db/data/', username=username, password=password)


class Course:
    def __init__(self, course_id):
        self.course_id = course_id

    def findRelationship(self):
        print("Find The Relationship Of", self.course_id)
        query = '''
        MATCH (a:Course { course_id: toInt({c_id}) } )<-[r]-(b:Course)
        WITH {  
            other: b.course_id, 
            percent: r.percent
        } AS sim
        RETURN sim
        ORDER BY sim.percent DESC
        LIMIT 10
        '''

        return graph.run(query, c_id=self.course_id)
