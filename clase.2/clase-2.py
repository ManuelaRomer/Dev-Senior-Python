# Conversión de datos 
altura = 80 
peso = "80" 

pesoNum = int(peso)
pesoNumFloat = float(peso)

peso2 = str(pesoNumFloat)

print(peso == peso2)


#Ejercicio 1 

def is_float(value): 
    try: 
        float(value)
        return True 
    except ValueError: 
        return False

inputUsuario = input("Ingrese el primer numero:")

#verificar si el dato ingresado es numerico
isFloat = is_float(inputUsuario)


if not isFloat: 
    inputUsuario = input("El numero no es valido, ingrese el primer numero: ")

numero1 = float(inputUsuario)

numero2 = float(input("Ingrese el segundo numero: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
división = numero1 / numero2 

print("suma: ", suma)
print(f"suma: {suma}")
print(f"resta: {resta}")
print(f"multiplicacion: {multiplicacion}")
print(f"división: {división}")
