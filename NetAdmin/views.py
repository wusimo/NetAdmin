from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from NetAdmin.models import Message
from Account.models import Account

def landing_page_view(request):
    return render(request, 'landing.html')

def index_page_view(request):
    if request.user.is_authenticated():
        if request.user.is_student:
            return HttpResponseRedirect('/student/')
        elif request.user.is_TA:
            return HttpResponseRedirect('/ta/')
        elif request.user.is_admin:
            return HttpResponseRedirect('/agent/')
        elif request.user.is_parents:
            return HttpResponseRedirect('/parents/')
    else:
        return HttpResponseRedirect('/account/login/')

def message_page_view(request, message_id):
    # todo:this message id should be the id of first message
    message_list = []
    message = Message.objects.get(id=message_id)
    message_list.append(message)
    while message.reply_to:
        reply = Message.objects.get(id=message.reply_to)
        message_list.append(reply)
        message = reply

    # todo: if too many replies then split to multiple pages
    return render(request, 'message_detail.html', {'message_list':message_list})

def send_message_view(request):
    if request.user.is_authenticated() and request.method == 'POST':
        new_message = Message()
        new_message.receiver = request.POST['receiver']
        new_message.sender = request.POST['sender']
        new_message.content = request.POST['content']
        # todo: check if title is too long

        if request.POST['reply_to']:
            new_message.reply_to = request.POST['reply_to']
            new_message.title = Message.objects.get(id=request.POST['reply_to']).title
        else:
            new_message.title = request.POST['title']

        sender_account = Account.objects.get(username=request.POST['sender'])
        # todo: looks like django has specific methods to deal with permissions
        if sender_account.is_student:
            new_message.from_student = True
        elif sender_account.is_admin:
            new_message.from_admin = True
        elif sender_account.is_TA:
            new_message.from_ta = True
        else:
            new_message.from_parents = True

        new_message.save()
        # todo: notifications

    # todo: redirect url
    return HttpResponseRedirect('/')
