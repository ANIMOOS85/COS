from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from django.shortcuts import render

# --- صفحه 404 سفارشی ---
def custom_404(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),   # اگر اپ اصلیت store هست
    path('accounts/', include('accounts.urls')),  # اگر داری
]
