import certifi
from elasticsearch import Elasticsearch

client = Elasticsearch(
    ['https://search-nthu-course-w2xlrcsccvfh6tzuu5jgoccxb4.us-east-1.es.amazonaws.com/'], use_ssl=True, ca_certs=certifi.where())


def toSearchOnlyKeyword(search_topic, keyword):
    print("search_topic:", search_topic, "keyword:", keyword)
    response = client.search(
        index="nthu",
        body={
            "size": 50,
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
    return response


def toSearchDoubleKeyword(search_topic, keyword, other_keyword):
    print("search_topic:", search_topic, "keyword:",
          keyword, "other_keyword:", other_keyword)
    response = client.search(
        index="nthu",
        body={
            "size": 50,
            "query": {
                "bool": {
                    "must": [
                        {"match": {"課程中文名稱": keyword}},
                        {"match": {earch_topic: other_keyword}}
                    ]
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
        index="nthu",
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
        index="nthu",
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
