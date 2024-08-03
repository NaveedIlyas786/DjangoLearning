from django.shortcuts import render

def AppModuleHome(request):
    return render(request, "posts/postModulefileList.html")
# Create your views here.
