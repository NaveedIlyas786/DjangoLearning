from django.shortcuts import render
from .models import Post

def AppModuleHome(request):
    posts = Post.objects.all().order_by("date") # we can arrange posts according to date ("date"=> asscending, and  "-date" => descending)
    return render(request, "posts/postModulefileList.html", {'posts': posts})
# Create your views here.
