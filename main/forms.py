from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        # fields = ["gambar","name", "price", "stok", "description"]
        fields = ['name', 'amount', 'description', 'price', 'gambar']