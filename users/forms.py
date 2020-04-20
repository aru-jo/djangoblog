#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 02:35:52 2019

@author: aravindjyothi
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta: 
        model = User
        fields = ['username', 'email']
    
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        