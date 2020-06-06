from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from content.models import Content, Menu, CImages
from product.models import Category


def index(request):
    return HttpResponse("Content App ")

