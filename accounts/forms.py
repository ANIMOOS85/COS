
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from .models import Profile

# from models import




class RegisterForm(forms.ModelForm):
    password = forms.CharField(label="رمز عبور", widget=forms.PasswordInput)
    password2 = forms.CharField(label="تکرار رمز عبور", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')   # نام کاربری و ایمیل از مدل User

    def clean_password2(self):
        # این متد خودکار توسط فرم صدا زده می‌شود برای اعتبارسنجی فیلد password2
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password2')
        if not p1 or not p2:
            raise ValidationError("هر دو فیلد رمز باید پر شوند.")
        if p1 != p2:
            raise ValidationError("رمزها یکسان نیستند.")
        return p2

class ProfileEditForm(forms.ModelForm):
    email = forms.EmailField(label="ایمیل", required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
        }
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
