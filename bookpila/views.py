from django.shortcuts import render

def index(req):
    return render(req, 'index.html')

def book_not_found(req):
    return render(req, 'book_not_found.html')
