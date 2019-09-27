from . models import Products
from django.forms import ModelForm



class ProductsForm(ModelForm):
    class Meta():
        model = Products
        fields = '__all__'