from django.urls import path
from . import views

urlpatterns = [
    path('home_page/', views.home, name='home_page'),
    path('about/', views.about, name='about'),
    path('book/<int:id>', views.book, name='book'),
    path('create_book/', views.create_book, name='create_book'),
    path('update_book/<int:id>', views.update_book, name='update_book'),
    path('delete_book/<int:id>', views.delete_book, name='delete_book'),
    path('home/', views.home_author, name='home'),
    path('create_author/', views.create_author, name='create_author'),
    path('update_author/<int:id>/', views.update_author, name='update_author'),
    path('delete_author/<int:id>/', views.delete_author, name='delete_author'),
    path('', views.cart_page, name='cart_page'),
    path('manager/', views.manager_page, name='manager_page'),
    path('customer_page/', views.customer_page, name='customer_page'), 
    path('manage_orders/', views.manage_orders, name='manage_orders'),
    path('order_detail/<int:order_id>', views.order_detail, name='order_detail'),
]

