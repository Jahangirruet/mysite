from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product_list/',views.product_list,name='product_list'),
    path('product_detail/',views.product_detail,name='product_detail'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('contact/',views.contact,name='contact'),
    ]