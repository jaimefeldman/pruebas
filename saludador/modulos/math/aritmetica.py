# -*- coding: utf-8 -*-
"""
    calculadora.aritmetica
    ~~~~~~~~~~~~~~~~~~~~~~

    CALCULOS ARITMETICOS.

    :copyright: (c) 2022 by Jaime Feldman.
    :license: MIT, see LICENSE for more details.
"""

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def mutiplica(a, b):
    return a * b

def divide(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        return a / b

