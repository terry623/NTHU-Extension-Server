import certifi
from elasticsearch import Elasticsearch
from backend.save import toSaveKeyword

client = Elasticsearch(['localhost:9200/'])


def toSearchOnlyKeyword(search_topic, keyword):
    print("search_topic:", search_topic, "keyword:", keyword)
    response = client.search(
        index="nthu3",
        body={
            "size": 100,
            "query": {
                "bool": {
                    "must": [
                        {"match": {search_topic: keyword}}
                    ]
                }
            }
        }
    )
    # for hit in response['hits']['hits']:
    #     print(hit['_source']['課程中文名稱'])
    toSaveKeyword(search_topic, keyword, '')
    return response


def toSearchDoubleKeyword(search_topic, keyword, other_keyword):
    print("search_topic:", search_topic, "keyword:", keyword, "other_keyword:", other_keyword)

    match_special = {"match_all": {}}
    if(keyword != ""):
        match_special = {"match": {"課程中文名稱": keyword}}

    response = client.search(
        index="nthu3",
        body={
            "size": 100,
            "query": {
                "bool": {
                    "must": [
                        match_special,
                        {"match": {search_topic: other_keyword}}
                    ]
                }
            }
        }
    )
    # for hit in response['hits']['hits']:
    #     print(hit['_source']['課程中文名稱'])
    toSaveKeyword(search_topic, keyword, other_keyword)
    return response


def toSearchTime(search_topic, keyword, time_group):
    print("search_topic:", search_topic, "keyword:",
          keyword, "time_group:", time_group)

    match_special = {"match_all": {}}
    if(keyword != ""):
        match_special = {"match": {"課程中文名稱": keyword}}

    all_time = ["M1", "M2", "M3", "M4", "Mn", "M5",
                "M6", "M7", "M8", "M9", "Ma", "Mb", "Mc",
                "T1", "T2", "T3", "T4", "Tn", "T5",
                "T6", "T7", "T8", "T9", "Ta", "Tb", "Tc",
                "W1", "W2", "W3", "W4", "Wn", "W5",
                "W6", "W7", "W8", "W9", "Wa", "Wb", "Wc",
                "R1", "R2", "R3", "R4", "Rn", "R5",
                "R6", "R7", "R8", "R9", "Ra", "Rb", "Rc",
                "F1", "F2", "F3", "F4", "Fn", "F5",
                "F6", "F7", "F8", "F9", "Fa", "Fb", "Fc",
                "S1", "S2", "S3", "S4", "Sn", "S5",
                "S6", "S7", "S8", "S9", "Sa", "Sb", "Sc"]

    should_group = []
    must_not_group = []
    for each_time in all_time:
        each_match = {"match": {"時間": each_time}}
        if each_time not in time_group:
            must_not_group.append(each_match)
        else:
            should_group.append(each_match)

    response = client.search(
        index="nthu3",
        body={
            "size": 100,
            "query": {
                "bool": {
                    "must": [
                        match_special
                    ],
                    "should": should_group,
                    "minimum_should_match": 1,
                    "must_not": must_not_group
                }
            }
        }
    )
    # for hit in response['hits']['hits']:
    #     print(hit['_source']['課程中文名稱'])
    return response


def toSearchBySingleCourseNo(course_no):
    print("course_no:", course_no)
    response = client.search(
        index="nthu3",
        body={
            "query": {
                "bool": {
                    "must": [
                        {"match": {"科號": course_no}}
                    ]
                }
            }
        }
    )
    # for hit in response['hits']['hits']:
    #     print(hit['_source']['課程中文名稱'])
    return response


def toSearchByID_Group(id_0, id_1, id_2):
    print("id_0:", id_0, "id_1:", id_1, "id_2:", id_2)
    response = client.search(
        index="nthu3",
        body={
            "query": {
                "terms": {
                    "_id": [
                        id_0, id_1, id_2
                    ]
                }
            }
        }
    )
    # for hit in response['hits']['hits']:
    #     print(hit['_source']['課程中文名稱'])
    return response
