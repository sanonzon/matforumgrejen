#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import datetime
import os
# import helperFunctions 

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    asd = "heJ tesTTNNIGN 7878as 79d 7 DOOOT"
    test = normalizeTitle(asd)
    return render(request, "base.html", {
        'words':test, 
    })
   
def forumIndex(request):   
    asd = "heJ tesTTNNIGN 7878as 79d 7 DOOOT"
    test = normalizeTitle(asd)
    return render(request, "base.html", {
        'words':test, 
    })
    # PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    # TEMPLATE_DIRS = (
    #     os.path.join(PROJECT_ROOT, 'templates').replace('\\','/'),
    # )
    # return HttpResponse(TEMPLATE_DIRS[0])
    

def forumPost(request, category, postId):
    string = "\n{}\n{}\n{}\n".format(request, category, postId)
    return HttpResponse("Category: %s<br>Id: %s" % (category, str(postId)))

def createNewPost(request):
    pass

def forumCategory(request, category):
    return HttpResponse("Category: %s" %category)
    


'''
FUNCTIONS FÖR JAG FATTARINTE HUR MAN ANROPER FRÅN FIL. PLS FIX
'''
def normalizeTitle(input):               
    if ' ' in input:
        result = ""
        first = True
        for word in input.split():
            if first:
                result += normalizeWord(word)
                first = False
            else:
                result += " " + normalizeWord(word)
        return result
    else:
        return normalizeWord(input)

def normalizeWord(word):
    first = True
    result = ""
    for char in word:
        if first and not char.isdigit():
            first = False
            result += char.upper()
        else:
            if char.isdigit():
                result += char
            else:
                result += char.lower()
    return result

