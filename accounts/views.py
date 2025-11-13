from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm , ProfileEditForm  , ProfileForm , Profile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # ورود خودکار بعد از ثبت‌نام
            login(request, user)
            messages.success(request, f"{user.username} خوش آمدی! ثبت‌نام با موفقیت انجام شد.")
            return redirect('accounts:profile')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"خوش آمدی {user.username}!")
            return redirect('accounts:profile')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, "شما خارج شدید.")
    return redirect('store:store')


@login_required
def profile_view(request):
    # اگر پروفایل کاربر وجود نداشت، ساخته شود
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    return render(request, 'accounts/profile.html', {
        'profile': profile
    })
@login_required
def edit_profile_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        user_form = ProfileEditForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "پروفایل با موفقیت به‌روزرسانی شد.")
            return redirect('accounts:profile')
    else:
        user_form = ProfileEditForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'accounts/edit_profile.html', context)
