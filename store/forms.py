from .models import  Product 
from django import forms



class cpz(forms.ModelForm):
    class Meta:
        fields = ['name' , 'title' , 'category' , 'price' , 'size' , 'image']
        
