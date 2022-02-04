from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.conf import settings
from rest_framework.status import HTTP_200_OK
from article.models import *
import json
