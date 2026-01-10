numero = int(input("Escriba un número: "))

for primo in range(2, numero + 1):
    if primo > 1:
        for i in range(2,primo):
            if primo % i == 0:
                break
        else:
            print(primo)