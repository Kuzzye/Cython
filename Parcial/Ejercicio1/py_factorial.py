'''
Fecha: 20 - Noviembre - 2022
Autor: Kevin Chepe - David Zarate
Tema: Programa para calcular el factorial
Materia: Parallel and Distributed Computing

'''
def factorial(n):
    if  n >= 1:
        return n * factorial(n - 1)
    return 1
