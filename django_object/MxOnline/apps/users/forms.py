# _*_ encoding:utf-8 _*_
__author__ = 'YL007'
__date__ = '2018/7/15 0:07'

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True)#如果为空就报错
    password = forms.CharField(required=True)