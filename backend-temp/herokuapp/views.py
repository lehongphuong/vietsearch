from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# from .models import User
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
import requests
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import JsonResponse

from django.core import serializers

import json

# https://scrapy.org/ 

# from models import User
from . import models

from django.db import connection 

# https://elasticsearch-py.readthedocs.io/en/master/
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host':'localhost','port':9200}]) 
from datetime import datetime

def index(request):
    return render(request, "index.html", {"users": 1}) 

# *********************************************
# begin common 
@api_view(['GET'])
@parser_classes((JSONParser,))
# TEST
def test(request, format=None): 
    return Response([{"result": "ok"}])

# convert cursor to json data
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

# execute query sql with cursor
def executeQuery(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        data = dictfetchall(cursor)
    return data 

@api_view(['GET'])
@parser_classes((JSONParser,))
# insert All Data From JSON 
def insertAllDataFromJSON(request, format=None):
    with open('khoa-hoc.json', 'r', encoding='utf8') as f:
        data = f.readline() 
        data = json.loads(data)
        ans = 1
        for item in data:
            item.update({'id':ans})
            esCreate('articles',item) 
            ans = ans + 1

    return Response([{"result": "ok"}])

# Insert data to Elasticsearch
def esCreate(index_name, doc):
    try: 
        res = es.index(index=index_name, doc_type='tweet', id=doc['id'], body=doc) 
        es.indices.refresh(index=index_name)
    except: 
        print("An exception occurred")

# Read data from Elasticsearch
def esRead(index_name, doc):
    try: 
        res = es.get(index=index_name, doc_type='tweet', id=doc['id']) 
        return res['_source']
    except: 
        print("An exception occurred") 
        return {}
    

# Read data from Elasticsearch
def esReadAll(index_name): 
    try: 
        res = es.search(index=index_name, body={"query": {"match_all": {}}})
        return res
    except: 
        print("An exception occurred") 
        return []

# Delete data Elasticsearch
def esDelete(index_name, doc):
    try: 
        res=es.delete(index=index_name, doc_type='tweet', id=doc['id']) 
        es.indices.refresh(index=index_name)
    except: 
        print("An exception occurred") 
    

# Delete data Elasticsearch
def esSearch(index_name, doc):
    query_search = []

    # Check if exists then add to query search
    if 'title' in doc:
        query_search.append({'match':{ 'title': doc['title'] }})
    if 'content' in doc:
        query_search.append({'match':{ 'content': doc['content'] }})
    if 'public_date' in doc:
        query_search.append({'match':{ 'public_date': doc['public_date'] }})

    # Start search data with query_search
    res = es.search(index=index_name,body={ 
        'query':{
            'bool': {
                        'must': query_search  
                    }
        }
    })
    return res
 
# end common
# *********************************************
 
 
# *********************************************
# begin Articles
@api_view(['POST'])
@parser_classes((JSONParser,))
# create data from Articles
def createDataArticles(request, format=None):
    data = json.loads(json.dumps(request.data))
    esCreate('articles', data)
    return Response([{"result": "ok"}])


@api_view(['POST'])
@parser_classes((JSONParser,))
# get one data from Articles by one id
def readDataArticles(request, format=None):
    data = json.loads(json.dumps(request.data))
    return Response(esRead('articles', data))


@api_view(['POST'])
@parser_classes((JSONParser,))
# get many data from Articles by many id
def readManyDataArticles(request, format=None):
    data = json.loads(json.dumps(request.data))
    result = [] 
    for item in data:
        result.append(esRead('articles', item)) 
    return Response(result)

@api_view(['GET'])
@parser_classes((JSONParser,))
# get all data from Articles
def readAllDataArticles(request, format=None):
    result = esReadAll('articles')
    return Response(result)

@api_view(['POST'])
@parser_classes((JSONParser,))
# Update data from Articles by id
def updateDataArticles(request, format=None):
    data = json.loads(json.dumps(request.data))
    esCreate('articles', data)
    return Response([{"result": "ok"}])


@api_view(['POST'])
@parser_classes((JSONParser,))
# Delete one data from Articles by id
def deleteDataArticles(request, format=None):
    data = json.loads(json.dumps(request.data))
    esDelete('articles', data)
    return Response([{"result": "ok"}])


@api_view(['POST'])
@parser_classes((JSONParser,))
# Delete many data from Articles by many id
def deleteManyDataArticles(request, format=None):
    data = json.loads(json.dumps(request.data))
    result = [] 
    for item in data:
        esDelete('articles', item)

    return Response([{"result": "ok"}]) 
 
@api_view(['POST'])
@parser_classes((JSONParser,))
# Search data of Articles
def searchDataArticles(request, format=None):
    data = json.loads(json.dumps(request.data)) 
    return Response(esSearch('articles', data))

# end Articles
# ********************************************* 