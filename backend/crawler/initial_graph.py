from py2neo import Graph, Node, Relationship
import os
import sqlite3
import csv

folder = os.environ.get('NEO4J_FOLDER')
url = os.environ.get('GRAPHENEDB_URL', 'http://localhost:7474')
username = os.environ.get('NEO4J_USERNAME')
password = os.environ.get('NEO4J_PASSWORD')
graph = Graph(url + '/db/data/', username=username, password=password)

conn = sqlite3.connect('backend/crawler/test.db')
# cursor = conn.cursor()
# cursor.execute('drop table courses')
# cursor.execute('create table courses (id Integer PRIMARY KEY AUTOINCREMENT, no varchar(20), name_zh varchar(255), name_en varchar(255), teacher varchar(255), syllabus BLOB)')


def add_data():
    # pass
    add_courses()
    # add_category()
    # add_teach()
    # add_department()
    # add_topic()
    # add_relativity()


def add_courses():
    print('Start Add Course ...')
    query = '''
    LOAD CSV WITH HEADERS FROM {file} AS row
    CREATE (n:Course)
    SET n = row
    '''

    return graph.run(query, file="file:///test.csv")


def add_category():
    print('Start Add Category ...')
    query = '''
    LOAD CSV WITH HEADERS FROM {file} AS row
    CREATE (n:Category)
    SET n = row, n.name = row.name
    '''

    return graph.run(query, file="file:///test.csv")


# 教授教哪一堂課
def add_teach():
    print('Start Add Teach ...')
    query = '''
    CREATE (Category)-[:TEACH]->(Course)
    '''

    return graph.run(query)


# 課程屬於哪個系所
def add_department():
    print('Start Add Department ...')
    query = '''
    CREATE (Course)-[:BELONG_TO]->(Category)
    '''

    return graph.run(query)


# 課程關於哪個主題
def add_topic():
    print('Start Add Topic ...')
    query = '''
    CREATE (Course)-[:RELATE_TO]->(Category)
    '''

    return graph.run(query)


# 課程與課程相關性
def add_relativity():
    print('Start Add Relativity ...')
    query = '''
    CREATE (Course)-[:LIKE {Relativity: x%}]->(Course)
    '''

    return graph.run(query)


def db_to_csv():
    cur = conn.cursor()
    cur.execute("SELECT id, no, name_zh, name_en FROM courses")
    rows = cur.fetchall()

    with open(folder + '/import/test.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'no', 'name_zh', 'name_en']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {'id': row[0], 'no': row[1], 'name_zh': row[2], 'name_en': row[3]})
