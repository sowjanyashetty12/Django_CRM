from django import forms
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from .models import Record

class SignUpForm(UserCreationForm):
    email=forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    first_name=forms.CharField(label="", max_length=30 , widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'FirstName'}))
    last_name=forms.CharField(label="", max_length=30 , widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'SecondName'}))
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')

    # we'll add all the attrs to username password1 and password2
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

class AddNewRecordForm(forms.ModelForm):

    # feilds name here should be same as in model or else it'll add extra feild in the form

    first_name=forms.CharField( max_length=20, required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    last_name=forms.CharField( max_length=20, required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    
    email=forms.CharField( max_length=20, required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
    phone_number=forms.CharField( max_length=20, required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone Number", "class":"form-control"}), label="")
    city=forms.CharField( max_length=20, required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
    class Meta:
        model=Record
        fields = '__all__'