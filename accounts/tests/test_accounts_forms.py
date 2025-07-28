from .test_base_fixture import TestAccountsFixture
from accounts.forms import SignUpForm


class TestAccountsForms(TestAccountsFixture):
    def test_password_is_invalid_if_too_common(self):
        data = self.make_form_data()
        data['password1'] = '123456'
        data['password2'] = '123456'

        form = SignUpForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn('password1', form.errors)
        self.assertIn(
            (
                'Esta senha é muito curta. Ela precisa '
                'conter pelo menos 8 caracteres.'
            ),
            form.errors['password1'][0]
        )

    def test_passwords_must_match(self):
        data = self.make_form_data()
        data['password1'] = 'umaSenhaForte123'
        data['password2'] = 'senhaDiferente456'

        form = SignUpForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)
        self.assertEqual(
            form.errors['password2'][0], 'As senhas não coincidem.'
        )

    def test_email_must_be_unique(self):
        existing_user_data = self.make_form_data()
        self.make_account(
            name=existing_user_data['name'],
            email=existing_user_data['email'],
            password=existing_user_data['password1']
        )

        form = SignUpForm(data=existing_user_data)

        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        self.assertEqual(form.errors['email'][0], 'E-mail já cadastrado!')
