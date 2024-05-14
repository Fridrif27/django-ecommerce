import re
from django import forms


class CreateOrderForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    card_number = forms.CharField()
    payment_on_get = forms.ChoiceField(
        choices=[
            ("0", 'False'),
            ("1", 'True'),
            ],
        )

    def clean_card_number(self):
        data = self.cleaned_data['card_number']

        if not data.isdigit():
            raise forms.ValidationError("The card number must contain only numbers")
        
        pattern = re.compile(r'^\d{16}$')
        if not pattern.match(data):
            raise forms.ValidationError("Invalid number format")

        return data
