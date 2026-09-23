
#creacion de variables
nombre = "Lau" #Variable String (texto)
documento = 123 #Variable tipo entero 
direccion = "Medellin crr 45"

tiene_deudas = True

#Mostrar informacion en pantalla 
print(nombre)

print("CONCATENACION USANDO +")
print("=" * 30) 

#Opcion 1: usando + No recomendado
print("Mi nombre es: " + nombre + " Mi documento es: " + str(documento))

#opcion 2: usando , recomendado
print("\nCONCATENACIÓN USANDO ,")
print("=" * 30)
print("Mi nombre es: ", nombre, " Mi documento es: ", documento , " Mi direccion es: ", direccion , " Mi estado de deudas es: ", tiene_deudas)


print("\nCONCATENACIÓN USANDO F-STRINGS")
print("=" * 30)

print(f"Mi nombre es: {nombre}, Mi documento es: {documento}, Mi direccion es: {direccion}, Mi estado de deudas es: {tiene_deudas}")

print("\nMOSTRAR VARIAS VARIABLES CON F-STRINGS")
print("=" * 30)

print(f"""-Nombre: {nombre}
-Documento: {documento}
-Direccion: {direccion}
-Tiene Deudas: {tiene_deudas}
""")

print(f"\n Hola, {nombre}!")
print(f"¡Bienvenida, {nombre} a Python. \n")