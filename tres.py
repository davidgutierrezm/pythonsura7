#crer un menu 
contador = 0
pueblos = []
print("***Enamorate de Antioquia***")
print("***Menu***")
print("1. Agregar pueblos")
print("2. Mostrar rutas")
print("3. Salir")
while (contador !=3 ):
    pueblo = {}
    contador = int(input("Digita una opción: "))
    if (contador ==1):
        print("Agregando pueblo: ")
        pueblo['nombre'] = input("Ingrese el nombre del pueblo: ")
        pueblo['Distancia'] = int(input("Ingrese la distancia del pueblo: "))
        pueblo['poblacion'] = int(input("Ingrese el número de personas en el pueblo: "))
        pueblos.append(pueblo)
    elif (contador ==2):
        print("Mostrando rutas: ")
        print(pueblos)
    elif (contador ==3):
        print("Digitaste salir")
        break
    else:
        print("Opcion invalida")