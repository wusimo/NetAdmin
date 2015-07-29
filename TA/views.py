from django.shortcuts import render
from django.http import HttpResponse

def papers_page_view(request):
    return HttpResponse('papers')

def tostudent_page_view(request, student_id):
    return HttpResponse('student ' + str(student_id))
