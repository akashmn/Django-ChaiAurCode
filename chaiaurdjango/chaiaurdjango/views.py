from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('HOME PAGE!')
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse('about PAGE!')

def contact(request):
    return HttpResponse('contact PAGE!')
