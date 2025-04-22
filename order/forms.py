from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	DIVISION_CHOICES = (
		('Kabankalan City', 'Kabankalan City'),
		('Bacolod City', 'Bacolod City'),
		('Himamaylan City', 'Himamaylan City'),
		('Binalbagan', 'Binalbagan'),
		('Hinigaran', 'Hinigaran'),
	)

	DISCRICT_CHOICES = (
		('Brgy.1', 'Brgy.1'), 
		('Brgy.2', 'Brgy.2'),
		('Brgy.3', 'Brgy.3'),
		('Brgy.4', 'Brgy.4'),
		('Brgy.5', 'Brgy.5'),
	)

	PAYMENT_METHOD_CHOICES = (
		('Paypal', 'Paypal'),
		('Credit Card','Credit Card')
	)

	division = forms.ChoiceField(choices=DIVISION_CHOICES)
	district =  forms.ChoiceField(choices=DISCRICT_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'transaction_id']
