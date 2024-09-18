import math

import pytest
import shapes


class TestCircle:

    def setup_method(self, method):
        """
        Isso define coisas que ficam disponíveis para
        todos os testes
        """
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        """
        Isso limpa as coisas que foram definidas no método
        """
        print(f"Tearing down {method}")
        del self.circle

    def test_radios(self):
        assert self.circle.area() == math.pi * self.circle.radios ** 2

    def test_two(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radios
        assert result == expected
