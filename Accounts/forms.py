from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,SetPasswordForm
from django import forms
from django.contrib.auth.models import User
from Ecommerce_Core.models import Profile


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		exclude = ['user','joined_at','saved_cart']

	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)

		self.fields['first_name'].widget.attrs['class'] = 'form-control'
		self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
		self.fields['first_name'].label = ''
		self.fields['first_name'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['last_name'].widget.attrs['class'] = 'form-control'
		self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
		self.fields['last_name'].label = ''
		self.fields['last_name'].required = False 


		self.fields['number'].widget.attrs['class'] = 'form-control'
		self.fields['number'].widget.attrs['placeholder'] = 'Number'
		self.fields['number'].label = ''
		self.fields['number'].required = False 

		self.fields['address'].widget.attrs['class'] = 'form-control'
		self.fields['address'].widget.attrs['placeholder'] = 'Address'
		self.fields['address'].label = ''
		self.fields['address'].required = False 

		self.fields['city'].widget.attrs['class'] = 'form-control'
		self.fields['city'].widget.attrs['placeholder'] = 'City'
		self.fields['city'].label = ''
		self.fields['city'].required = False 

		self.fields['country'].widget.attrs['class'] = 'form-control'
		self.fields['country'].widget.attrs['placeholder'] = 'Country'
		self.fields['country'].label = ''
		self.fields['country'].required = False 

		self.fields['zip_code'].widget.attrs['class'] = 'form-control'
		self.fields['zip_code'].widget.attrs['placeholder'] = 'Zip Code'
		self.fields['zip_code'].label = ''
		self.fields['zip_code'].required = False 

		self.fields['gender'].widget.attrs['class'] = 'form-control'
		self.fields['gender'].widget.attrs['placeholder'] = 'Gender'
		self.fields['gender'].label = ''
		self.fields['gender'].required = False 

class ChangePasswordForm(SetPasswordForm):
	class Meta:
		model = User
		fields = ['new_password1','new_password2']
	def __init__(self, *args, **kwargs):
		super(ChangePasswordForm, self).__init__(*args, **kwargs)

		self.fields['new_password1'].widget.attrs['class'] = 'form-control'
		self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['new_password1'].label = ''
		self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['new_password2'].widget.attrs['class'] = 'form-control'
		self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['new_password2'].label = ''
		self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
		

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'})
    )


class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))

	class Meta:
		model = User
		fields = ('username','email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
		