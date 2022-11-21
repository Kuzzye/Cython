"""
Fecha: 23 Noviembre-2022
Autor: David Zárate - Kevin Chepe
Tema: Parcial
"""

def count_primes(n):
  count:int = 0
  for i in range(n):
    if (i > 1):
      for j in range(2, i):
        if i % j == 0:
          break
      else:
        count += 1
  return count

a = count_primes(1000)
print("Cantidad de numeros primos entre el 0 y el 1000", a)
