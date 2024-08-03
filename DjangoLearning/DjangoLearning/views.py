# from django.http import HttpResponse
from django.shortcuts import render

def myHomePage(request):
    return render(request, "Home.html")

def myAboutPage(request):
    return render(request, "About.html")