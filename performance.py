# Fichero para la prueba y comparativa de rendimiento
# Solo pythom, con cython

import time
import py_planet_orbit
import cy_planet_orbit


init_time = time.time()

py_planet_orbit.main()
fin_time = time.time()

total_time_python = fin_time - init_time
print("Tiempo total de python: ",total_time_python)

init_time = time.time()
cy_planet_orbit.main()
fin_time = time.time()

total_time_cython = fin_time - init_time
print("Tiempo total de Cython: ", total_time_cython)

print(f"Cython es {total_time_python/total_time_cython} veces más rapido que Python")
