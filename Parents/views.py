from django.shortcuts import render
from django.http import HttpResponse

def tostudent_page_view(request):
    return HttpResponse('tostudent')

def toadmin_page_view(request):
    return HttpResponse('toadmin')
    
def toschool_page_view(request):
    return HttpResponse('toschool')
    
def aboutstudent_page_view(request):
    return HttpResponse('aboutstudent')