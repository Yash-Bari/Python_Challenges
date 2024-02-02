from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
from datetime import datetime
from rest_framework import generics
from .serializers import UserSerializer


def index(request):
    users = User.objects.all()
    current_datetime = datetime.now()
    return render(request, 'mywebapp/index.html', {'users': users, 'current_datetime': current_datetime})

def User_List(request):
    return render(request, 'mywebapp/user_list.html')

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'mywebapp/add_user.html', {'form': form})

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
