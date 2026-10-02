while True:
    try: 
        cantidad_estudiantes = int(input("ingrese la cantidad de estudiantes: "))
        if cantidad_estudiantes >0:
            break
        else:
            print("La cantidad debe ser mayor a 0")

    except ValueError:
        print("Debe ingresar un número entero")

suma_promedio=0
aprobado=0
reprobados=0


for estudiante in range (1, cantidad_estudiantes):
    print("Estudiante", estudiante)
    nombre=input("Nombre: ")

    while True:
        try:
            nota1=float(input("Primera nota (0-5): "))
            if nota1 >= 0 and nota1 <=5:
                break
            else:
                print("La nota debe estar entre 0 y 5")

        except ValueError:
            print("Debe ingresar un número valido")

    while True:
        try:
             nota2=float(input("Segunda nota (0-5): "))
             if nota2 >= 0 and nota2 <=5:
                 break
             else:
                print("La nota debe estar entre 0 y 5")
            
        except ValueError:
            print("Debe ingresar un número valido")
            

    while True:
        try:
            nota3=float(input("Tercera nota (0-5): "))
            if nota3 >= 0 and nota3 <=5:
             break
            else:
               print("La nota debe estar entre 0 y 5")
                        
        except ValueError:
            print("Debe ingresar un número valido")

    promedio=(nota1+nota2+nota3)/3
    if promedio >=3:
        print("Promedio", round(promedio))
        print("Estado: Aprobado")
        aprobado= aprobado+1
    else:
        print("Promedio", round(promedio))
        print("Estado: Reprobado")
        reprobados= reprobados+1 

    suma_promedio = suma_promedio + promedio 

    #calcular promedio general
    promedio_grupo = suma_promedio / cantidad_estudiantes

    #mostrar resumen
    print("\n==============================")
    print("       RESUMEN DEL GRUPO")
    print("==============================")
    print("Total estudiantes:", cantidad_estudiantes)
    print("Aprobados:", aprobado)
    print("Reprobados:", reprobados)
    print("Promedio general:", round(promedio_grupo, 2))
    print("==============================")


            






    