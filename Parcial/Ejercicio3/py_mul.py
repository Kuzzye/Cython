"""
Fecha: 23 Noviembre-2022
Autor: David Zárate - Kevin Chepe
Tema: Parcial
"""

def multiplo(a, b, m):
  s:int = 0
  if a < 0 or b < 0:
    print("Ingrese valores positivos")
  else:  
    for i in range(a, b):
        if i%m == 0:
            s = s + i
    return s
