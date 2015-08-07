from django.shortcuts import render
from django.http import HttpResponse

from NetAdmin.models import Message

def index_page_view(request):
    return HttpResponse('index page')

def toparents_page_view(request):
    message_list = Message.objects.filter(from_parents=True, receiver='agent', first_message=True)

    return render(request, 'message_list.html',
                  {'message_category': 'Message with Parents',
                   'message': message_list})

def tostudent_page_view(request):
    return render(request, 'message_list.html',)

def tota_page_view(request):
    return HttpResponse('toTA')

def translate_page_view(request):
    return HttpResponse('translate_list_view')

def studentinfo_page_view(request):
    return HttpResponse('student info')
