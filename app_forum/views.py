#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import datetime
import os
from app_forum.helperFunctions import normalizeTitle
from app_forum.models import Category,Ingredient,Recipe,SubCategory,User, ForumPost, ForumReply
from .forms import RecipeForm, ReplyForm, CategoryForm, ForumPostForm

# import helperFunctions 

# Create your views here.

def index(request):
    '''
    docString 
    '''
    categoryList = Category.objects.all()
    asd = "heJ tesTTNNIGN 7878as 79d 7 DOOOT"
    test = normalizeTitle(asd)
    return render(request, "forumIndexView.html", {
        'words':test,
        'categoryList' : categoryList
    })

def forumPost(request, ctg, postId):
    '''
    RENDER THE FORUMPOST AND ALL THE CHILDREN THAT REPLIED 
    '''
    # NEW FORUM POST
    ForumPost.objects.get( pk = postId, category = ctg)


            

    string = "\n{}\n{}\n{}\n".format(request, category, postId)
    return HttpResponse("Category: %s<br>Id: %s" % (category, str(postId)))

def createNewPost(request):

    '''
    docString 
    '''
    pass

def forumCategory(request, category):
    '''
    LIST ALL FORUM POSTS FOR THIS CATEGORY
    '''  
    
    # VALIDATE FORM
    if(request.method == 'POST'):
        print(request.POST)
        form = ForumPostForm(request.POST)
        if(form.is_valid):
            #    INSERT SHIT TO DATABASE
            pass
        return HttpResponse("IS DONE")

    #RENDER ALL THE SHIT
    else:
        print(request.GET)
        form = ForumPostForm()
        forumPosts = ForumPost.objects.filter(pk = category)

        return render(request, "forumPostsView.html", {'posts' : forumPosts, 'postForm' : form, 'category': category})
#HttpResponse("Category: %s" %category, {posts : forumPosts})
    


