from django import forms
from django.core.exceptions import ValidationError 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer


# validators field

def validate_number(value):
    cc=str(value)
    
    if cc.startswith("+880"):
        pass
    else:
        raise ValidationError("Oops! plz use +880 in your number ")


def validate_check_mail(value): 
    if value.endswith("@gmail.com"):
        pass
    elif value.endswith("@yahoo.com"):
        pass
    else: 
        raise ValidationError("Oops! we only accept Gmail and Yahoo mail. ")



def validate_check_mail_valided(value): 
    if value.endswith("@gmail.com"):
        pass
    elif value.endswith("@yahoo.com"):
        pass
    else: 
        raise ValidationError("Oops! Enter valid email. ")





def validate_email(value):
    try:
        log_cus=User.objects.get(email=value)
                    
    except:
        log_cus=User.objects.filter(email=value)

    if log_cus:
        raise ValidationError("Oops!This email is already exists . ")
    else:
        pass




# class CustomerRegistrationForm(forms.Form):
#     first_name=forms.CharField(required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
#     last_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     email=forms.CharField(required=True,validators=[validate_check_mail,validate_email],widget=forms.EmailInput(attrs={"class":"form-control"}))
#     password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
#     password2=forms.CharField(label="Confirm password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
#     number=forms.CharField(validators=[validate_number],required=True,label= _("Mobile number"),max_length=14,min_length=14, widget=forms.TextInput(attrs={"class":"form-control","placeholder":"start with +880"}))
#     address=forms.CharField(required=True,max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))





    
    





class CustomerRegistrationForm(UserCreationForm):
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(label="Confirm password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    
    email=forms.CharField(required=True,validators=[validate_check_mail,validate_email],widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    number=forms.CharField(validators=[validate_number],required=True,label= _("Mobile number"),max_length=14,min_length=14, widget=forms.TextInput(attrs={"class":"form-control","placeholder":"start with +880"}))
    address=forms.CharField(required=True,max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    city=forms.CharField(required=True,max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model= User
        fields=["first_name","email","password1","password2"]
        labels={"email":"Email"}
        widgets ={"username":forms.TextInput(attrs={"class":"form-control"}),"first_name":forms.TextInput(attrs={"class":"form-control"}),"last_name":forms.TextInput(attrs={"class":"form-control"})}







class LoginForm(forms.Form):

    email =forms.CharField(validators=[validate_check_mail_valided],widget=forms.EmailInput(attrs={"class":"form-control"}))
    password =forms.CharField(label=_("password"),strip=False,widget=forms.PasswordInput(attrs={"autocomplete":"current-password","class":"form-control"}))




class ChangePassword(PasswordChangeForm):
    old_password=forms.CharField(label= _("Old Password"),widget=forms.PasswordInput(attrs={"class":"form-control","autocomplete":"current-password","autofocus":True}),strip=False)
    new_password1=forms.CharField(label= _("New Password"),widget=forms.PasswordInput(attrs={"class":"form-control","autocomplete":"new-password"}),strip=False,help_text=password_validation.password_validators_help_text_html())
    new_password2=forms.CharField(label= _("Confirm Password"),widget=forms.PasswordInput(attrs={"class":"form-control","autocomplete":"new-password"},),strip=False)
    


class MyPasswordResetForm(PasswordResetForm):
    email=forms.EmailField(label= _("Email"),max_length=254,widget=forms.EmailInput(attrs={"autocomplete":"email","class":"form-control"}))



class MySetPassword(SetPasswordForm):
    new_password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    new_password2=forms.CharField(label="Confirm password",widget=forms.PasswordInput(attrs={"class":"form-control"}))




class CustomerProfile(forms.ModelForm):
    number=forms.CharField(validators=[validate_number],required=True,label= _("Mobile number"),max_length=14,min_length=14, widget=forms.TextInput(attrs={"class":"form-control","placeholder":"start with +880"}))
    
    class Meta:
        model = Customer
        fields = ["name","number","locality","city"]
        labels={"number":"Phone-num","locality":"Address"}
        widgets={"name":forms.TextInput(attrs={"class":"form-control"}),
        
        "locality":forms.TextInput(attrs={"class":"form-control"}),
        "city":forms.Select(attrs={"class":"form-control"}),}


# def Nm(pk):
#     return print(pk)



class Edit_Address(forms.Form):
    name=forms.CharField(required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    mobile=forms.CharField(validators=[validate_number],required=True,label= _("Mobile number"),max_length=14,min_length=14, widget=forms.TextInput(attrs={"class":"form-control","placeholder":"start with +880"}))
    address=forms.CharField(required=True,max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    city=forms.CharField(required=True,max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
  




        
        

