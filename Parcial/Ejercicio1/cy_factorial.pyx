#cython: language_level=3

cimport cython

'''
Fecha: 20 - Noviembre - 2022
Autor: Kevin Chepe - David Zarate
Tema: Programa para calcular el factorial
Materia: Parallel and Distributed Computing
'''

cpdef long cfactorial(long n):
    if  n >= 1:
        return n * cfactorial(n - 1)
    return 1
