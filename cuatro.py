#crear menu para vender empanadas
contador = 0
empanadas = []

print("***Lista de Empanadas***")
print("***Menu***")
print("1. Agregar empanadas")
print("2. Mostrar empanadas")
print("3. Salir")

while (contador !=3 ):
    ingredientes = []
    empanada = {}
    contador = int(input("Digite la opción: "))
    if (contador == 1):
        print("Agregando empanada")
        empanada['nombre'] = input("Ingrese el nombre de la empanada: ")
        for i in range (3):
            ingredientes.append(input(f"Ingrese el ingrediente {i+1}: "))
        empanada['ingredientes'] = ingredientes
        empanada['precio'] = int(input("Ingrese el precio: $"))
        empanadas.append(empanada)
    elif (contador == 2):
        print("mostrando empanada")
        print(empanadas)
    elif (contador == 3):
        print("Digitaste salir")
        break
    else:
        print("Opcion invalida")