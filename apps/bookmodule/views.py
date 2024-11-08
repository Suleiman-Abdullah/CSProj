from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q, Count, Sum, Avg, Max, Min
from .models import Book, Students, Address


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


def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getbookslist()
        newbooks = []
        for item in books:
            contained = False
        if isTitle and string in item['title'].lower():
            contained = True
        if not contained and isAuthor and string in item['author'].lower():
            contained = True

        if contained: newbooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books': newbooks})
    return render(request, 'bookmodule/search.html')


def __getbookslist():
 book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
 book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
 book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
 return [book1, book2, book3]


def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})


def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull=False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')


def task1(request):
    mybook=Book.objects.filter(Q(price__lte=50))
    return render(request, 'bookmodule/task1.html', {'books': mybook})


def task2(request):
    mybook=Book.objects.filter(Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'bookmodule/task2.html', {'books': mybook})


def task3(request):
    mybook=Book.objects.filter(~Q(edition__gt=2) & ~(Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'bookmodule/task3.html', {'books': mybook})


def task4(request):
    mybook=Book.objects.order_by('title')
    return render(request, 'bookmodule/task4.html', {'books': mybook})


def task5(request):
    mybook=Book.objects.aggregate(
        count=Count('id'),
        TPrice=Sum('price'),
        APrice=Avg('price'),
        MaPrice=Max('price'),
        MiPrice=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'books': mybook})


def task7(request):
    number=Students.objects.values('address__city').annotate(count=Count('id'))
    return render(request, 'bookmodule/task7.html', {'number': number})
