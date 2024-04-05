from math import exp # importacion de funcion exponencial

def factorial_funcion (num : int) -> int: 
    fact : int = 1      #constante 
    numero : int = 1    #constante
    while num > 1: #limite de regresion
        fact = fact * num #operacion de factorial
        num -= 1 #regresion hasta 1
        numero += 1
    if num == 0: #caso especial 0!
        fact = 1
        numero = 0
    return fact

def expo (x : float, n : int = 10, fun : float = 0) -> float:
    for i in range (0, n + 1): # planteamiento del rango (0, n) para la sumatoria
        fun += (x ** i) / factorial_funcion(i) # sumatoria de serie de mclaurin para aproximacion exponencial
    return fun
if __name__ == "__main__":
    try:
        x : float = float(input("Ingrese a x: ")) # Ingreso de exponente para e 
        n : int = int(input("Ingrese a n: ")) # ingreso de numero de sumas
        expo_real = exp(x) # funcion exponencial importada
        expo_aprox = expo(x, n) # funcion exponencial aproximada
        print(expo_aprox)
        print(expo_real)
        error : float = abs(expo_real - expo_aprox) / expo_real * 100 # porcentaje de error entre funcion real y aproximacion
        print(f"{error}%")
    except ValueError:
        print("El valor ingresado no se trata de un numero real / entero")

    # con 10 sumas, el valor a partir del que el margen de error es de 0.1% es con una x = 3.5 O x = -2.19