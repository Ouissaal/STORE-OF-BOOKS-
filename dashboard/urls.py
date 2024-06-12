from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
urlpatterns = [
    path('book_create/', views.book_create, name='book_create'),
    path('', views.book_page, name='book'),
    path('book_delete/<int:id>', views.book_delete, name='book_delete'),
    path('book_update/<int:id>', views.book_update, name='book_update'),
    path('author/', views.author, name='author'),
    path('author_create/', views.author_create, name='author_create'),
    path('author_delete/<int:id>/', views.author_delete, name='author_delete'),
    path('author_update/<int:id>/', views.author_update, name='author_update'),
    path('category/', views.category, name='category'),
    path('category_create/', views.category_create, name='category_create'),
    path('category_delete/<int:id>', views.category_delete, name='category_delete'),
    path('category_update/<int:id>', views.category_update, name='category_update'),
    path('order/', views.order, name='order'),
    path('order_create/', views.order_create, name='create_order'),
    path('order_delete/<int:id>', views.order_delete, name='order_delete'),
    path('order_update/<int:id>', views.order_update, name='order_update'),
    
]