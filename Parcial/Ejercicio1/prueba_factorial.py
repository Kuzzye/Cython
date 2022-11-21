"""
Fecha: 20 nov 2022
Autor: Kevin Fabian Chepe Astudillo
Tema: Cython
Topico: Factorial
Principal: llama a ambos programas Cy/Py
La idea principal es crear un .csv
"""

import time
import py_factorial
import cy_factorial

"""Definición de experimento
Reducción de ruido gausiano"""

#Se crea un formato para la impresión sobre el fichero
formato_datos = "{:.5f},{:.5f}\n"

for i in range(30):
	#Toma de tiempos para Python
	inicioPy = time.time()
	py_factorial.factorial(995)
	finalPy = time.time() - inicioPy
	
	#Toma de tiempos para Cython
	inicioCy = time.time()
	cy_factorial.cfactorial(995)
	finalCy = time.time() - inicioCy
	
	with open("factorial.csv","a") as archivo:
		archivo.write(formato_datos.format(finalPy,finalCy))
