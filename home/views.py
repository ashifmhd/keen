from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(requst):
    return render(requst, 'index.html')

def edit(requst):
    return render(requst, 'edit.html')

def view(requst):
    return render(requst, 'view.html')

