from django.shortcuts import render

def index_page_view(request):
    return render(request, 'mailbox.html')
