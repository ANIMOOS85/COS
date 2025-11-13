from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Cart, CartItem
from django.contrib import messages


# 🏠 صفحه اصلی
def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, "store/home.html", {
        'products': products,
        'categories': categories,
    })


# 🛍 نمایش دسته‌بندی‌ها
def store(request):
    categories = Category.objects.all()
    return render(request, "store/category.html", {
        'categories': categories,
    })


# 📦 محصولات یک دسته‌بندی خاص
def category_product(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.product_set.all()
    categories = Category.objects.all()
    return render(request, "store/category_product.html", {
        'category': category,
        'products': products,
        'categories': categories,
    })


# 🛒 افزودن محصول به سبد خرید
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # 🔹 تشخیص نوع کاربر
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
        cart, created = Cart.objects.get_or_create(session_id=request.session.session_key)

    # 🔹 افزودن یا افزایش تعداد محصول
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f"✅ {product.name} به سبد خرید اضافه شد.")
    return redirect('store:cart_detail')


# 🧾 جزئیات سبد خرید
def cart_detail(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
        cart = Cart.objects.filter(session_id=request.session.session_key).first()

    categories = Category.objects.all()
    return render(request, "store/cart_detail.html", {
        "cart": cart,
        "categories": categories,
    })


# ❌ حذف آیتم از سبد خرید
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    messages.warning(request, "🗑️ محصول از سبد خرید حذف شد.")
    return redirect('store:cart_detail')
