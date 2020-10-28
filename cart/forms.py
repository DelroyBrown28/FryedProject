
from django.contrib.auth import get_user_model
from django import forms
from .models import (OrderItem, Product,
                     SizeVariation, Address)


User = get_user_model()


class AddToCartForm(forms.ModelForm):
    size = forms.ModelChoiceField(queryset=SizeVariation.objects.none())
    quantity = forms.IntegerField(min_value=1)

    class Meta:
        model = OrderItem
        fields = ['quantity', 'size']

    def __init__(self, *args, **kwargs):
        self.product_id = kwargs.pop('product_id')
        product = Product.objects.get(id=self.product_id)
        super().__init__(*args, **kwargs)

        self.fields['size'].queryset = product.available_sizes.all()

    def clean(self):
        product_id = self.product_id
        product = Product.objects.get(id=self.product_id)
        quantity = self.cleaned_data['quantity']
        if product.stock <= quantity:
            raise forms.ValidationError(
                f"Sorry, I only have {product.stock} of these available")


class AddressForm(forms.Form):
    selected_shipping_address = forms.ModelChoiceField(
        Address.objects.none(), required=False
    )
    selected_billing_address = forms.ModelChoiceField(
        Address.objects.none(), required=False
    )
    shipping_address_line_1 = forms.CharField(required=False)
    shipping_address_line_2 = forms.CharField(required=False)
    shipping_zip_code = forms.CharField(required=False)
    shipping_city = forms.CharField(required=False)
    billing_address_line_1 = forms.CharField(required=False)
    billing_address_line_2 = forms.CharField(required=False)
    billing_zip_code = forms.CharField(required=False)
    billing_city = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id')
        super().__init__(*args, **kwargs)

        # user = User.objects.get(id=user_id)

        shipping_address_queryset = Address.objects.filter(
            # user=user,
            address_type='S'
        )

        billing_address_queryset = Address.objects.filter(
            # user=user,
            address_type='B'
        )

        self.fields['selected_shipping_address'].queryset = shipping_address_queryset
        self.fields['selected_billing_address'].queryset = billing_address_queryset

    def clean(self):
        data = self.cleaned_data

        selected_shipping_address = data.get('selected_shipping_address', None)
        if selected_shipping_address is None:
            if not data.get('shipping_address_line_1', None):
                self.add_error("shipping_address_line_1",
                               "PLEASE, I NEED THE INFO!")
            if not data.get('shipping_address_line_2', None):
                self.add_error("shipping_address_line_2",
                               "PLEASE, I NEED THE INFO!")
            if not data.get('shipping_zip_code', None):
                self.add_error("shipping_zip_code", "PLEASE, I NEED THE INFO!")
            if not data.get('shipping_city', None):
                self.add_error("shipping_city", "PLEASE, I NEED THE INFO!")

        selected_billing_address = data.get('selected_billing_address', None)
        if selected_billing_address is None:
            if not data.get('billing_address_line_1', None):
                self.add_error("billing_address_line_1",
                               "PLEASE, I NEED THE INFO!")
            if not data.get('billing_address_line_2', None):
                self.add_error("billing_address_line_2",
                               "PLEASE, I NEED THE INFO!")
            if not data.get('billing_zip_code', None):
                self.add_error("billing_zip_code", "PLEASE, I NEED THE INFO!")
            if not data.get('billing_city', None):
                self.add_error("billing_city", "PLEASE, I NEED THE INFO!")
