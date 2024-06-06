from django.contrib import admin
from .models import Book, Author, Category, Order, OrderDetails
# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderDetails)
