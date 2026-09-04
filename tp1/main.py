
#
# Se me ocurrio esta posible solucion, hay que verificar casos bordes.
#
# Para cada turno k se pueden elejir 2 monedas, m_l o m_u donde nuestro array de monedas es:
# arr = [m_l,m_(l+1), ..., m_(u-1), m_u]
# Una regla greedy es la que minimize la perdida para sofia y maximise para mateo, ej;
#
# Si el turno es de sofia:
#  Si elijo la moneda m_l mateo (sofia) va a elejir en su turno min(m_(l+1), m_u)
#  Si elijo la moneda m_u ... min(m_l, m_(u-1))
#
# Por lo que la ganancia de elejir una moneda es:
# g = m_l - min(m_(l+1), m_u) //Para moneda m_l
# g = m_u - min(m_l, m_(u-1)) //Para moneda m_u
#
# Si es el turno de mateo:
# Si elijo la moneda m_l sofia va a elejir en su turno max(m_(l+1), m_u)
# ...
#
# # Por lo que la ganancia de elejir una moneda es:
# g = m_l - max(m_(l+1), m_u) //Para moneda m_l
# g = m_u - max(m_l, m_(u-1)) //Para moneda m_u
#
# Sofia simplemente debe elejir la ganancia mayor y darle a su hermano la menor
#
# Notar que en caso de empate sofia elije el mas grande y mateo el mas chico, si no:
#   [1, 2, 3, 2]
# falla
#
# Notar que si tanto sofia como mateo usan calcular_min_siguiente, ambos elijen min
# [1, 1, 2, 2, 1, 1]
# falla
#
#


from collections import deque
from math import floor
from random import random


def calcular_minimos_siguientes(arr: list[int]):
  if len(arr) == 0:
    return 0
  if len(arr) == 1:
    return arr[0]
  return min(arr[0], arr[-1])

def calcular_maximo_siguientes(arr: list[int]):
  if len(arr) == 0:
    return 0
  if len(arr) == 1:
    return arr[0]
  return max(arr[0], arr[-1])


def generar_elecciones(arr: list[int]):
  resultado_sofia = deque()
  resultado_mateo = deque()
  turno_sofia = True
  while(arr):
    g_l = 0
    g_u = 0
    if turno_sofia:
      g_l = arr[0] - calcular_minimos_siguientes(arr[1:])
      g_u = arr[-1] - calcular_minimos_siguientes(arr[:-1])
    else:
      g_l = arr[0] - calcular_maximo_siguientes(arr[1:])
      g_u = arr[-1] - calcular_maximo_siguientes(arr[:-1])

    gl_mayor = g_l > g_u

    #El caso de empate que mencione antes
    if g_l == g_u:
      gl_mayor = arr[0] > arr[-1]

    if turno_sofia:
      if gl_mayor:
        resultado_sofia.append(arr.pop(0))
      else:
        resultado_sofia.append(arr.pop(-1))
    else:
      if gl_mayor:
        resultado_mateo.append(arr.pop(-1))
      else:
        resultado_mateo.append(arr.pop(0))
    turno_sofia = not turno_sofia

  return resultado_sofia, resultado_mateo


def generar_array_random(elementos, valor_max):
  return [round((random() * (valor_max-1)) + 1) for i in range(elementos)]

CASOS_BORDE = [
  ([1, 2, 3, 2], 2),
  ([2, 5, 5, 2], 0),
  ([1, 2, 3, 3, 2, 1], 0),
]

def prueba_casos_borde():
  for arr, esperado in CASOS_BORDE:
    s, m = generar_elecciones(arr.copy())
    obtenido = sum(s) - sum(m)
    if obtenido != esperado:
      print(f"FALLA {arr}: margen esperado {esperado}, obtenido {obtenido}")

def es_empate_forzado(arr: list[int]):
  n = len(arr)
  if n % 2 == 1:
    return False
  return arr[0] <= arr[1] and arr == [arr[0]] + [arr[1]] * (n - 2) + [arr[0]]

def prueba():
  prueba_casos_borde()
  n = 100_000
  gana_sofia, empate = 0, 0
  empate_forzado = 0
  for i in range(n):
    num_elems = floor(random() * 25 + 1)
    valor_max = floor(random() * 15 + 1)
    arr = generar_array_random(num_elems,valor_max)
    s,m = generar_elecciones(arr.copy())
    sum_s = sum(s)
    sum_m = sum(m)
    if sum_s > sum_m:
      gana_sofia += 1
    if sum_s == sum_m:
      empate += 1
      if es_empate_forzado(arr):
        empate_forzado += 1
      else:
        print(num_elems,valor_max)
        print(arr)

  res = f"Sofia gana: {gana_sofia} mateo: {n - gana_sofia - empate} empates: {empate}"
  if empate:
    res += f" forzados: {(empate_forzado / empate) * 100.0}%"
  print(res)

prueba()
#
# El caso:
# [1, 2, 3, 3, 2, 1]
# falla
#
# --Federico
#
