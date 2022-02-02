"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
#from accounts import urls


urlpatterns = [
    #path('',include('myapp.urls')),
    path('',views.index,name='index'),    
   path('product_list/',views.product_list,name='product_list'),
   path('product_detail/',views.product_detail,name='product_detail'),
   path('login/',views.login,name='login'),
   # path('my-account/',views.my-account,name="my-account"),
   path('my-account/',views.MyAccount,name='MyAccount'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('contact/',views.contact,name='contact'),

    #path('login/',include('accounts.urls')),
    path('signup/',views.signup,name='signup'),
    #path('signup/', views.signup, name='signup'),
    #path('login/', views.login, name='login'),

    path('admin/', admin.site.urls),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)