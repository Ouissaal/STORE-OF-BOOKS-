from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('home_page/', views.home, name='home_page'),
    path("manager/book_list", views.manager_book_list, name="book_list_manager"),
    path("user/book_list", views.user_book_list, name="book_list_user"),
    path('user/about/', views.about, name='about'),
    path('user/book/<int:id>', views.book, name='book'),
    path('manager/create_book', views.create_book, name='create_book'),
    path('manager/update_book/<int:id>', views.update_book, name='update_book'),
    path('manager/delete_book/<int:id>', views.delete_book, name='delete_book'),
    path('user/author_list', views.user_author_page, name='user_author_page'),
    path('manager/author_list', views.manager_author_page, name='manager_author_page'),
    path('manager/create_author/', views.create_author, name='create_author'),
    path('manager/update_author/<int:id>/', views.update_author, name='update_author'),
    path('manager/delete_author/<int:id>/', views.delete_author, name='delete_author'),
    path('manager/', views.manager_page, name='manager_page'),
    path('user/customer_page/', views.customer_page, name='customer_page'), 
    path('user/create_order/<int:id>', views.order_page, name='create_order'),
    path('manager/manage_orders/', views.manage_order, name='manage_order'),
    path('manager/order_details/<int:order_id>/', views.details_of_order, name='Order_Details'),
    path('', views.Home_page, name='Home_page'),
    path('user/author_details/<int:id>', views.author_details, name='author_details'),
    path('login_view/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('Cart/', views.cart_page, name='cart_page'),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('account/', views.account_page, name='account_page'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('contact/', views.Contact_page, name='contact')
   
]
