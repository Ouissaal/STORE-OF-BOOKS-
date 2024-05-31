from django.shortcuts import render, redirect
from .models import Author, Book

def home(request): 
    books = Book.objects.all()

    books_list = [
        {'title': 'Book1', 'price': 100, 'publication_year': 1999},
        {'title': 'Book2', 'price': 100, 'publication_year': 1999},
        {'title': 'Book3', 'price': 100, 'publication_year': 1999}               
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
    authors = Author.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        genre = request.POST.get('genre')
        price = request.POST.get('price')
        publication_year = request.POST.get('publication_year')
        author_id = request.POST.get('author')
        author = Author.objects.get(id=author_id)
        Book.objects.create(title=title, genre=genre, price=price, publication_year=publication_year, author=author)
        return redirect('home_page')
    context = { 
        'authors': authors
    }
    return render(request, 'create_book.html', context=context)

def update_book(request, id):
    book = Book.objects.get(id=id)
    authors = Author.objects.all()
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.genre = request.POST.get('genre')
        book.price = request.POST.get('price')
        book.publication_year = request.POST.get('publication_year')
        author_id = request.POST.get('author')
        book.author = Author.objects.get(id=author_id)
        book.save()
        return redirect('home_page')
    context = { 
        'book': book,
        'authors': authors,   
    }
    return render(request, 'update_book.html', context=context)

def delete_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('home_page')
    context = {   
        'book': book,   
    }
    return render(request, 'delete_book.html', context=context)

def home_author(request):
    authors = Author.objects.all()
    return render(request, 'home_author.html', {'authors': authors})

def create_author(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        birth_date = request.POST.get('birth_date')
        nationality = request.POST.get('nationality')
        Author.objects.create(name=name, birth_date=birth_date, nationality=nationality)
        return redirect('home')
    return render(request, 'create_author.html')

def update_author(request, id):
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        author.name = request.POST.get('name')
        author.birth_date = request.POST.get('birth_date')
        author.nationality = request.POST.get('nationality')
        author.save()
        return redirect('home')
    return render(request, 'update_author.html', {'author': author})

def delete_author(request, id):
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        author.delete()
        return redirect('home')
    return render(request, 'delete_author.html', {'author': author})