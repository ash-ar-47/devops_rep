#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Unit test for the calculator library """

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_addition2(self):
        assert 5 == calculator.add(2, 3)

    def test_substraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)

    def test_division(self):
        assert 11 == calculator.divide(121, 11)
