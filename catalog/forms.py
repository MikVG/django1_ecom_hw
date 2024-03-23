from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):

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


class VersionForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Version
        fields = ('version_number', 'version_name', 'current_version')
