from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Count, Sum, Avg, Max, Min
from .models import Book, Student, Address, Student2, BookCover
from .forms import BookForm, StudentForm, StudentForm2, BookCoverForm


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
    number=Student.objects.values('address__city').annotate(count=Count('id'))
    return render(request, 'bookmodule/task7.html', {'number': number})


def listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/listbooks.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = float(request.POST.get('price'))
        edition = int(request.POST.get('edition'))
        Book.objects.create(title=title, author=author, price=price, edition=edition)
        return redirect('/books/lab9_part1/listbooks')
    return render(request, 'bookmodule/addbook.html')


def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = float(request.POST.get('price'))
        book.edition = int(request.POST.get('edition'))
        book.save()
        return redirect('/books/lab9_part1/listbooks')
    return render(request, 'bookmodule/editbook.html', {'book': book})


def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/books/lab9_part1/listbooks')


def listbooks2(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/listbooks2.html', {'books': books})


def add_book2(request):
    form = BookForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/books/lab9_part2/booklist2')
    return render(request, 'bookmodule/addbook2.html', {'form': form})


def edit_book2(request, id):
    book = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, instance=book)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/books/lab9_part2/listbooks2')
    return render(request, 'bookmodule/editbook2.html', {'form': form, 'book': book})


def delete_book2(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.delete()
        return redirect('/books/lab9_part2/listbooks2')


def list_students(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/list_students.html', {'students': students})


def add_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_students')
    return render(request, 'bookmodule/add_student.html', {'form': form})


def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('list_students')
    return render(request, 'bookmodule/update_student.html', {'form': form})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('list_students')


def list_students2(request):
    students = Student2.objects.all()
    return render(request, 'bookmodule/list_student2.html', {'students': students})


def add_student2(request):
    form = StudentForm2(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_students2')
    return render(request, 'bookmodule/add_student2.html', {'form': form})


def update_student2(request, id):
    student = get_object_or_404(Student2, id=id)
    form = StudentForm2(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('list_students2')
    return render(request, 'bookmodule/update_student.html', {'form': form})


def delete_student2(request, id):
    student = get_object_or_404(Student2, id=id)
    student.delete()
    return redirect('list_students2')


def addBookWithCover(request):
    if request.method == 'POST':
        form = BookCoverForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            books =BookCover.objects.all()
            return render(request,'bookmodule/listBooksCovers.html',{'books':books})
        else:
            print(form.errors)
    form = BookCoverForm(None)
    return render(request,'bookmodule/addbookcover.html',{'form':form})


def l12task1(request):
    return render(request,'bookmodule/l12task1.html')


def l12task2(request):
    return render(request,'bookmodule/l12task2.html')


def l12task3(request):
    return render(request,'bookmodule/l12task3.html')


def l12task4(request):
    return render(request,'bookmodule/l12task4.html')


def l12task5(request):
    return render(request,'bookmodule/l12task5.html')