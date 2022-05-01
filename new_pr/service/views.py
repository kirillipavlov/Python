#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello')

def page(request, page_num):
    print("ddf")
    return HttpResponse(f'Page {page_num}')