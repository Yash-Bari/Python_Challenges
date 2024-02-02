from django.shortcuts import render
from datetime import datetime

def index(request):
    current_datetime = datetime.now()
    return render(request, 'mywebapp/index.html', {'current_datetime': current_datetime})
