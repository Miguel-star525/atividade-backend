from django.shortcuts import render
from django.http import HttpResponse

def home(resquest):
    return HttpResponse("Bem-vindo! Me chamo Miguel")