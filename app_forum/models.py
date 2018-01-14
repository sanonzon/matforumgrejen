#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    # Doot
    pass

class Ingredient:
    name = models.CharField()
    unit = models.CharField()
    amount = models.FloatField()

# grönsaker, kött, fisk doot
class Category:
    name = models.CharField()

# mer filtrering?
class SubCategory:
    name = models.CharField()

class Recipe:
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField()
    
    # No damn hosting for images. Do imgur or whatever.
    imageUrl = models.CharField()
    created = models.DateTimeField()


