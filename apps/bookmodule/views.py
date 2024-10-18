from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def index2(request, val1=0):
    return HttpResponse("value1 = "+str(val1))


def index(request):
    return render(request, "bookmodule/index.html")


def list_books(request):
    return render(request, 'bookmodule/list_books.html')


def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')


def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')


def links(request):
    return render(request, 'bookmodule/links.html')


def formatting(request):
    return render(request, 'bookmodule/formatting.html')


def listing(request):
    return render(request, 'bookmodule/listing.html')


def tables(request):
    return render(request, 'bookmodule/tables.html')