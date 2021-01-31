class Cajero_automatico():

  ubicacion = None
  que_banco = None
  color = None
  digital = None
  tipo_cajero = None
  tamanio = None
  accesibilidad = None
  entrada_tarjeta = None
  turno = None
  contrasenia = None

  def __init__(self):
    print("Clase cajero automatico")

  def repetir_dinero(self):
    print("Metodo repetir dinero")
   
  def depositar(self):
     print("Metodo depositar")
  
  def pagar(self):
    print("Metodo pagar")
  
  def trasferir(self):
    print("Metodo trasferir")
  
  def consultar_saldo(self):
    print("Metodo consultar saldo")

bbva = Cajero_automatico()
bbva.ubicacion = "supermecado"
bbva.que_banco = "Bancomer"
bbva.color = "azul y gris"
bbva.digital = "si"
bbva.tipo_cajero = "trasferencias"
bbva.tamanio = "grande"
bbva.accesibilidad = "si"
bbva.entrada_tarjeta = "horizontal"
bbva.turno = ""
bbva.contrasenia = "si"

print(bbva.ubicacion)
print(bbva.que_banco)
print(bbva.color)
print(bbva.digital)
print(bbva.tipo_cajero)
print(bbva.tamanio)
print(bbva.accesibilidad)
print(bbva.entrada_tarjeta)
print(bbva.turno)
print(bbva.contrasenia)

bbva.repetir_dinero()
bbva.depositar()
bbva.pagar()
bbva.trasferir()
bbva.consultar_saldo()