from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name="books.index"),
 path('list_books/', views.list_books, name="books.list_books"),
 path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
 path('aboutus/', views.aboutus, name="books.aboutus"),
 path('html5/links/', views.links, name='books.links'),
 path('html5/text/formatting/', views.formatting, name='books.formatting'),

 path('index2/<int:val1>/', views.index2),
]
