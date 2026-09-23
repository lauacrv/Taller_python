print("ejercicio 1: suma de dos numeros")
print(".."*20)

numero1=float(input("ingrese el primer numero: "))
numero2=float(input("ingrese el segundo numero:"))

print(f"Resultado: {numero1+numero2}")

print("ejercicio 2: Area del rectangulo")
print(".."*20)

base =float(input("ingrese la base del rectangulo"))
altura =float(input("ingrese la altura del rectangulo"))

area = base * altura
print(f"El area del rectangulo es: {area}")

print("ejercicio 3:  Conversión de minutos a horas y minutos")
print(".."*20)
minutos_totales = int(input("ingrese la cantidad de minutos: "))

horas = minutos_totales // 60
minutos = minutos_totales % 60 

print(f"{minutos_totales} minutos son {horas} horas y {minutos} minutos")


print("ejercicio 4: Cálculo del precio con descuento ")
print(".."*20)

precio = float(input("ingrese el precio del producto: "))
descuento = float(input("ingrese el porcentaje de descuento: "))

valor_descuento = precio * (descuento/100)
precio_final = precio - valor_descuento

print(f"El precio final del producto con descuento es: {precio_final:.2f}")

print("ejercicio 5: Intercambio de valores entre dos variables")
print(".."*20)

a=float(input("ingresar el valor de a:"))
b=float(input("ingresar el valor de b:"))

auxiliar= a
a= b
b= auxiliar

print(f"despues del intercambio, el valor de a es: {a} y el valor de b es: {b}")

print("ejercicio 6: calcular el perimetro de un terreono")
print(".."*20)
largo = float(input("ingrese el largo del terreno: "))
ancho = float(input("ingrese el ancho del terreno: "))

print(f"el perimetro del terreno es: {largo*2 + ancho*2}")


print("ejercicio 7: Solicitar tres números y mostrar su promedio")
print(".."*20)

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

promedio = (numero1 + numero2 + numero3) / 3

print(f"El promedio de los tres números es: {promedio:.2f}")

print("ejercicio 8: solicitar una cantidad de segundos y convertirla a horas, minutos y segundos")
print(".."*20)

segundos = float(input("ingrese la cantidad de segundos: "))

minutos = segundos / 60 
horas = segundos / 3600

print(f""" segundos: {segundos}
minutos: {minutos}
horas: {horas}""")

print("ejercicio 9:solicitar un vaslor en pesos colomnianos y mostrar su equivalente aproximado en dolares")
print(".."*20)
pesos = float(input("ingrese la cantidad de pesos colombianos:"))
dolares = pesos / 3137
print(f"el equivalente aproximado en dolares es: {dolares:2f}")

