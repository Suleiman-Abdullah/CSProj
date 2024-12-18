from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name="books.index"),
 path('list_books/', views.list_books, name="books.list_books"),
 path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
 path('aboutus/', views.aboutus, name="books.aboutus"),
 path('html5/links/', views.links, name='books.links'),
 path('html5/text/formatting/', views.formatting, name='books.formatting'),
 path('html5/listing/', views.listing, name='books.listing'),
 path('html5/tables/', views.tables, name='books.tables'),
 path('search/', views.search, name='books.search'),
 path('simple/query', views.simple_query, name='books.simple_query'),
 path('complex/query', views.complex_query, name='books.complex_query'),
 path('lab8/task1', views.task1, name='books.task1'),
 path('lab8/task2', views.task2, name='books.task2'),
 path('lab8/task3', views.task3, name='books.task3'),
 path('lab8/task4', views.task4, name='books.task4'),
 path('lab8/task5', views.task5, name='books.task5'),
 path('lab8/task7', views.task7, name='books.task7'),
 path('lab9_part1/listbooks', views.listbooks, name='listbooks'),
 path('lab9_part1/addbook', views.add_book, name='add_book'),
 path('lab9_part1/editbook/<int:id>', views.edit_book, name='edit_book'),
 path('lab9_part1/deletebook/<int:id>', views.delete_book, name='delete_book'),
 path('lab9_part2/listbooks2/', views.listbooks2, name='listbooks2'),
 path('lab9_part2/addbook2/', views.add_book2, name='add_book2'),
 path('lab9_part2/editbook2/<int:id>/', views.edit_book2, name='edit_book2'),
 path('lab9_part2/deletebook2/<int:id>/', views.delete_book2, name='delete_book2'),
 path('lab10/list_student', views.list_students, name='list_students'),
 path('lab10/add_student', views.add_student, name='add_student'),
 path('lab10/update/<int:id>/', views.update_student, name='update_student'),
 path('lab10/delete/<int:id>/', views.delete_student, name='delete_student'),
 path('lab10/list_student2', views.list_students2, name='list_students2'),
 path('lab10/add_student2', views.add_student2, name='add_student2'),
 path('lab10/update2/<int:id>/', views.update_student2, name='update_student2'),
 path('lab10/delete2/<int:id>/', views.delete_student2, name='delete_student2'),
 path('lab10/addBookWithCover', views.addBookWithCover, name= "books.addBookWithCover"),
 path('lab12/task1', views.l12task1, name= "lab12_task1"),
 path('lab12/task2', views.l12task2, name= "lab12_task2"),
 path('lab12/task3', views.l12task3, name= "lab12_task3"),
 path('lab12/task4', views.l12task4, name= "lab12_task4"),
 path('lab12/task5', views.l12task5, name= "lab12_task5"),
]
