#!/usr/bin/env python3.7
"""
Imprime a tabiada do 1 ao 10.
Tabuada do 1 ao 10
"""
__version__ = "0.1.0"
__author__ = "Raphael"

#base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
from traceback import print_tb


numeros = (list(range(1,11)))

#itarable (Percorriveis )

#para cada número em números
for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("--------------")
