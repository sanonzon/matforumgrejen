#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    # Doot
    pass

class Ingredient(models.Model):
    '''
    docString 
    '''
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=5)
    amount = models.FloatField()

# grönsaker, kött, fisk doot
class Category(models.Model):
    '''
    docString 
    '''
    name = models.CharField(max_length=255)

# mer filtrering?
    '''
    docString 
    '''
class SubCategory(models.Model):
    name = models.CharField(max_length=255)

class Recipe(models.Model):
    '''
    docString 
    '''
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    description = models.TextField()
    created = models.DateTimeField()   
    # No damn hosting for images. Do imgur or whatever.
    imageUrl = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
 

class ForumPost(models.Model):
    '''
    docString 
    '''
    title = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)   
    
class ForumReply(models.Model):
    '''
    docString 
    '''
    parent = models.ForeignKey(ForumPost, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
