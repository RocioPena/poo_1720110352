class Futbolista():
  
  nombre = None
  equipo = None
  nacionalidad = None
  numero = None
  sexo = None
  meter_gol = None
  portero = None
  defensa = None
  mediocentro = None
  delantero = None

  def __init__(self):
    print ("Clase futbolista")
  
  def patear(self):
    print("Metodo patear")
  
  def correr(self):
    print("Metod correr")
  
  def pasar(self):
    print("Metodo pasar")
  
  def recibir(self):
    print("Metodo recibir")
  
  def quitar_balon(self):
    print("Metodo quitar_balon")

paul = Futbolista()

paul.nombre = "Paul Labile Pogba"
paul.equipo = "Manchester United F. C."
paul.nacionalidad = "Francesa"
paul.numero = 6
paul.sexo = "masculino"
paul.meter_gol = "no"
paul.portero = "no"
paul.defensa = "no"
paul.mediocentro = "si"
paul.delantero = "si"

print(paul.nombre)
print(paul.equipo)
print(paul.nacionalidad)
print(paul.numero)
print(paul.sexo)
print(paul.meter_gol)
print(paul.portero)
print(paul.defensa)
print(paul.mediocentro)
print(paul.delantero)

paul.patear()
paul.correr()
paul.pasar()
paul.recibir()
paul.quitar_balon