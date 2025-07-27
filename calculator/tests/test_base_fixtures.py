from django.test import TestCase
from calculator.models import Operation
from accounts.models import CalculatorUser


class TestCalculatorFixture(TestCase):
    def setUp(self):
        return super().setUp()

    def make_account(
            self,
            name='Test',
            email='Test@test.com',
            password='123456',
    ):
        return CalculatorUser.objects.create_user(
            name=name,
            email=email,
            password=password
        )

    def meke_operation(
        self,
        user=None,
        parameters='1 + 1 - 1',
        result='1',
    ):
        if user is None:
            user = self.make_account()

        return Operation.objects.create(
            user=user,
            parameters=parameters,
            result=result
        )
