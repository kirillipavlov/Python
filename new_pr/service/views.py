#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, StreamingHttpResponse
from django.urls import reverse
sd
from .models import Product

from django.core.exceptions import ObjectDoesNotExist


def index(request):
    return HttpResponse('Index Service')


def page(request, page_num):
    print("ddf")
    return HttpResponse(f'Page {page_num}')


#def about(request):
#    #a = int(request.GET.get('a'))
#    #b = int(request.GET.get('b'))
#    #return HttpResponse(f'{a+b}')
#    #return HttpResponse(f'{request.headers}')
#    #return HttpResponse(f'{request.method}')
#    #return HttpResponse(f'{request.scheme}')
#    #return HttpResponse(f'{dict(request.GET)}')
#    #return HttpResponse("About")

#    res = HttpResponse('Hello')
#    #return HttpResponse(f'{res.status_code}')
#    #return HttpResponse(f'{res.content}')#

#    #return HttpResponseRedirect('service')
#    return HttpResponseRedirect(reverse('service'))


def about(request, id):
    try:
        var = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return HttpResponseNotFound("NOT FOUND")
    return HttpResponse('OK')
