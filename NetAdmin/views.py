from django.shortcuts import render
from django.http import HttpResponse

def index_page_view(request):
    return render(request, 'mailbox.html')

def landing_page_view(request):
    return HttpResponse('Here is landing page')
