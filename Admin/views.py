from django.shortcuts import render
from django.http import HttpResponse

def index_page_view(request):
    return HttpResponse('index page')

def toparents_page_view(request):
    return render(request, 'chat.html')

def tostudent_page_view(request):
    return HttpResponse('tostudent')

def tota_page_view(request):
    return HttpResponse('toTA')

def translate_page_view(request):
    return HttpResponse('translate_list_view')

def studentinfo_page_view(request):
    return HttpResponse('student info')
