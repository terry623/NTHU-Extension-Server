import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import requests
import json

mapping = {
    "mappings": {
        "course": {
            "properties": {
                "不可加簽說明": {"type": "text"},
                "人限": {"type": "long"},
                "備註": {"type": "text"},
                "學分數": {"type": "long"},
                "授課語言": {"type": "keyword"},
                "擋修說明": {"type": "text"},
                "新生保留人數": {"type": "long"},
                "科號": {"type": "keyword"},
                "課程中文名稱": {"type": "text"},
                "課程英文名稱": {"type": "text"},
                "課程限制說明": {"type": "text"},
                "通識對象": {"type": "keyword"},
                "通識類別": {"type": "keyword"},
                "課綱": {"type": "text"},
                "開課代碼": {"type": "keyword"},
                "教師": {"type": "text"},
                "教室": {"type": "text"},
                "時間": {"type": "keyword"},
                "學程": {"type": "keyword"},
                "必選修": {"type": "keyword"},
                "第一二專長": {"type": "keyword"},
            }
        }
    }
}
req = requests.put('http://localhost:9200/nthu2', json=mapping)
print(req.json())

d = pd.read_pickle('../data/open_course_data_with_syllabus_serialize_10710')


def index2elastic(idx, data):
    req = requests.put(
        'http://localhost:9200/nthu2/course/' + str(idx), json=data)
    print(idx, req.json()['result'])


for idx, row in d.iterrows():
    index2elastic(idx, row.to_dict())
