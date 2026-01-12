numero = int(input("Escriba un número: "))

for primo in range(1, numero + 1):
    if primo > 1:
        for i in range(2,primo):
            if primo % i == 0:
                break
        else:
            print(primo)

# Hacerlo con funcion
'''
numero = int(input("Escriba un número: "))

def es_primo(n):
    if n <= 1:       
        return False
    for i in range(2, n):   
        if n % i == 0:        
            return False
    return Tre

'''
