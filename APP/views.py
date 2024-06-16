from django.http import JsonResponse
from .forms import AuthorForm, BookForm, OrderForm
from .models import Author, Book, User, Order, Cart, CartItem, OrderItem
from .forms import AuthorForm, BookForm, CartItemForm
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, Http404

def home(request): 
    books = Book.objects.filter(is_featured=True)[:4]
    home_page_context = {
        'books': books,
    }
    return render(request, 'home_page.html', context=home_page_context)

def manager_book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 8)
    page_number = request.GET.get('page', 1)
    page = paginator.page(page_number)    
    return render(request, 'home_page.html', {'page': page, 'is_manager': True} )

def user_book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 8)
    page_number = request.GET.get('page', 1)
    page = paginator.page(page_number)    
    return render(request, 'shop.html', {'page': page, 'is_manager': False} )

def about(request):
    return render(request, 'about.html')


def book(request, id):
    book = Book.objects.get(id=id)
    booksCategory = Book.objects.filter(category=book.category).exclude(id = book.id)
    if request.method == 'POST':
        quantity = request.POST['qte']

        cart = Cart.objects.filter(user=request.user, is_paid=False)
        if not cart:
            cart = Cart.objects.create(user=request.user)
            CartItem.objects.create(cart=cart, book=book, quantity=quantity)
        else:
            CartItem.objects.create(cart=cart[0], book=book, quantity=quantity)

        return redirect('cart_page')
        
    context = {
        'book': book,  
        'booksCategory': booksCategory 
    }
    return render(request, 'book.html', context=context)


@login_required
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home_page')
    else:
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
    author_books = author.book_set.all() 
    return render(request, 'authors_details.html', {'author': author, 'author_books': author_books})




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
    return render(request, 'account_page.html')


def logout_view(request):
    logout(request)
    return render(request, 'home_page.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
            user.save()
            return redirect('login')
        else:
            return JsonResponse({'error': 'Passwords do not match'})
    return render(request, 'login.html')






@login_required
def cart_page(request):
    try:
        cart = Cart.objects.get(user=request.user, is_paid=False)
    except Cart.DoesNotExist:
        cart = None
    if cart:
        cart_items = CartItem.objects.filter(cart=cart)
    else:
        cart_items = []
    


    
    context = { 
        'cart': cart,
        'cart_items': cart_items
    }
    return render(request, 'Cart_page.html', context)
@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart = Cart.objects.get(user=request.user)
    form = CartItem(request.POST)
    
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(book=book, quantity=cd['quantity'])
        return JsonResponse({'message': 'Book added to cart successfully'})
    else:
        return JsonResponse({'error': 'Invalid form data'}, status=400)

@login_required
def checkout(request):
    try:
        cart = Cart.objects.get(user=request.user, is_paid=False)
    except Cart.DoesNotExist:
        cart = None
    if cart:
        cart_items = CartItem.objects.filter(cart=cart)
    else:
        cart_items = []

    if not cart_items:
        return redirect('cart_page')
    
    order = Order.objects.create(user=request.user)

    for cart_item in cart_items:
        OrderItem.objects.create(order=order, book=cart_item.book, quantity=cart_item.quantity)

    cart.is_paid = True
    cart.save()

    return redirect('book_list_user')

@login_required
def update_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    quantity = int(request.POST.get('quantity'))

    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
    return redirect('cart_page')


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('cart_page')


@login_required
def account_page(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_account.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, 'order_acc_details.html', {'order': order, 'order_items': order_items})


@login_required
def Contact_page(request):
    return render(request, 'Contact_page.html')