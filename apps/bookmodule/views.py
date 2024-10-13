from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    name = request.GET.get("name") or "world!"  # add this line
    return render(request, "bookmodule/index.html", {"name": name})


def index2(request, val1=0):
    return HttpResponse("value1 = "+str(val1))


def viewbook(request, bookid):
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetbook = None
    if book1['id'] == bookid:
        targetbook = book1
    if book2['id'] == bookid:
        targetbook = book2
    context = {'book': targetbook}
    return render(request, 'bookmodule/show.html', context)