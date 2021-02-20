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
      #if num_retraso >= 3:
      # uno = 1
      #else:
       # cero = 0

      resta = num_clase - num_faltas
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