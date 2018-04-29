# -*- encoding: utf-8 -*-

import json
import sqlite3
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from pdf_parser import pdf_parser

acixstore = 'h099vl4srcr8c5sjs9nbgikqk3'

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# cursor.execute('drop table courses')
# cursor.execute('create table courses (id Integer PRIMARY KEY AUTOINCREMENT, no varchar(20), name_zh varchar(255), name_en varchar(255), teacher varchar(255), syllabus BLOB)')

data = json.load(open('open_course_data.json'))
for idx, course in enumerate(data):
    # course = data[1]

    # Just get "GE" courses
    if idx >= 721 and idx <= 730:
        no = course['科號']
        name_zh = course['課程中文名稱']
        name_en = course['課程英文名稱']
        teacher = course['授課教師']
        r = requests.get('https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/JH/common/Syllabus/1.php',
                         params={
                             'ACIXSTORE': acixstore,
                             'c_key': no
                         })
        r.encoding = 'cp950'
        soup = BeautifulSoup(r.text, 'lxml')
        syllabus = soup.find_all('table')[5].find('td', class_='class2')
        is_file = syllabus.text.startswith('觀看上傳之檔案(.pdf)')

        if is_file:
            r = requests.get('https://www.ccxp.nthu.edu.tw%s' %
                             syllabus.find('a').get('href'), stream=True)
            with open('test.pdf', 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            syllabus_blob = pdf_parser('test.pdf').encode('utf-8')
        else:
            syllabus_blob = syllabus.text.encode('utf-8')

        cursor.execute('INSERT INTO courses (no, name_zh, name_en, teacher, syllabus) VALUES (?, ?, ?, ?, ?)', [
                       no, name_zh, name_en, teacher, sqlite3.Binary(syllabus_blob)])
        conn.commit()

cursor.close()
conn.close()
