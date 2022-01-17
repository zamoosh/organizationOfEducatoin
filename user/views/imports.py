# from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
