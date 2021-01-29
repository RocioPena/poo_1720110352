class Vacaciones():
  lugar = None
  gps = None
  guia_turista = None
  hotel = None
  tipo_ropa = None
  utencilios = None
  agente_viajes = None
  epoca_del_anio = None
  planificacion = None
  tiempo_de_viaje = None

  def __init__(self):
    print("Clase vacaciones")
  
  def viajar(self):
    print("Metodo viajar")
  
  def divertir(self):
    print("Metodo divertir")
  
  def conocer(self):
    print("Metodo conocer")
  
  def experimentar(self):
    print("Metodo experimentar")
  
  def transporte(self):
    print("Metodo transporte")
  
playa = Vacaciones()

playa.lugar = "Veracruz"
playa.gps = "si"
playa.guia_turista = "no"
playa.hotel = "si"
playa.tipo_ropa = "playa"
playa.utencilios = "cepillo de dientes, protector solar, etc."
playa.agente_viajes = "no"
playa.epoca_del_anio = "verano"
playa.planificacion = "si"
playa.tiempo_de_viaje = "2 dias"

print(playa.lugar)
print(playa.gps)
print(playa.guia_turista)
print(playa.hotel)
print(playa.tipo_ropa)
print(playa.utencilios)
print(playa.agente_viajes)
print(playa.epoca_del_anio)
print(playa.planificacion)
print(playa.tiempo_de_viaje)

playa.viajar()
playa.divertir()
playa.conocer()
playa.experimentar()
playa.transporte()
