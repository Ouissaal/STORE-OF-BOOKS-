from django.shortcuts import render, redirect
from .models import Author, Book, Order
from .forms import AuthorForm, BookForm, OrderForm
from .models import Author, Book
from .forms import AuthorForm, BookForm
from django.core.paginator import Paginator


def home(request): 
    books = Book.objects.all()
    home_page_context = {
        'books': books,
    }
    return render(request, 'home.html', context=home_page_context)

def manager_book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 8)
    page_number = request.GET.get('page', 1)
    page = paginator.page(page_number)    
    return render(request, 'home.html', {'page': page, 'is_manager': True} )

def user_book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 8)
    page_number = request.GET.get('page', 1)
    page = paginator.page(page_number)    
    return render(request, 'home.html', {'page': page, 'is_manager': False} )

def about(request):
    return render(request, 'about.html')


def book(request, id):
    book = Book.objects.get(id=id)
    context = {
        'book': book    
    }
    return render(request, 'book.html', context=context)


def create_book(request):
    if request.method == 'POST':
        # code to create a book
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home_page')
    else:
        # code to show the form
        form = BookForm()
    context = { 
        'form': form,
    }
    return render(request, 'create_book.html', context=context)

def update_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = BookForm(instance=book)
    context = { 
        'book': book,
        'form': form,
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
   
    return render(request, 'home_author.html', {'page': page, 'authors': authors})


def user_author_page(request):
    authors = Author.objects.all()
    paginator = Paginator(authors, 8)
    page_number = request.GET.get('page', 1)
    page = paginator.page(page_number)    
    return render(request, 'home_author.html', {'page': page, 'is_manager': False} )

def manager_author_page(request):
    authors = Author.objects.all()
    paginator = Paginator(authors, 8)
    page_number = request.GET.get('page', 1)
    page = paginator.page(page_number)
    return render(request, 'home_author.html', {'page': page, 'is_manager': True})
   
def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm()
    context = {
        'form': form
    }
    return render(request, 'create_author.html', context)

def update_author(request, id):
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm(instance=author)

    return render(request, 'manager/update_author.html', {'author': author, 'form': form})
    


def delete_author(request, id):
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        author.delete()
        return redirect('home')
    return render(request, 'delete_author.html', {'author': author})


def manager_page(request):
    return render(request, 'manager.html')
                  
def customer_page(request):
    return render(request, 'customer.html')



def manage_orders(request):
    if request.method == 'POST':       
        form = OrderForm(request.POST)

        if form.is_valid():
            book_id = form.cleaned_data['book_id']
            form.save()
            return redirect('order_detail', order_id=order_id)
    else:
        form = OrderForm()

    orders = Order.objects.all()
    context = { 
        'form': form,
        'orders': orders,
    }
    return render(request, 'order.html', context=context)
def __str__(self):
    return f"Order #{self.id} - {self.customer_name}"




def manage_order(request):
    orders = Order.objects.all()

    paginator = Paginator(orders, 4)

    page_number = request.GET.get('page', 1)

    page = paginator.page(page_number)
    return render(request, 'manage_order.html', {'page': page})

def order_page(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':       
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list_user')
    else:
        form = OrderForm(initial={'book': book})

    context = { 
        'form': form,
        'book_id': id,
    }
    return render(request, 'order_page.html', context=context)

def details_of_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    return render(request, 'order_details.html', {'order': order})
    


def details_of_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('manage_order')
    else:
        form = OrderForm(instance=order)
    return render(request, 'order_details.html', {'order': order})

def Home_page(request):
    books = Book.objects.filter(is_featured=True)[:4]
    return render(request, 'Home_page.html', {'books': books})



def author_details(request, id):
    author = Author.objects.get(id=id)
    return render(request, 'authors_details.html', {'author': author})

def account_page(request):
    return render(request, 'account_page.html')