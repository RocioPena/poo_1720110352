class Avion():

  color = None
  modelo = None
  marca = None
  velocidad = None
  capacidad = None
  comercial = None
  privado = None
  tecnologico = None
  carga = None
  tamaño = None

  def __init__(self):
    print("Clase avion")
  
  def volar(self):
    print("Metodo volar")
  
  def aterrizar(self):
    print("Metodo aterrizar")
  
  def encender(self):
    print("Metodo encender")
  
  def apagar (self):
    print("Metodo apagar")
  
  def planear(self):
    print("Metodo planear")

avioncomercial = Avion( )


avioncomercial.color ="azul"
avioncomercial.modelo ="Boeing 747"
avioncomercial.marca = "Boeing"
avioncomercial.velocidad = 900
avioncomercial.capacidad = 467
avioncomercial.comercial = "si"
avioncomercial.privado = "no"
avioncomercial.tecnologico = "si"
avioncomercial.carga = "si" 
avioncomercial.tamaño = "71 metros"

print(avioncomercial.color)
print(avioncomercial.modelo)
print(avioncomercial.marca)
print(avioncomercial.velocidad)
print(avioncomercial.capacidad)
print(avioncomercial.comercial)
print(avioncomercial.privado)
print(avioncomercial.tecnologico)
print(avioncomercial.carga)
print(avioncomercial.tamaño)

avioncomercial.volar()
avioncomercial.aterrizar()
avioncomercial.encender()
avioncomercial.apagar()
avioncomercial.planear()