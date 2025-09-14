"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

import os 
import sys 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from calculator import Calculator

def test_app():
    calc = Calculator()
    assert calc.get_hello_message() == "== Calculatrice v1.0 =="

def test_addition():
    calc = Calculator()
    assert calc.addition(5, 3) == 8

def test_subtraction():
    calc = Calculator()
    assert calc.subtraction(205, 115) == 90

def test_multiplication():
    calc = Calculator()
    assert calc.multiplication(35, 43) == 1505

def test_division():
    calc = Calculator()
    assert calc.division(5, 2) == 2.5