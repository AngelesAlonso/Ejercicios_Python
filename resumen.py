'''
variable = "Mario"
edad = 30

print(f"Hola soy {variable} y tengo {edad} años")

#lista
lista = ["naranja", "manzana", "pátano"]

dato1 = lista[1]
dato2 = lista[2]

print(f"El primer elemento de la lista es {dato1} y el segundo elemento es {dato2}")

fruta = input("Ingrese el elemento que quieras añadir a la lista: ")

lista = ["naranja", "manzana", "pátano"]
lista.append(fruta) #añadir un elemento a la lista
print(f"Se añade el elemento {fruta}")
print(lista)

#Tuplas (son inmutables)
tupla = ("naranja", "manzana", "platano")
print(tupla)
print(tupla[0])

#Condicionales:
variable = 30
if variable == 3:
    print(f"La variable vale {variable}, por lo que es igual que 3")
elif variable == 8:
    print(f"La variable vale {variable}, por lo que es igual que 8")
else:
    print("Nada de lo anterior se cumplió")
   
#Diccionario : estrutura de datos
edad = int(input(" Cuantos años ha cumplido Mario "))

mi_diccionario = {
    'nombre': 'Mario',
    'edad': 28,
    'ciudad': 'New York'
} 
print(mi_diccionario['ciudad']) #imprime la ciudad
mi_diccionario['edad'] = edad #cambiar la edad
print(mi_diccionario['edad']) #imprime la ciudad
print(f"Mario ha cumplido años, ahora tiene: {mi_diccionario['edad']}")

 #Bucles While y for
lista = [1, 2, 3]
for numero in lista:
    print("En esta vuelta el númeo vale: ", numero)

import os
archivos = os.listdir() #muestra todos los archivos de directorio
for archivo in archivos:
    print("En esta vuelta estamos recorriendo el archivo ", archivo)

contador = 1
while contador <= 10:
    print("Contador en esta vuelta vale: ",contador)
    contador +=1

#excepciones
try:
   10 / 0
except ZeroDivisionError as error:
    print("Hubo un error al ejecuatar el codigo: ", error)

try:
   lista = [1,2,3,4]
   print(lista[50])
except IndexError as error:
    print("Hubo un error al ejecuatar el codigo: ", error)

#funcion
def sumar(numero1, numero2):
    return numero1 + numero2 #opcional pero si se usa return lo guarda
resultado = sumar(2,5)
print(resultado)
'''
#orientado a objetos (métodos) conjunto de dataos que hace algo
import os
import time
class Ordenador: 
    def __init__(self, nombre_carpeta):
        self.nombre_carpeta = nombre_carpeta
    def crear_carpeta(self):
        os.mkdir(self.nombre_carpeta)
    def eliminar_carpeta(self):
        os.rmdir(self.nombre_carpeta)
usuario1 = Ordenador("carpetita_mario")
usuario2 = Ordenador('carpetita_luis')
usuario2.crear_carpeta()
time.sleep(4)
usuario1.eliminar_carpeta()