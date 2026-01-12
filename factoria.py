numero = int(input("Introduzca un número: "))

factorial = 1

for i in range(1, numero +1):    # for i in range(2, numero +1):
    factorial *= i
    
print(f"El factoria de {numero} es: {factorial}")

#con función:

def factorial (numero):
    if numero == 0 or numero ==1:
        return 1
    else:
        return factorial (numero-1) * numero

print(factorial(int(input("Introduzca un número: "))))
