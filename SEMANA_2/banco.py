class Banco():

  nombre_cliente = None
  numero_cliente = None
  maximo_numero_cliente = None
  tabla_cliente = None
  saldo_cliente = None
  direccion_cliente = None
  id_tarjeta = None

  def __init__(self):
    print("Clase banco")

  def crear_cuenta(self):
    print("Metodo crear cuenta")

  def cerrar_cuenta(self):
    print("Metodo cerrar cuenta")
  
  def modificar_saldo(self):
    print("Metodo modificar saldo")
  
  def menu_operaciones(self):
    print("Metodo menús de operadores")
  
  def dar_tarjetas(self):
    print("Metodo dar tarjetas")

santander = Banco()

santander.nombre_cliente = "Porfirio"
santander.numero_cliente = 8735
santander.maximo_numero_cliente = 9863
santander.tabla_cliente = "si"
santander.saldo_cliente = 4741
santander.id_tarjeta = 84467885

print(santander.nombre_cliente)
print(santander.numero_cliente)
print(santander.maximo_numero_cliente)
print(santander.tabla_cliente)
print(santander.saldo_cliente)
print(santander.id_tarjeta)

santander.crear_cuenta()
santander.cerrar_cuenta()
santander.modificar_saldo()
santander.menu_operaciones()
santander.dar_tarjetas()