class Serie_tv():

  nombre_serie = None
  personajes= None
  trama = None
  duracion = None
  origen = None
  idioma = None
  dias_transmision = None
  horario = None
  canciones = None
  episodios = None

  def __init__(self):
    print("Clase serie_tv")
  
  def entretener(self):
    print("Metodo entretener")
  
  def aprender(self):
    print("Metodo aprender")
  
  def emocionar(self):
    print("Metodo emocionar")
  
  def intrigar(self):
    print("Metodo intrigar")
  
  def dejar_suspenso(self):
    print("Metodo dejar suspenso")

hwarang = Serie_tv()

hwarang.nombre_serie = "Hwarang: The Poet Warrior Youth"
hwarang.personajes = "Sun Woo, Ah Ro, Ji Dwi"
hwarang.trama = "Drama, Histórico, Comedia, Romance "
hwarang.duracion = "1 hora"
hwarang.origen = "Corea del Sur"
hwarang.idioma = "coreano"
hwarang.dias_transmision = "Lunes y Martes"
hwarang.horario = "10 pm"
hwarang.canciones = "si"
hwarang.episodios = "20"

print(hwarang.nombre_serie)
print(hwarang.personajes)
print(hwarang.trama)
print(hwarang.duracion)
print(hwarang.origen)
print(hwarang.idioma)
print(hwarang.dias_transmision)
print(hwarang.horario)
print(hwarang.canciones)
print(hwarang.episodios)

hwarang.entretener()
hwarang.aprender()
hwarang.emocionar()
hwarang.intrigar()
hwarang.dejar_suspenso()