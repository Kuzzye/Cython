
"""
Fecha: 23 Noviembre-2022
Autor: David Zárate - Kevin Chepe
Tema: Parcial
"""

import time
import py_mul
import cy_mul

formato_datos = "{:.5f},{:.5f}\n"

inicio = 0
fin = 1000
m = 5

a = py_mul.multiplo(inicio, fin, m)
print("La suma de los multiplos de 5 entre los valores 0 y 1000 es -> ", a)

for i in range(30):
	inicioPy = time.time()
	py_mul.multiplo(inicio, fin, m)
	finalPy = time.time() - inicioPy
	inicioCy = time.time()
	cy_mul.multiplo(inicio, fin, m)
	finalCy = time.time() - inicioCy
	
	with open("bfs.csv","a") as archivo:
		archivo.write(formato_datos.format(finalPy, finalCy))
