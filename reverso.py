cadena = input("Introduzca un texto: ")

texto = list(cadena)
texto.reverse()

cadena_invertida = "".join(texto)

print ("El texto al revés es: ", cadena_invertida)