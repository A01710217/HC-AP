#Promedio

def promedio():
    n = int(input("Cuantos numeros vas a promediar? "))
    suma = 0
    for i in range(n):
        suma = suma + float(input("Dame un numero: "))
    print(f"El promedio es: {suma/n}")

promedio()