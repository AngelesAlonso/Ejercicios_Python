numero = int(input("Introduzca un número: "))

factorial = 1

for i in range(1, numero +1):
    factorial *= i
    
print(f"El factoria de {numero} es: {factorial}")