from django.urls import path

from . import views

urlpatterns = [
    path('', views.AppModuleHome, name="postsApp"),
    path('<slug:slug>', views.post_page, name="page"),
]