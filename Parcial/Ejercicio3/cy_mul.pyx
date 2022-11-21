#cython: language_level=3
cimport cython
"""
Fecha: 23 Noviembre-2022
Autor: David Zárate - Kevin Chepe
Tema: Parcial
"""
cpdef multiplo(int a, int b, int m):
  cdef int i
  cdef int s = 0
  if a < 0 or b < 0:
    print("Ingrese valores positivos")
  else:
    for i in range(a, b):
        if i%m == 0:
            s = s + i
    return s
