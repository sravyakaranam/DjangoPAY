"""offlineWallet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from products.views import view_products,addtocart
from accounts.models import Account
from accounts.views import signup,profile,viewall,login,Acc_view,Dummy,logout
from products.views import view_products,addtocart,viewcart,deleteproduct,buynow,savetodb

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('signup/',signup,name='signup'),
    path('profile/',profile,name='profile'),
    path('dummy/',Dummy),
    path('login/',login,name='login'),
    path('logout/',savetodb),
    path('',viewall),
    path('accview/',Acc_view),
     path('proview/',view_products),
    path('proview/added',view_products),
    path('proview/viewcart/',viewcart),
    path('proview/addtoart/',viewcart),
    path('addtocart/<str:id>/',addtocart),
    path('deleteproduct/<str:id>',deleteproduct),
    path('buynow/<str:id>/',buynow),
   
]
