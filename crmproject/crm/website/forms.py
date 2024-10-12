from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer



class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dirección de correo electrónico'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Requerido. 150 caracteres o menos. Solo letras, dígitos y @/./+/-/_.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Tu contraseña no puede ser muy similar a tu otra información personal.</li><li>Tu contraseña debe contener al menos 8 caracteres.</li><li>Tu contraseña no puede ser una contraseña comúnmente utilizada.</li><li>Tu contraseña no puede ser completamente numérica.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar contraseña'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Introduce la misma contraseña que antes, para verificación.</small></span>'

# Formulario para agregar un registro
class AddCustomerForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder": "Primer nombre", "class": "form-control"}), 
        label=""
    )
    last_name = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder": "Apellido", "class": "form-control"}), 
        label=""
    )
    email = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder": "Email", "class": "form-control"}), 
        label=""
    )
    phone = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder": "Celular", "class": "form-control"}), 
        label=""
    )
    address = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder": "Dirección", "class": "form-control"}), 
        label=""
    )
    city = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder": "Ciudad", "class": "form-control"}), 
        label=""
    )
    country = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder": "Pais", "class": "form-control"}), 
        label=""
    )

    class Meta:
        model = Customer
        exclude = ("user",)
