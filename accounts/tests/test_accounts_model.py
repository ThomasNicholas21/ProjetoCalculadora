from .test_base_fixture import TestAccountsFixture
from django.core.exceptions import ValidationError
from accounts.models import CalculatorUser


class TestAccountModel(TestAccountsFixture):
    def setUp(self):
        self.account_default: CalculatorUser = self.make_account()
        self.account_admin: CalculatorUser = self.make_account_admin()
        return super().setUp()

    def test_account_max_lenght(self):
        setattr(self.account_default, 'name', 'Test' * 128)
        with self.assertRaises(ValidationError):
            self.account_default.full_clean()

    def test_account_create_super_user(self):
        admin_account = self.account_admin
        self.assertEqual(admin_account.is_staff, True)

    def test_account_methods(self):
        perm = 'accounts.test_event'
        app_label = 'event'
        self.account_default.name = 'str_method_name'
        self.account_default.full_clean()
        self.account_default.save()

        self.assertEqual(self.account_default.has_perm(perm=perm), True)
        self.assertEqual(
            self.account_default.has_module_perms(app_label=app_label), True
        )
        self.assertEqual(str(self.account_default), 'str_method_name')

    def test_account_no_email_valueerror(self):
        with self.assertRaises(ValueError):
            self.make_account(email=None)
