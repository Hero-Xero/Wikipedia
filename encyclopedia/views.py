from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
        
    })
    
def entry_page(request, entry_title):
    try:
        entry_page = markdown2.markdown(util.get_entry(entry_title)) 
        return render(request, "encyclopedia/entry-page.html", {
            "entry_page": entry_page,
            "entry_title" : entry_title
        })
    except:
        return render(request, "encyclopedia/entry-page.html", {
            "entry_page": None
        })
 


def random(request):
    entry_title = util.random_entry()
    return redirect("entry_page", entry_title)

def create(request):
    if request.method == "POST":
        title = request.POST["title"].strip()
        content = request.POST["content"].strip()
        if title and content:
            if util.get_entry(title) is None:
                util.save_entry(title, content) 
                return redirect("entry_page", title)
            else:
                return render(request, "encyclopedia/create-new-page.html", {
                    "error": "An entry with this title already exists"
                })
        else:
            return render(request, "encyclopedia/create-new-page.html", {
                "error": "Please fill out both fields"
            })
    return render(request, "encyclopedia/create-new-page.html")


def search(request):
    query = request.GET.get("q")
    if util.get_entry(query):
        return redirect("entry_page", query)
    
    else:
        all_entries = util.list_entries()
        results = [entry for entry in all_entries if query.lower() in entry.lower() or entry.lower() in query.lower()]
        return render(request, "encyclopedia/search.html", {
            "results": results
        }) 
    

def edit(request, entry_title):
    entry_page = util.get_entry(entry_title)    
    if request.method == "POST":   
       title = request.POST["title"].strip()
       content = request.POST["content"].strip()
       if title and content:
                util.edit_entry(title, content, entry_title) 
                return redirect("entry_page", title)
       else:
            return render(request, "encyclopedia/edit.html", {
                "title": entry_title,
                "content": entry_page,
                "error": "Please fill out both fields"
            })

    return render(request, "encyclopedia/edit.html", {
        "title": entry_title,
        "content": entry_page,
    })



