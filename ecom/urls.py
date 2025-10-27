from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin, messages
from django.contrib.auth import views
from django.contrib.auth import authenticate, login, logout
from django.urls import path, include


from cart.views import add_to_cart, cart, checkout
from product.views import product

urlpatterns = [
    path('', include('store.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
