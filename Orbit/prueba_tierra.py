"""
Fecha: 2 nov 2022
Autor: Kevin Fabian Chepe Astudillo
Tema: Cython
Topico: Planetas - orbita gravitacional
Principal: llama a ambos programas Cy/Py
La idea principal es crear un .csv
"""

import time
import py_planet_orbit
import cy_planet_orbit

"""Ejemplo usando datos del planeta tierra"""
"""Datos del planeta por Wikipedia"""

#Inicialización de planeta para PYTHON
tierraPy = py_planet_orbit.Planet()
tierraPy.x = 100*10**3
tierraPy.y = 300*10**3
tierraPy.z = 700*10**3
tierraPy.vx = 2.000*10**3
tierraPy.vy = 29.87*10**3
tierraPy.vz = 0.034*10**3
tierraPy.m = 5.9741*10**24

"""Ejemplo usando datos del planeta tierra"""
"""Datos del planeta por Wikipedia"""

#Inicialización de planeta para CYTHON
tierraCy = cy_planet_orbit.Planet()
tierraCy.x = 100*10**3
tierraCy.y = 300*10**3
tierraCy.z = 700*10**3
tierraCy.vx = 2.000*10**3
tierraCy.vy = 29.87*10**3
tierraCy.vz = 0.034*10**3
tierraCy.m = 5.9741*10**24

time_span = 400
n_steps = 2000000

"""Definición de experimento
Reducción de ruido gausiano"""

#Se crea un formato para la impresión sobre el fichero
formato_datos = "{:.5f},{:.5f}\n"

for i in range(30):
	#Toma de tiempos para Python
	inicioPy = time.time()
	py_planet_orbit.step_time(tierraPy, time_span, n_steps)
	finalPy = time.time() - inicioPy
	
	#Toma de tiempos para Cython
	inicioCy = time.time()
	cy_planet_orbit.step_time(tierraCy, time_span, n_steps)
	finalCy = time.time() - inicioCy
	
	with open("tierra.csv","a") as archivo:
		archivo.write(formato_datos.format(finalPy,finalCy))
