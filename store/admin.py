from django.contrib import admin
from .models import Size , Category , Product
# Register your models here.


admin.site.register(Category)

admin.site.register(Size)

admin.site.register(Product)