from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class  SignUpForm(UserCreationForm):
	email = forms.EmailField(widget = forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Input Title'}))
	first_name = forms.CharField(max_length = 100, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input Title'}))
	last_name = forms.CharField(max_length = 100,widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input Title'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')



	def __init__(self, *args, **kwards):
		super(SignUpForm, self).__init__(*args, **kwards)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'