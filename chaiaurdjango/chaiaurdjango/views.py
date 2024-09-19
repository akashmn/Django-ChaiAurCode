from django.http import HttpResponse

def home(request):
    return HttpResponse('HOME PAGE!')

def about(request):
    return HttpResponse('about PAGE!')

def contact(request):
    return HttpResponse('contact PAGE!')
