import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "cec63220-7a06-11eb-8f8d-f5fc6e6673a6eadf2e0b-3506-4a61-8a7a-460c6df3bcce"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

repetir = "si"
while repetir == "si":

  pregunta = input ("Descripcion del genero de musica: ")

  # CHANGE THIS to something you want your machine learning model to classify
  demo = classify(pregunta)

  label = demo["class_name"]
  confidence = demo["confidence"]


  if label == "Kpop":
    print("Te mando el playlist de Kpop")
  elif label == "Pop":
    print("Te mando el playlist de Pop")

  repetir = input("Otra vez (si/no)")
