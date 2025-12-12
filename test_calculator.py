
import pytest

from calculator import Calculator
class TestCalculator:
    @pytest.fixture
    def calc(self):
        return Calculator()
    def test_add(self,calc):
        assert calc.add(3,5) == 8
    def test_sub(self,calc):
        assert calc.subtract(5,3) == 2