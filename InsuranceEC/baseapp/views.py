from django.shortcuts import render

# Create your views here.

def starting_page(request):
    return render(request, "baseapp/index.html")


def register(request):
    pass


def signin(request):
    pass


def about(request):
    pass


def services(request):
    pass
