from django.shortcuts import render
from django.http import HttpResponse


def index_i(requests):
    
    # data = "hello"
    return HttpResponse('hello django')