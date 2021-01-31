class Coche():

  color = None
  modelo = None
  marca = None
  quemacocos = None
  tipo_combustible = None
  velociadades = None
  placas = None
  rines = None
  motor = None
  caballos_fuerza = None

  def __init__(self):
    print("Clase coche")
  
  def frenar(self):
    print("Metodo frenar")
  
  def encender(self):
    print("Metodo encender")
  
  def acelerar(self):
    print("Metodo acelerar")
  
  def apagar(self):
    print("Metodo apagar")

  def asegurar(self):
    print("Metodo asegurar")

camioneta = Coche()

camioneta.color = "blanco"
camioneta.modelo = "Rio"
camioneta.marca = "KIA"
camioneta.quemacocos = "no"
camioneta.tipo_combustible = ""
camioneta.velociadades = ""
camioneta.placas = "H64H3H"
camioneta.rines = ""
camioneta.motor = "1.0 T-GDI"
camioneta.caballos_fuerza = ""

print(camioneta.color)
print(camioneta.modelo)
print(camioneta.marca)
print(camioneta.quemacocos)
print(camioneta.tipo_combustible)
print(camioneta.velociadades)
print(camioneta.placas)
print(camioneta.rines)
print(camioneta.motor)
print(camioneta.caballos_fuerza)

camioneta.frenar()
camioneta.encender()
camioneta.acelerar()
camioneta.apagar()
camioneta.asegurar()
