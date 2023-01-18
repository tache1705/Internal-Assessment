from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def cover_page(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "cover_page.html", {})


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})
