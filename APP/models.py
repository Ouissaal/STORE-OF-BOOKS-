from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100, validators=[
        RegexValidator(
            regex='^[a-zA-Z]*$',
            message='Name must be Alphabetic',
            code='invalid name'
        )
    ])
    birth_date = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=50, null=True)
    publication_year = models.PositiveIntegerField(null=True, blank=True , default='2000')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, default='Category')

    def __str__(self):
        return self.title


class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    )

    customer_name = models.CharField(max_length=100)
    order_date = models.DateField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='Pending')
    books = models.ManyToManyField(Book)

    def __str__(self):
        return f"Order #{self.pk} - {self.customer_name}"
