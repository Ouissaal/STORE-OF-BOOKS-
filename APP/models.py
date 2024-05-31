from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100, validators=[
        RegexValidator(
            regex='^[a-zA-Z]*$', 
            message='Name must be Alphabetic', 
            code='invalid_name'
        )
    ])
    birth_date = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=50, null=True)
    publication_year = models.PositiveIntegerField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.title



# Create your models here.
