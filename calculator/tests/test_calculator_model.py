from .test_base_fixtures import TestCalculatorFixture
from django.core.exceptions import ValidationError
from parameterized import parameterized


class TestCalculatorModel(TestCalculatorFixture):
    def setUp(self):
        self.calculator = self.meke_operation()
        return super().setUp()

    @parameterized.expand(
            [
                ('parameters', 128),
                ('result', 128)
            ]
    )
    def test_calculator_max_lenght_fields(self, field, max_length):
        setattr(self.calculator, field, 'Test' * max_length)
        with self.assertRaises(ValidationError):
            self.calculator.full_clean()
