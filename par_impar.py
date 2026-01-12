numero = int(input("Introduce un numero: "))

if numero % 2 == 0:
    print("El numeros que has indicado es par")
else:
    print("El númeo indicado es impar")

# versión 2 del enuncionado.
# Mostrar por pantalla los números pares entre el 1 y el 20 (ambos incluidos)
for n in range(1, 21):
    es_par = n % 2 == 0
    if es_par:
        print(n)


# Mismo enunciado anterior pero en una sola línea
print([n for n in range(1,21) if n % 2 == 0])

print(*[n for n in range(1,21) if n % 2 == 0])

print(*range(2, 21, 2))

