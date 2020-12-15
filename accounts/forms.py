from django import forms
from django.contrib.auth import get_user_model
from .models import UserAddress
User=get_user_model()

class UserAddressForm(forms.ModelForm):
    default = forms.BooleanField(label='Make Default')
    class Meta:
        model=UserAddress
        fields=["address","address2","city","state","country","zipcode","phone","shipping"]



class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username=self.cleaned_data.get('username')
        try:
            user=User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Are you sure you are registered?")
        return username

    def clean_password(self):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')

        try:
            user=User.objects.get(username=username)
        except:
            user=None
        if user is not None and not user.check_password(password):
            raise forms.ValidationError("invalid password")
        elif user is None:
            pass
        else:
            return password

class RegistrationForm(forms.ModelForm):
    email=forms.EmailField(label="Your email")
    password1=forms.CharField(label='password',widget=forms.PasswordInput())
    password2=forms.CharField(label='password confirmation',widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','email']

    def clean_email(self):
        email=self.cleaned_data.get('email')

        user_count=User.objects.filter(email=email).count()
        if user_count>0:
            raise forms.ValidationError("this email is already registered,Please check and try again")
        return email

    def clean_password2(self):
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError("password does not match")
        return password2

    def save(self,commit=True):
        user=super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
