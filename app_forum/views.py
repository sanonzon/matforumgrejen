#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import datetime
import os
from app_forum.helperFunctions import normalizeTitle
from app_forum.models import Category,Ingredient,Recipe,SubCategory,User
# import helperFunctions 

# Create your views here.

def index(request):
    categoryList = Category.objects.all()
    asd = "heJ tesTTNNIGN 7878as 79d 7 DOOOT"
    test = normalizeTitle(asd)
    return render(request, "base.html", {
        'words':test,
        'categoryList' : categoryList
    })

def forumPost(request, category, postId):
    string = "\n{}\n{}\n{}\n".format(request, category, postId)
    return HttpResponse("Category: %s<br>Id: %s" % (category, str(postId)))

def createNewPost(request):
    pass

def forumCategory(request, category):
    return HttpResponse("Category: %s" %category)
    


