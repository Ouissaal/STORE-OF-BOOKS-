from django.shortcuts import render
from APP.models import Author, Book, Order, Category
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from APP.forms import AuthorForm, BookForm, CategoryForm, OrderForm
# Create your views here.

    
  
@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('dashboard/home_page')
    else:
        form = BookForm()
    context = { 
        'form': form,
    }
    return render(request, 'dashboardf/book_create.html', context=context)

def book_page(request):
    books = Book.objects.all()
    book_page_context = {
        'books': books,
    }
    return render(request, 'dashboardf/book.html', context=book_page_context)

def book_delete(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('dashboard/book')
    context = {   
        'book': book,   
    }
    return render(request, 'dashboardf/book_delete.html', context=context)

def book_update(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('dashboard/book')
    else:
        form = BookForm(instance=book)
    context = { 
        'book': book,
        'form': form,
    }
    return render(request, 'dashboardf/book_update.html', context=context)

def author(request):
    authors = Author.objects.all()
    author_page_context = {
        'authors': authors,
    }
    return render(request, 'dashboardf/author.html', context=author_page_context)  

def author_delete(request, id):
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        author.delete()
        return redirect('dashboard/author')
    return render(request, 'dashboardf/author_delete.html', {'author': author})

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard/author')
    else:
        form = AuthorForm()
    context = {
        'form': form
    }
    return render(request, 'dashboardf/author_create.html', context=context)

def author_update(request, id):
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('dashboard/author')
    else:
        form = AuthorForm(instance=author)

    return render(request, 'dashboardf/author_update.html', {'author': author, 'form': form})

def category(request):
    categories = Category.objects.all()
    category_page_context = {
        'categories': categories,
    }
    return render(request, 'dashboardf/category.html', context=category_page_context) 

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard/category')
    else:
        form = CategoryForm()
    context = {
        'form': form
    }
    return render(request, 'dashboardf/category_create.html', context=context)

def category_delete(request, id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        category.delete()
        return redirect('dashboard/category')
    return render(request, 'dashboardf/category_delete.html', {'author': author})

def category_update(request, id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('dashboard/category')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'dashboardf/category_update.html', {'category': category, 'form': form})

def order(request):
    orders = Order.objects.all()
    order_page_context = {
        'orders': orders,
    }
    return render(request, 'dashboardf/order.html', context=order_page_context) 

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard/order')
    else:
        form = OrderForm()
    context = {
        'form': form
    }
    return render(request, 'dashboardf/order_create.html', context=context)

def order_delete(request, id):
    order = Order.objects.get(id=id)
    if request.method == 'POST':
        order.delete()
        return redirect('dashboard/order')
    return render(request, 'dashboardf/order_delete.html', {'order': order})

def order_update(request, id):
    order = Order.objects.get(id=id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('dashboard/order')
    else:
        form = OrderForm(instance=order)

    return render(request, 'dashboardf/order_update.html', {'order': order, 'form': form})

