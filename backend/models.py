from py2neo import Graph, Node, Relationship
import os
import sqlite3
import csv

url = os.environ.get('GRAPHENEDB_URL', 'http://localhost:7474')
username = os.environ.get('NEO4J_USERNAME')
password = os.environ.get('NEO4J_PASSWORD')
graph = Graph(url + '/db/data/', username=username, password=password)


class User:
    def __init__(self, username):
        self.username = username

    def add_people(self, other_username):
        tx = graph.begin()
        user = Node('User', name=self.username)
        tx.create(user)
        other = Node('User', name=other_username)
        rel = Relationship(user, 'KNOWS', other)
        tx.create(rel)
        tx.commit()


class Course:
    def __init__(self, courseID):
        self.courseID = courseID

    def loadCourseData(self):
        return graph.find_one('Course', 'id', self.courseID)
