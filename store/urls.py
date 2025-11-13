from . import views
from django.urls import path



app_name = "store"


urlpatterns = [
    

     path('', views.home, name='home'),
     path('store/' , views.store , name='store'),  
     path('category/<int:category_id>/', views.category_product, name='category_product'),
     path('cart/', views.cart_detail, name='cart_detail'),
     path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
     path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    
]
