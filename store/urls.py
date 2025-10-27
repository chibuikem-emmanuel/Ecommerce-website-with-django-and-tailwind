from django.urls import path
from store.views import frontpage, shop, signup, login_user, logout_user, myaccount, edit_myaccount
from product.views import product
from django.contrib.auth import views
from django.contrib.auth import authenticate, login, logout

urlpatterns = [
    path('shop/', shop, name='shop'),
    path('myaccount/', myaccount, name='myaccount'),
    path('myaccount/edit/', edit_myaccount, name='edit_myaccount'),
    path('shop/<slug:slug>/', product, name='product'),
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/',logout_user, name='logout'),
    path('login/', login_user, name='login'),
   
]
