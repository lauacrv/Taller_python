

"""print("Por favor ingrese los siguientes datos\n")

var_nombre = input("Nombre: ")
var_edad = int(input("Edad: ")) 

#crear condicion

if var_edad >= 18 :
    print(f"{var_nombre} Eres mayor de edad")
else:
    print(f"{var_nombre} Eres menor de edad")"""

#crear condicion

"""print("Ejercicio: nota final")

var_nombre = input("Nombre: ")
var_notafinal = float(input("Nota final: "))

if var_notafinal < 0 or var_notafinal > 5: 
    print("Nota invalida ❔")

elif var_notafinal >= 3.5 :
    print(f"Estudiante {var_nombre} Gano ✅")

else: 
    print(f"Estudiante {var_nombre} Perdio ❌") """  

"""print("ejercicio: determinar si el numero es positivo, negativo o cero")

var_numero = float(input("Número:"))

if var_numero > 0:
    print(f"{var_numero} Positivo")

elif var_numero < 0: 
    print(f"{var_numero} Negativo")

else:
    print("El numero es cero")"""

"""print("ejercicio: par o impar")
 
var_numero = int(input("Número:"))

if var_numero % 2 == 0:
    print("{var_numero} par")
else:
    print("{var_numero} impar")"""

"""print("Ejercicio: el mayor de tres numeros")

var_numero1 = float(input("Número1:"))
var_numero2 = float(input("Número2:"))
var_numero3 = float(input("Número3:"))

if var_numero1 >= var_numero2 and var_numero1 >= var_numero3:
    mayor = var_numero1

elif var_numero2 >= var_numero1 and var_numero2 >= var_numero1:
    mayor = var_numero2
else: 
    mayor = var_numero3

print(f"El mayor de los numeros es {mayor}")"""

"""print("ejercicio: edad")

var_nombre = input("¿cual es tu nombre?: ")
var_edad = int(input("¿cual es tu edad?: "))

if var_edad <= 0:
    print("edad no identificada")

elif var_edad >= 18:
    print(f"hola {var_nombre} tu edad es {var_edad} SI puedes entrar")

else:
 print(f"hola {var_nombre} tu edad es {var_edad} por lo tanto NO puedes entrar ")
"""




"""print("ejercicio con rango de notas")

nombre= input("nombre: ")
nota= float(input("nota: ")) 
if nota < 0 or nota > 5:
    print(f"{nota} inavalida")

elif nota < 3:
    print(f"{nota} insuficiente")

elif nota <3.5:
    print(f"{nota} aceptable")
elif nota <4.5:
    print(f"{nota} bueno")
else:
    print(f"{nota} excelente")"""

print("ejercicio: descuento de precios")

nombre =input("nombre: ")
total_compra= float(input("total compra: "))

if total_compra < 100000 :
    print(f"""
          -Cliente{nombre}
          -Compra "{total_compra} no tiene descuento "
          """)
    
elif total_compra < 299999:
    print(f"""
    -Cliente {nombre}
    -Compra {total_compra}
    -Descuento {total_compra * 0.1} 
    -total a pagar {total_compra - (total_compra * 0.1)}

""")
elif total_compra < 499999:
    print(f"""
    -Cliente {nombre}
    -Compra {total_compra}
    -Descuento {total_compra * 0.15} 
    -total a pagar {total_compra - (total_compra * 0.15)} 

""")
elif total_compra >= 500000:
    print(f"""
    -Cliente {nombre}
    -Compra {total_compra}
    -Descuento {total_compra * 0.20} 
    -total a pagar {total_compra - (total_compra * 0.20)} 

""") 

print("ejercicio: 5")


    
            

