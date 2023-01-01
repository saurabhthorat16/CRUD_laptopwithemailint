from django import forms
from .models import Laptop

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'
        lables = {
            'lid': 'LAPTOP ID',
            'brand_name': 'BRAND NAME',
            'model_name': 'MODEL NAME',
            'price': 'PRICE',
            'rom':  'ROM',
            'ram': 'RAM',
            'SSD': 'SSD',
            'HDD': 'HDD',
            'Weight': 'WEIGHT',
            'year': 'YEAR'
        }