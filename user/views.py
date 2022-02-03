from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect


def login_page(request):
    return render(request, "login/profile.html")


def test(request):
    return render(request, 'test.html')


def test2(request):
    return render(request, 'index.html', context={"name": "ali"})


