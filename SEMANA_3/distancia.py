class Distancia():
  def __init__(self):
    pass
  
  def distanciaPuntos(self,x2,x1,y2,y1):
    resta1 = x2-x1
    resta2 = y2-y1
    potencia1 = resta1**2
    potencia2 = resta2**2
    suma = potencia1+potencia2
    import math
    raiz = suma
    print(math.sqrt(raiz))
    
resultado = Distancia()

resultado.distanciaPuntos(4.99,3.17,7.88,4.78)

resultado.distanciaPuntos(1.93,7.15,4.38,21.6)

resultado.distanciaPuntos(10.4,12.17,29.3,10.4)

resultado.distanciaPuntos(68.3,39.4,187.2,78.9)

resultado.distanciaPuntos(295.3,88.7,18.4,118.3)