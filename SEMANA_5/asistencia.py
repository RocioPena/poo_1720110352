class Asistencia():

  def bucle(self):
    repetir = "s"
    while repetir == "s":

      materia = input("Materia: ")
      numero_alumno = input("Numero de alumnos: ")
      nombre = input("Nombre del alumno: ")
      num_clase = int(input("Numero de clases: ")) 
      num_faltas = int(input("Numero de faltas: "))
      num_retraso = int(input("Numero de retraso:"))
      mod = num_retraso // 3
      resta = num_clase - num_faltas - mod
      multi = 100/num_clase
      porcentaje = resta*multi
      print("Porcentaje: ", porcentaje)
      if porcentaje > 80:
        print("Resultado: Tienes derecho")
      else:
        print("Resultado: No tienes derecho")

      repetir = input("Otra evaluacion (s/n)") 

hi = Asistencia()
hi.bucle()

#dice que varible local en la linea 7,8,9 pero no se pero si funciona
