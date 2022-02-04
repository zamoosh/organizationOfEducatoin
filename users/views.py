from django.shortcuts import render


def profile(request):
    return render(request, 'login/profile.html')


def notes(request):
    return render(request, 'lesson/notes.html')


def lessons(request):
    return render(request, 'lesson/lessons.html')


def index(request):
    return render(request, 'index.html')


def article(request):
    return render(request, 'lesson/articles.html')


def notifications(request):
    return render(request, 'lesson/notifications.html')
