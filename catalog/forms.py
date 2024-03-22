from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price')

    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    def clean_name(self):
        create_data = self.cleaned_data['name']
        if create_data in self.forbidden_words:
            raise ValidationError('Нельзя использовать запрещенное слово в названии')
        return create_data

    def clean_description(self):
        create_data = self.cleaned_data['description']
        if create_data in self.forbidden_words:
            raise ValidationError('Нельзя использовать запрещенное слово в описании')
        return create_data
