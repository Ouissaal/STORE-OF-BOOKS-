from django import forms

from .models import Author, Book, Order

from .models import Author, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date', 'nationality']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control'}),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title',
                  'genre',
                  'publication_year',
                  'author',
                  'price',
                  'category',
                  'image',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control ', 'style': 'width: 400px; height: 40px; margin: auto;'}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 400px; height: 40px; margin: auto;'}),
            'publication_year': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 400px; height: 40px; margin: auto;'}),
            'author': forms.Select(attrs={'class': 'form-control', 'style': 'width: 400px; height: 40px; margin: auto;'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 400px; height: 40px; margin: auto;'}),
            'category': forms.Select(attrs={'class': 'form-control', 'style': 'width: 400px; height: 40px; margin: auto;'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'style': 'width: 400px; height: 40px; margin: auto;'})
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'book']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'book': forms.Select(attrs={'class': 'form-control'}),
           
        }
