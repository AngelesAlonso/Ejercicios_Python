# Un palíndromo es una secuencia de caacteres o digitos que se lee igual al derecho y al reves.
palindromo = input("Introduzca una cadena de texto para saber si es o no un palíndromo: ")

if str(palindromo) == str(palindromo)[::-1]:
    print("Es palindromo")
else:
    print ("No es palindromo")