from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('statement updated in hello')
    
def hello(request,name):
    return HttpResponse(f'statement updated with {name}')

def question(request):
    return HttpResponse('find the solution')

def question(request,data):
    return HttpResponse(f'solution found')