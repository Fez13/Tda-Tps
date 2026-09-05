#Carga las pruebas provistas por la catedra en un formato numerico simple de corroborar

def cargar_archivo(path_prueba) -> list[int]:
  numbers = []
  with open(path_prueba) as prueba_file:
    #Ignorar cometario en primera linea
    if(prueba_file.readline() == 0):
      raise NameError("Prueba vacia")
    numbers = [int(val.strip()) for val in prueba_file.read().split(";") if val.strip()]
  return numbers
