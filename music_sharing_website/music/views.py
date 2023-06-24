from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from .forms import MusicFileForm,UserRegistrationForm
from .models import MusicFile

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'music/register.html', {'form': form})

@login_required
def home(request):
    username = request.user.username
    music_files = MusicFile.objects.filter(visibility='public') | MusicFile.objects.filter(user=request.user) | MusicFile.objects.filter(allowed_emails=request.user.email)
    
    
    return render(request, 'music/home.html', {'username': username, 'music_files': music_files})
    

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = MusicFileForm(request.POST, request.FILES)
        if form.is_valid():
            music_file = form.save(commit=False)
            music_file.user = request.user
            music_file.save()
            return redirect('home')
    else:
        form = MusicFileForm()
    return render(request, 'music/upload.html', {'form': form})
