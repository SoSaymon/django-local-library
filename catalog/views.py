from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    num_genres = Genre.objects.all().count()
    num_books_with_love_word = Book.objects.filter(title__contains="Love").count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_books_with_love_word': num_books_with_love_word,
    }

    return render(request, 'index.html', context=context)
