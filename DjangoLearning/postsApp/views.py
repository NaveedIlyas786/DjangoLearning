from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
def AppModuleHome(request):
    posts = Post.objects.all().order_by("date") # we can arrange posts according to date ("date"=> asscending, and  "-date" => descending)
    return render(request, "posts/postModulefileList.html", {'posts': posts})

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "posts/post_page.html", {'post': post})

# Create your views here.
