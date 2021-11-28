# ejercicio 1
def longitud(cadena):
    
    contador = 0
    
    for c in cadena:
        contador += 1
    return contador

my_string = input("Ingresar el texto: ")
lista_palabras = my_string.split()

print("El texto ingresado es: {}".format(my_string))
print(f"La ultima palabra es {lista_palabras[-1]} y su longitud es de {longitud(lista_palabras[-1])} caracteres.")

# ejercicio 2
def mayuscula_primer_caracter(frase):
    resultado=""
    for p in frase.split():
        resultado += p[0].upper() + p[1::] + " "
    return resultado
texto="hola mundo que tal"
print(mayuscula_primer_caracter(texto))

# ejercicio 3
class circulo:
    def __init__(self, radio, pi):
        self.radio = radio
        self.pi = pi
pi=3.1416
radio=float(input("Ingrese el area: "))
area=pi*radio**2
print("El area del circulo es: ", area)

# ejercicio 4
class rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
base=float(input("Ingrese la base: "))
altura=float(input("Ingrese la altura: "))
area= base * altura
print("El area del rectangulo es: ", area)

# ejercicio 5
class Alumno:
    def __init__(self, name, nroregistro, edad, nota):
        self.name=name
        self.nroregistro=nroregistro
        self.edad=edad
        self.nota=nota
        print('\033[1m',"Se ha registrado el alumno: ", self.name,'\033[0m')
    
    def __str__(self) -> str:
        return "{} ({})".format(self.name, self.nroregistro)

    def display(self):
        print(f"Nombre: {self.name}")
        print(f"Número de registro: {self.nroregistro}")

    def setAge(self, edad):
        self.edad.append(edad)
    
    def setNota(self, nota):
        self.nota.append(nota)

cust1=Alumno("Axel", "01", "23 años", "16 puntos")

print(f"El nombre del alumno es: {cust1.name}")
print(f"El numero de registro es: {cust1.nroregistro}")
print("La edad del alumno es: {}".format(cust1.edad))
print("La nota del alumnos es: {}".format(cust1.nota))

cust2 = Alumno("Carlos","02","28 años","19 puntos")

print(f"El nombre del alumno es: {cust2.name}")
print(f"El numero de registro es: {cust2.nroregistro}")
print("La edad del alumno es: {}".format(cust2.edad))
print("La nora del alumnos es: {}".format(cust2.nota))

# ejercicio 6
print ('\033[1m',"¡BIENVENIDO!, ingrese las calificaciones",'\033[0m')
Lista = []
    
try:
    n = 3
    for i in range(n): 
        new_element = float(input("Ingrese nota: ")) 
        Lista.append(new_element)
    print('\033[1m',f"Las calificaciones son: {Lista}",'\033[0m')
    
    Lista_entero = [ float(x) for x in Lista]

    print(f"La primera calificación individual de valor entero es: {Lista_entero[0]}") 
    print(f"La segunda calificación individual de valor entero es: {Lista_entero[1]}")  
    print(f"La tercera calificación individual de valor entero es: {Lista_entero[2]}")

except:
    print("¡Ha ocurrido un error!, los valores no pueden ser convertidos debido a un error de formato")

# ejercicio 7
n=int(input("Ingrese cantidad de filas: "))
def triangulo_pascal(filas):
	fila=[1]
	cero=[0]
	for i in range(filas):
		print(fila)
		fila=[i + d for i, d in zip(fila + cero, cero + fila)]
triangulo_pascal(n)

# ejercicio 8


# ejercicio 9
import random

numero=random.randint(1,100)
intentos=0
jugando=True
print("===ADIVINA UN NUMERO DEL 1 AL 100===")
while jugando:
	intentos += 1
	if intentos <= 7:
		eleccion=int(input("Dime un numero del 1 al 100: "))
		if eleccion==numero:
			print("Has acertado.Has necesitado", intentos, "intentos.")
			jugando=False
		elif eleccion > numero:
			print("Demasiado alto.Llevas" , intentos, "intentos.")
		elif eleccion < numero:
			print("Demasiado bajo.Llevas" , intentos, "intentos.")
	else:
		print("Se te acabaron los intentos. Has perdido.")
		jugando=False

# ejercicio 10
import operaciones
import math
print("Bienvenido al menú interactivo")

while True:
    print("""¿Qué quieres hacer? Escribe una opción
    1) Sumar dos números
    2) Restar dos números
    3) Producto de dos números
    4) División de dos números
    5) Salir""")
    
    opcion=int(input())
    if opcion == 1:
        a=float(input("Introduce un numero: "))
        b=float(input("Introduce un numero: "))

        resultado=operaciones.suma(a, b)
        print(resultado)

    elif opcion == 2:
        a=float(input("Introduce un numero: "))
        b=float(input("Introduce un numero: "))

        resultado=operaciones.resta(a, b)
        print(resultado)

    elif opcion == 3:
        a=float(input("Introduce un numero: "))
        b=float(input("Introduce un numero: "))

        resultado=operaciones.producto(a, b)
        print(resultado)

    elif opcion == 4:
        a=float(input("Introduce un numero: "))
        b=float(input("Introduce un numero: "))

        resultado=operaciones.division(a, b)
        print(resultado)
    elif opcion == 5:
        print("Hasta luego. Un gusto ayudarte.")
        break
    else:
        print("Comando desconocido. Ingresa una opcion valida.")
    