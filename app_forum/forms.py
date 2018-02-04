#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

class RecipeForm(forms.Form):
    '''
    Designated form to create a recipe?
    '''
    title = forms.CharField(label='Title', max_length=255 )
    content = forms.CharField(widget=forms.Textarea)

class ReplyForm(forms.Form):
    '''
    Form for replying to existing forum post
    '''
    content = forms.CharField(widget=forms.Textarea)

class CategoryForm(forms.Form):
    '''
    Create a new category
    '''
    category = forms.CharField(label='Category', max_length=255 )

class ForumPostForm(forms.Form):   
    '''
    Create a new forum post for duscission
    '''
    title = forms.CharField(label='Title', max_length=255)
    content = forms.CharField(widget=forms.Textarea)
    