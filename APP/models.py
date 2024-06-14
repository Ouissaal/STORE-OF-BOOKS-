from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    address = models.CharField(max_length=100, default='')


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='book_image/', blank=True, null=True)
   

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=50, null=True)
    publication_year = models.PositiveIntegerField(null=True, blank=True , default='2000')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='book_image/', null=True, blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    )

    customer_name = models.CharField(max_length=100)
    order_date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='Pending')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order #{self.pk} - {self.customer_name}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    create_at = models.TimeField(auto_now=True)
    is_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Cart {self.id} for {self.user.username}'
    def total_price(self):
        return sum(item.book.price * item.quantity for item in self.cart_items.all())

    
class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE, related_name='cart_items')
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
        
    def __str__(self):
        return f'{self.quantity} x {self.book.title if self.book else "Unknown Book"} in Cart {self.cart.id}'

    def get_total_price(self):
        if self.book:
            return self.book.price * self.quantity
        return 0
    
