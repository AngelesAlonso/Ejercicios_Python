entrada = input("Introduce númeos separados por comas: ")

numeros = []

for elemento in entrada.split(","):
    numeros.append(int(elemento.strip()))

numeros.sort()

num_max = numeros[0]
num_min = numeros[0]

for n in numeros:
    if n > num_max:
        num_max = n
if n < num_min:
        num_min = n

print("La lista introducida es: ", numeros)
print("El valor máximo es:", num_max)
print("El valor mínimo es:", num_min)
    
    