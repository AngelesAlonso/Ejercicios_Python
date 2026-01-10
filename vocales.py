entrada = input("introduzca palabras para saber el número de vocales que tiene: ")
vocales = ['a', 'e', 'i', 'o', 'u']
conteovocales = 0

for n in entrada:
    if n in vocales:
        conteovocales += 1
        
print("El número de vocales en los caracteres introducidos son: ", conteovocales)

    
    