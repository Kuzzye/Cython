
"""
Fecha: 23 Noviembre-2022
Autor: David Zárate - Kevin Chepe
Tema: Parcial
"""

import time
import py_primo
import cy_primo

formato_datos = "{:.5f},{:.5f}\n"

for i in range(30):
	inicioPy = time.time()
	py_primo.count_primes(1000)
	finalPy = time.time() - inicioPy
	inicioCy = time.time()
	cy_primo.count_primes(1000)
	finalCy = time.time() - inicioCy
	
	with open("primo.csv","a") as archivo:
		archivo.write(formato_datos.format(finalPy, finalCy))
