"""for i in range(2,11,2):
    print(f"{i} - Dracarys 🔥")"""



"""mensaje = input("Escribe tu mensaje : ")
repeticion = int(input("Cuantas vaces quieres repetir el mensaje: "))

for i in range(repeticion):
    print(f"{i+1} - {mensaje}")"""


"""#preguntar al profe: cuantas notas quiere registrar
#hacer promedio de las notas y mostrarlo
#si el valor >= 3.5 mostrar gano - contrario perdio

print("sistema de calificacion")
estudiante = input("nombre del estuciante: ")
can_notas = int(input("cuantas notas vas a registrar: "))

promedio = 0
for i in range(can_notas):
    nota = float(input(f"ingresar la nota {i+1}: "))
    if nota not in range(0, 6):
        print("nota invalida")
        break

    promedio += nota

    print(promedio/can_notas)


promedio_final = promedio/can_notas

if promedio_final >= 3.5:
    print(f"el estudiante {estudiante} - Promedio {promedio_final:.1f} - gano✅")
else: 
    print(f"el estudiante {estudiante} - Promedio {promedio_final:.1f} - perdio❌")"""

while True:
    menu =int(input("""
    Seleccione una opcion: 
    
    1. Sumar
    2. Restar
    3. Salir
    :  """))
    if menu == 1: 
        n1 = int(input("ingrese el numero: "))
        n2 = int(input("ingrese el numero: "))
        print(f"resultado {n1+n2}")
    elif menu == 2:
        n1 = int(input("ingrese el numero uno: "))
        n2 = int(input("ingrese el numero dos: "))
        print(f"resultado {n1-n2}")
    elif menu == 3:
        print("saliendo del programa")
        break
    else:
        print("opcion invalida")