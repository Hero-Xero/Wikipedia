from django.urls import path, include
from . import views

from django.shortcuts import redirect

def redirect_to_wiki(request):
    return redirect("index")  

urlpatterns = [
    path("", redirect_to_wiki), 
    path("wiki/", include([
        path("", views.index, name="index"), 
        path("random/", views.random, name="random"),
        path("create/", views.create, name="create"),
        path("search/", views.search, name="search"),
        path("edit/<str:entry_title>/", views.edit, name="edit"),
        path("<str:entry_title>/", views.entry_page, name="entry_page"),
    ])),
]