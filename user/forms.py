from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='İsim ')
    last_name = forms.CharField(max_length=50, label='Soyisim ')
    email = forms.EmailField(required=True, label='Email ')
    username = forms.CharField(max_length=50, label='Kullanıcı Adi ')
    password = forms.CharField(max_length=20, label='Parola Giriniz ', widget = forms.PasswordInput)
    confirm_password = forms.CharField(max_length=20, label='Parolayı Doğrulayınız ', widget = forms.PasswordInput)
    
    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Girdiğiniz parolalar eşleşmiyor')
        
        values = {
            'first_name' : first_name,
            'last_name' : last_name,
            'email' : email,
            'username' : username,
            'password' : password
        }

        return values

class LoginForm(forms.Form):
    username = forms.CharField(label='Kullanıcı Adı ', required=True)
    password = forms.CharField(label = 'Parola ', widget = forms.PasswordInput, required=True)