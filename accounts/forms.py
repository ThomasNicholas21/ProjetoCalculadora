from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from accounts.models import CalculatorUser


class SignUpForm(forms.ModelForm):
    class Meta:
        model = CalculatorUser
        fields = [
            'name', 'email'
        ]

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Insira seu nome'
            }
        ),
        required=True,
        label='Nome Completo'
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Insira seu e-mail'
            }
        ),
        required=True,
        label='E-mail'
    )
    password1 = forms.CharField(
        label='Senha',
        strip=False,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Insira sua senha'
            }
        ),
        help_text=password_validation.password_validators_help_text_html()
    )
    password2 = forms.CharField(
        label='Confirmação de Senha',
        strip=False,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirme sua senha'
            }
        ),
        help_text='Use a mesma senha de antes'
    )

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            password_validation.validate_password(password1)

        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError(
                'As senhas não coincidem.'
            )

        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if CalculatorUser.objects.filter(email=email).exists():
            raise ValidationError(
                'E-mail já cadastrado!'
            )

        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user
