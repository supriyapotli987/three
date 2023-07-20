from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def string_response(request):
    return HttpResponse('This is my First string')
def string_response1(request):
    return HttpResponse('This is my Second string')
def string_response2(request):
    return HttpResponse('This is my 3rd string')
    

