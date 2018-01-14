from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import datetime

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    html = "hej dootface, kl är %s \n\nif inloggad:\n\tvisa index\nelse:\n\tredirect login" % now
    return HttpResponse(html)

def forumIndex(request):
    return HttpResponse("forumet")

def forumPost(request, category, postId):
    string = "\n{}\n{}\n{}\n".format(request, category, postId)
    return HttpResponse(string)

def createNewPost(request):
    pass