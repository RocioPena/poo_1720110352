class Estudiante():
  dedicacion = None
  calidad_trabajo = None
  esfuerzo = None
  atencion = None
  comunicacion = None
  visualizacion = None
  interes = None
  organizacion = None
  realizar_trabajos = None
  higiene = None

  def __init__(self):
    print("Clase Estudiante")

  def estudiar(self):
    print ("Metodo estudiar")
  
  def particiar(self):
    print("Metodo particiar")

  def responsabilidad(self):
    print("Metodo responsabilidad")
  
  def puntualidad(self):
    print("Metodo puntualidad")
  
  def asistir(self):
    print("Metodo asistir")

juan = Estudiante()

juan.dedicacion = "si"
juan.calidad_trabajo = "si"
juan.esfuerzo = "si"
juan.atencion = "si"
juan.comunicacion = "no"
juan.visualizacion = "si"
juan.interes = "no"
juan.organizacion = "no"
juan.realizar_trabajos = "si"
juan.higiene = "no"

print(juan.dedicacion)
print(juan.calidad_trabajo)
print(juan.esfuerzo)
print(juan.atencion)
print(juan.comunicacion)
print(juan.visualizacion)
print(juan.interes)
print(juan.organizacion)
print(juan.realizar_trabajos)
print(juan.higiene)

juan.estudiar()
juan.particiar()
juan.responsabilidad()
juan.puntualidad()
juan.asistir()