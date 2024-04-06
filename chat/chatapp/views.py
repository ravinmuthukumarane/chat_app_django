from django.shortcuts import render

def CreateRoom(request):
    return render(request, 'index.html')

def MessageView(request, room_name, username):
    return render(request, '_message.html')