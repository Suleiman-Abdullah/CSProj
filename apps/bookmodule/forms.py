from django import forms
from .models import Book, Student, Student2, Address, BookCover


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentForm2(forms.ModelForm):
    class Meta:
        model = Student2
        fields = '__all__'


class BookCoverForm(forms.ModelForm):
    class Meta:
        model = BookCover
        fields = '__all__'

