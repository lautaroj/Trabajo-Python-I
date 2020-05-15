# 1)Complete en un script que muestre como resultado los elementos f, g y h. Explique la solución.
#   `lettters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]`
def show(letters):
            for x in range(len(letters)):
                if letters[x]=="f" or letters[x]=="g":
                    print(letters[x])
                elif letters[x]=="h":
                    print(letters[x])
    #Se toma cada valor del array, y se lo devuelve si cumple el requerimiento de igualdad con alguna de las letras.

# 2)Tomando dos valores del usuario, calculamos la multiplicación
def producto(x,y):
    print(x*y)

# 3)Mostrar la salida de una la lista de 5 números flotantes ingresados por el usuario.
def show(arr):
    for x in range(5):
        print(arr[x])

# 4)Como puedo saber si el archivo permisos.txt, está vació o no ?
import os
archivo = "permisos.txt"
datos = os.stat(archivo)
if datos.st_size == 0:
    print("El archivo está vacío")

# 5)Como puedo leer la línea 4 del archivo test.txt cuyo contendio es el que sigue:
    # línea 1
    # línea 2
    # línea 3
    # línea 4
    # línea 5
    # línea 6
text = open("test.txt")
lector = text.readlines()
print(lector[3])

# 6)Partiendo de la lista a continuación, mostrá solamente los números divisibles por 5. La iteración se debe detner cuando encuentre un número mayor a 150
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for x in range(len(list1)):
    if list1[x]%5 == 0:
        if list1[x]<151:
           print(list1[x])    

# 7)Quiero que imprimas el siguiente patrón. Fundamenta la solución.
    # 5 4 3 2 1 
    # 4 3 2 1 
    # 3 2 1 
    # 2 1 
    # 1
    
for x in range(5):
    for y in range(5 - x, 0, -1):
        print(y, end=' ')
    print()

    #Se crea un loop en el que "x" va desde 0 hasta 4, y se imprime una "y" que comienza en 5 y en cada iteración
    #el comienzo desciende en "x", es decir cuando "x"=0, el comienzo de "y"=(5-0), luego (5-1) y así sucesivamente.
    #También se marca que el ciclo termine en 0, y que ascienda en -1, es decir que descienda

# 8)(Solo en Python) Si ejecuto el siguiente script, pienso que tendré un error. Cómo puedo lograr evitarlo y que muestre un mensaje "Listo!" ?
for i in range(10):
    print(i)
print("Listo!")

# 9)(Solo en Python) Partiendo de la siguiente función dataEstudiante(nombre, edad), como podría llamarla usando esta función pero reutilizándola y asignándole un nuevo nombre como mostrarEstudiante(nombre, edad)
# def dataEstudiante(nombre, edad):
#     print(nombre, edad)
# dataEstudiante("Victor", 36)

def dataEstudiante(nombre, edad):
    print(nombre, edad)

mostrarEstudiante = dataEstudiante

# 10)(Solo en Python) Explicar que hace esta función y por qué ?
def dataEmpleado(nombre, salario=29000):
    print("Empleado", nombre, "El sueldo es:", salario)

    #Al llamar a la funcion y otorgarle los datos, se imprime el nombre y el sueldo deseado (sobreescribiendo el predeterminado).
    #Pero si no se le torga ningún dato de sueldo, el valor automático sería 29000, ya que se encuentra previamente establecido en la función.
    
# 11)Partiendo de dos strings: str1 y str2, necesito una función que cree una nueva y única cadena formada por el primero,
#el medio y el último carácter de str1 y str2
def mixStr(str1,str2):
    primeraletra1 = str1[0]
    primeraletra2 = str2[0]
    letramedio1 = str1[int(len(str1)/2)]
    letramedio2 = str2[int(len(str2)/2)]
    letrafinal1 = str1[-1]
    letrafinal2 = str2[-1]

    print(primeraletra1+primeraletra2+letramedio1+letramedio2+letrafinal1+letrafinal2)

# 12)Necesito saber que un script me pueda informar cuantas ocurrencias se dan por cada letra en el siguiente string “acoltrapersobrabilacodaNaNy!
palabra = "acoltrapersobrabilacodaNaNy"
contador = {}
for x in palabra:
    if x in contador:
        contador[x]+=1
    else:
        contador[x]=1
print(contador)

# 13)Un vecino de Cañuelas cría gallínas, vacas y cerdos. Necesitamos saber cuantas patas hay en total entre todas las especies.
#Ahora resulta que un programador anterior, le envió un e-mail al granjero con el siguiente array y el mensaje, "perdón, pero no puedo seguir"*/
#  animales(12,23,11) = 12*2 23*4 11*4
def animales(gallinas, vacas, cerdos):
    patasG = gallinas*2
    patasV = vacas*4
    patasC = cerdos*4
    print(patasG+patasV+patasC)

animales(12,23,11)