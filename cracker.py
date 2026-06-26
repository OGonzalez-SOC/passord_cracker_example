password = "12345"
diccionario = ["123","456","789","12345"]
intentos = 0

for i in diccionario:
  intentos = intentos + 1
  print("Intento: ", i)

  if i == password:
    print("Contraseña Encontrada: ", i)
    print("Total de intentos: ", intentos)
    break
  
else:
  print("Contraseña no encontrada en el diccionario")
 
