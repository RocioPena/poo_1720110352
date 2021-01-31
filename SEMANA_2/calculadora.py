class Calculadora():

  tamanio = None
  color = None
  marca = None
  cientifica = None
  solar = None
  pila = None
  manual = None
  combinaciones = None
  tapa = None
  digital = None

  def __init__(self):
    print("Clase calculadora")
  
  def sumar(self):
    print("Metodo sumar")
  
  def restar(self):
    print("Metodo restar")

  def dividir(self):
    print("Metodo dividir")
  
  def multiplicacion(self):
    print("Metodo multiplicacion")
  
  def calcular (self):
    print("Metodo calcular")

casio = Calculadora()

casio.tamanio = "mediano"
casio.color = "rojo"
casio.marca = "casio"
casio.cientifica = "si"
casio.solar = "no"
casio.pila = "si"
casio.manual = "si"
casio.combinaciones = "si"
casio.tapa = "si"
casio.digital = "no"

print(casio.tamanio)
print(casio.color)
print(casio.marca)
print(casio.cientifica)
print(casio.solar)
print(casio.pila)
print(casio.manual)
print(casio.combinaciones)
print(casio.tapa)
print(casio.digital)

casio.sumar()
casio.restar()
casio.dividir()
casio.dividir()
casio.calcular()