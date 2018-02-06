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
                {'_id': jb['name'], 'password': jb['pwd']})
        except Exception as e:
            print(e)
            return HttpResponseBadRequest(e)
        else:
            return HttpResponse("inserted.")
    return HttpResponseBadRequest("not support method.")


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
    return HttpResponseBadRequest("not support method.")


def update(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def delete(request):
    return HttpResponse("Hello, world. You're at the polls index.")
