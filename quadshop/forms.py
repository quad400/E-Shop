from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from .models import  Comment,Cart,UserProfile


class UserUpdate(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'input', 'placeholder':'Username'}),
            'email' : forms.EmailInput(attrs={'class': 'input', 'placeholder':'Email'}),
            'first_name' : forms.TextInput(attrs={'class': 'input', 'placeholder':'First Name'}),
            'last_name' : forms.TextInput(attrs={'class': 'input', 'placeholder':'Last Name'})
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'address', 'zip', 'city', 'country', 'image']
        widgets = {
            'phone' : forms.TextInput(attrs={'class': 'input', 'placeholder':'phone'}),
            'address' : forms.TextInput(attrs={'class': 'input', 'placeholder':'address'}),
            'zip' : forms.TextInput(attrs={'class': 'input', 'placeholder':'zip'}),
            'city' : forms.TextInput(attrs={'class': 'input', 'placeholder':'city'}),
            'country' : forms.TextInput(attrs={'class': 'input', 'placeholder':'country'}),
            'image': forms.FileInput(attrs={'class': 'input', 'placeholder':'image'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'content','rate']

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['quantity']

class CheckoutForm(forms.Form):

    # PAYMENT_CHOICES = (
    #     ('S', 'Stripe'),
    #     ('P', 'Paypal'),
    # )

    street_address = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder':'Street Address'}))
    apartment_address = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder':'Apartment Address'}),required=False)
    country = CountryField(blank_label='(select country)', ).formfield(
                        widget=CountrySelectWidget(attrs={'class': 'input form-control'}))
    zip = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder':'Zip'}))
    # same_billing_address = forms.BooleanField(widget=forms.CheckboxInput(),required=False)
    # save_info = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    # payment_option = forms.ChoiceField(widget=forms.RadioSelect(),
    #         choices=PAYMENT_CHOICES
    # )

class SearchForm(forms.Form):
    query = forms.CharField(max_length=225)
    category_id = forms.IntegerField()