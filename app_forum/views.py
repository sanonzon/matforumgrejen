from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import datetime
import os

# Create your views here.

def index(request):
    now = datetime.datetime.now()
 
    return render(request, "base.html")
   
def forumIndex(request):   
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    TEMPLATE_DIRS = (
        os.path.join(PROJECT_ROOT, 'templates').replace('\\','/'),
    )
    return HttpResponse(TEMPLATE_DIRS[0])
    

def forumPost(request, category, postId):
    string = "\n{}\n{}\n{}\n".format(request, category, postId)
    return HttpResponse("Category: %s<br>Id: %s" % (category, str(postId)))

def createNewPost(request):
    pass

def forumCategory(request, category):
    return HttpResponse("Category: %s" %category)
    