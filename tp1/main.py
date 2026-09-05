
#
# Cuando lei el tp por primera vez pense que las monedas podian estar repetidas.
# De no ser el caso la solucion naive generar_elecciones_simple parece andar.
#


from collections import deque
from math import ceil, floor
from random import random, sample

from pruebas.loader import cargar_archivo

#
# Demostracion:
# Dado el arreglo de monedas:
# S = [l1, l2, ..., ln]
#
# Se toma:
#   M1 = max{l1,ln}
#   m1 = min{l2,ln} o min{l1,l(n-1)}
#
# Si M1 elije l1, es porque l1 > ln -> m1 < l1 ya que m1 es el minimo entre ln y otro
# de la misma forma si se elije rn
#
# En general M1 > m1
# ahora las listas de solucion quedan
# p1 = {M1} (sofi)
# p2 = {m1} (mateo)
#
# Esto se repite hasta el ultimo elemento
#
# p1 = {M1,M2,...,M(n/2), M(n/2 + 1)} El ultimo elemento es en caso de n impar, si no es 0
# p2 = {m1,m2,...,m(n/2)}
#
# ahora:
#   Mn > mn y M(n/2 + 1) >= 0
# por lo que:
#   sum(Mk - mk) + M(n/2 + 1) >= 0 -- Solo es igual en caso de array vacio o donde hay una moneda con 0
#   divido la suma:
#   sum(Mk) + M(n/2 + 1) - sum(mk) >= 0
#   sum(Ml) + M(n/2 + 1) >= sum(mk)
#
# Y ese es el objetivo ya que las monedas de sofia M, son siempre mayores a las de mateo m, salvo por el caso trivial de empate.
#

def generar_elecciones_simple(arr: list[int]):
  resultado_sofia = deque()
  resultado_mateo = deque()
  turno_sofia = True
  while arr:
    max_idx = 0
    min_idx = -1
    if arr[0] < arr[-1]:
      max_idx = -1
      min_idx = 0

    if turno_sofia:
      resultado_sofia.append(arr.pop(max_idx))
    else:
      resultado_mateo.append(arr.pop(min_idx))
  return resultado_sofia,resultado_mateo


def generar_array_random(elementos, valor_max):
  return sample(range(1, valor_max + 1), elementos)

CASOS_BORDE = [
  [3, 4, 1, 2],
  [3, 1, 2, 5, 4],
  [2, 1, 5, 3, 4],
]

def prueba_casos_borde():
  for arr in CASOS_BORDE:
    s, m = generar_elecciones_simple(arr.copy())
    if sum(s) <= sum(m):
      print(f"FALLA {arr}: sofia no gana ({sum(s)} vs {sum(m)})")

def prueba_casos_catedra():
  for file in ["pruebas/TP1/20.txt","pruebas/TP1/25.txt","pruebas/TP1/50.txt","pruebas/TP1/100.txt","pruebas/TP1/1000.txt","pruebas/TP1/10000.txt","pruebas/TP1/20000.txt"]:
    archivo = cargar_archivo(file)
    s,m = generar_elecciones_simple(archivo.copy())
    sum_s = sum(s)
    sum_m = sum(m)
    if sum_s <= sum_m:
      print(f"Se esperaba victoria en prueba de catedra: {file}")

def prueba():
  prueba_casos_borde()
  prueba_casos_catedra()
  return
  n = 100_000
  gana_sofia = 0
  for i in range(n):
    num_elems = floor(random() * 100 + 1)
    valor_max = num_elems + floor(random() * 100 + 1)
    arr = generar_array_random(num_elems,valor_max)
    s,m = generar_elecciones_simple(arr.copy())
    sum_s = sum(s)
    sum_m = sum(m)
    if sum_s > sum_m:
      gana_sofia += 1
    else:
      print(f"NO GANA {arr}: {sum_s} vs {sum_m}")

  print(f"Sofia gana: {gana_sofia}/{n}")

prueba()
