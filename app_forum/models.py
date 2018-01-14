#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    # Doot
    pass

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=5)
    amount = models.FloatField()

# grönsaker, kött, fisk doot
class Category(models.Model):
    name = models.CharField(max_length=255)

# mer filtrering?
class SubCategory(models.Model):
    name = models.CharField(max_length=255)

class Recipe(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    # No damn hosting for images. Do imgur or whatever.
    imageUrl = models.TextField()
    created = models.DateTimeField()


