from django.shortcuts import render
from django.http import HttpResponse

def tostudent_page_view(request, student_id):
    return HttpResponse('tostudent ' + str(student_id))
    
def tostudent_toschool_page_view(request, student_id):
    return HttpResponse('tostudent_toschool ' + str(student_id))

def tota_page_view(request, ta_id):
    return HttpResponse('tota ' + str(ta_id))
    
def toparents_page_view(request, parents_id):
    return HttpResponse('toparents ' + str(parents_id))
    
def dashboard_page_view(request):
    return HttpResponse('dashboard')