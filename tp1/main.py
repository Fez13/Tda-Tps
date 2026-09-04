
#
# Se me ocurrio esta posible solucion, hay que verificar casos bordes.
#
# Para cada turno k se pueden elejir 2 monedas, m_l o m_u donde nuestro array de monedas es:
# arr = [m_l,m_(l+1), ..., m_(u-1), m_u]
# Una regla greedy es la que minimize la perdida para sofia, ej;
#
# Si el turno es de sofia:
#  Si elijo la moneda m_l mateo (sofia) va a elejir en su turno min(m_(l+1), m_u)
#  Si elijo la moneda m_u ... min(m_l, m_(u-1))
#
# Por lo que la ganancia de elejir una moneda es:
# g = m_l - min(m_(l+1), m_u) //Para moneda m_l
# g = m_u - min(m_l, m_(u-1)) //Para moneda m_u
#
# Sofia simplemente debe elejir la ganancia mayor y darle a su hermano la menor
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

def generar_elecciones(arr: list[int]):
  resultado_sofia = deque()
  resultado_mateo = deque()
  turno_sofia = True
  while(arr):
    g_l = arr[0] - calcular_minimos_siguientes(arr[1:])
    g_u = arr[-1] - calcular_minimos_siguientes(arr[:-1])
    gl_mayor = g_l > g_u

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
  return [floor((random() * (valor_max-1)) + 1) for i in range(elementos)]

def prueba():
  n = 100_000
  gana_sofia, empate = 0,0
  for i in range(n):
    arr = generar_array_random(floor(random() * 499 + 1),floor(random() * 14 + 1))
    s,m = generar_elecciones(arr)
    sum_s = sum(s)
    sum_m = sum(m)
    if sum_s > sum_m:
      gana_sofia += 1
    if sum_s == sum_m:
      empate += 1
  print(f"Sofia gana: {gana_sofia} mateo: {n - gana_sofia - empate} empates: {empate}")

prueba()
"""
❯ time python main.py
Sofia gana: 92783 mateo: 0 empates: 7217

________________________________________________________
Executed in   14.28 secs    fish           external
   usr time   14.25 secs  575.00 micros   14.24 secs
   sys time    0.00 secs  262.00 micros    0.00 secs
"""
#Quiza medio lento, hay que verificar si los empates son optimos, es decir. Son situaciones en las que no se puede ganar.
