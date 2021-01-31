class Classroom():
  profesor = None
  tiempo_materia = None
  materia = None
  correo_electronico = None
  numero_alumno = None
  nombre_alumno = None
  permisos = None
  tiempo_entrega = None
  idioma = None
  contraseña = None

  def __init__(self):
    print("Clase classroom")
   
  def subir_trabajos(self):
    print("Metodo subir trabajos")
  
  def comentar(self):
    print("Metodo comentar")
  
  def checar_calendario(self):
    print("Metodo checar calendario")
  
  def archivar_clase(self):
    print("Metodo archivar clase")
  
  def ver_videoconferencias(self):
    print("Ver videoconferencias")

mate = Classroom()

mate.profesor = "Juan"
mate.tiempo_materia = "un cuatrimestre"
mate.materia = "matematicas"
mate.correo_electronico = "juan******@gmail.com"
mate.numero_alumno = 30
mate.nombre_alumno = ""
mate.permisos = "si"
mate.tiempo_entrega = "una semana"
mate.idioma = "español"
mate.contraseña = "********"

print(mate.profesor)
print(mate.tiempo_materia)
print(mate.materia)
print(mate.correo_electronico)
print(mate.numero_alumno)
print(mate.nombre_alumno)
print(mate.permisos)
print(mate.tiempo_entrega)
print(mate.idioma)
print(mate.contraseña)

mate.subir_trabajos()
mate.comentar()
mate.checar_calendario()
mate.archivar_clase()
mate.ver_videoconferencias()