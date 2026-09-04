
#
# Cuando lei el tp por primera vez pense que las monedas podian estar repetidas.
# De no ser el caso la solucion naive generar_elecciones_simple parece andar.
#


from collections import deque
from math import ceil, floor
from random import random, sample

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

# Casos borde: la consigna pide que Sofia gane (no importa el margen).
# Fallan si Sofia no gana (empata o pierde).
CASOS_BORDE = [
  [3, 4, 1, 2],        # empate de ganancias: ejerce el desempate
  [3, 1, 2, 5, 4],     # la eleccion inmediata (max/min extremos) difiere de la ganancia
  [2, 1, 5, 3, 4],     # caso de margen suboptimo conocido (igual gana)
]

def prueba_casos_borde():
  for arr in CASOS_BORDE:
    s, m = generar_elecciones_simple(arr.copy())
    if sum(s) <= sum(m):
      print(f"FALLA {arr}: sofia no gana ({sum(s)} vs {sum(m)})")

def prueba():
  prueba_casos_borde()
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
