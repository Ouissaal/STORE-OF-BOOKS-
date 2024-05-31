from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('about/', views.about, name='about'),
    path('book/<int:id>', views.book, name='book'),
    path('create_book/', views.create_book, name='create_book'),

]