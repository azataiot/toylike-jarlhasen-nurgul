from django.shortcuts import render
from datetime import datetime
import time
from django.utils import timezone
from .models import Blessing


def index(request):
    if request.method == 'GET':
        invited_name = request.GET.get('name', default='Досым')
        blessings = Blessing.objects.all()
        content = {
            'friend': invited_name,
            'blessings': blessings
        }
        return render(request, 'index.html', content)
    if request.method == 'POST':
        sender = request.POST.get('sender', None)
        message = request.POST.get('message', None)
        if (len(sender) != 0) and (len(message) != 0):
            blessings = Blessing.objects.all()
            content = {
                'friend': sender,
                'blessings': blessings
            }
            new_blessings = Blessing()
            new_blessings.sender = sender
            new_blessings.message = message
            new_blessings.save()
        return render(request, 'index.html', content)
