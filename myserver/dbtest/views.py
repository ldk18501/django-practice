from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .connect import MongoConnection
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

mongo = MongoConnection('django_test')


@csrf_exempt  # 避免403
def insert(request):
    if request.method == 'POST':
        jb = json.loads(request.body.decode("utf-8"))
        print(jb)
        try:
            mongo.db.users.insert_one(
                {'_id': jb['name'], 'password': jb['password']})
        except Exception as e:
            print(e)
            return HttpResponseBadRequest(e)
        else:
            return HttpResponse("inserted.")
    return HttpResponseBadRequest("method error.")


def find(request):
    if request.method == 'GET':
        username = request.GET.get('name')
        if username is None:
            lstUser = list()
            for u in mongo.db.users.find():
                lstUser.append(u)
            return HttpResponse(json.dumps(lstUser))
        else:
            return HttpResponse(json.dumps(mongo.db.users.find_one({'_id': username})))
    return HttpResponseBadRequest("method error.")


@csrf_exempt
def update(request):
    if request.method == 'PUT':
        try:
            username = request.GET.get('name')
            jb = json.loads(request.body.decode("utf-8"))
            mongo.db.users.update_many({'_id': username}, {'$set': jb}, True)
            return HttpResponse(json.dumps(mongo.db.users.find_one({'_id': username})))
        except Exception as e:
            print(e)
            return HttpResponseBadRequest(e)
    return HttpResponseBadRequest("method error.")


@csrf_exempt
def delete(request):
    if request.method == 'DELETE':
        # 测一下delete_one，实际应用不删数据只改status
        username = request.GET.get('name')
        mongo.db.users.delete_one({'_id': username})
        return HttpResponse('deleted.')
    return HttpResponseBadRequest("method error.")
