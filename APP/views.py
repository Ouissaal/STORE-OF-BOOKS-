from django.shortcuts import render, redirect
from .models import Author, Book

def home(request): 
    books = Book.objects.all()

    books_list = [
        {
        'title' : 'Book1',
        'price': 100,
        'publication_year':1999,
        },
        {
        'title' : 'Book2',
        'price': 100,
        'publication_year':1999,
        },
        {
        'title' : 'Book3',
        'price': 100,
        'publication_year':1999,
        }                                  
        
    ]

    home_page_context = {
        'books': books,
        'manual_book_list': books_list,
    }
    return render(request, 'home.html', context=home_page_context)

def about(request):
    return render(request, 'about.html')


def book(request, id):
    book = Book.objects.get(id=id)
    context = {
        'book': book    
    }
    return render(request, 'book.html', context=context)


def create_book(request):
    author = Author.objects.get(id=1)
    if request.method == 'POST':
        title = request.POST.get('title')
        genre = request.POST.get('genre')
        price = request.POST.get('price')
        Book.objects.create(title=title, genre=genre, price=price, author=author)
        return redirect('home_page')
    return render(request, 'create_book.html')
