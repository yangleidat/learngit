from django.shortcuts import render
from .models import UserMessage
# Create your views here.

def getindex(request):
    message = None
    all_messages = UserMessage.objects.filter(name='yanglei2')
    if all_messages:
        message = all_messages[0]


    # if request.method == 'POST':
    #     user_message = UserMessage()
    #     user_message.name = request.POST.get('name','')
    #     user_message.message = request.POST.get('message','')
    #     user_message.address = request.POST.get('address','')
    #     # user_message.object_id = request.POST.get('','')
    #     user_message.email = request.POST.get('email','')
    #     user_message.save()
    return render(request, '留言板.html', {
        'my_message':message
    })