from math import sin # importacion de funcion seno

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

def sen (x : float, n : int = 10, fun : float = 0) -> float:
    for i in range (0, n + 1): # planteamiento del rango (0, n) para la sumatoria
        fun += (-1) ** i * ((x ** (2 * i + 1)) / factorial_funcion(2 * i + 1)) # sumatoria de serie de mclaurin para aproximacion del seno 
    return fun
if __name__ == "__main__":
    try:
        x : float = float(input("Ingrese a x: ")) # Ingreso de valor para el seno
        while x == 0:
            x = float(input("El valor ingresado no es aceptado para la funcion, intentelo de nuevo: "))
        n : int = int(input("Ingrese a n: ")) # ingreso de numero de sumas
        sen_real = sin(x) # funcion seno importada
        sen_aprox = sen(x , n) # funcion seno aproximada
        print(sen_aprox)
        print(sen_real)
        error : float = abs(sen_real - sen_aprox) / sen_real * 100 # porcentaje de error entre funcion real y aproximacion
        print(f"{error}%")
    except ValueError:
        print("El valor ingresado no se trata de un numero real / entero")
    
    # con 10 sumas, el valor a partir del que el margen de error es de 0.1% es con una x = 6.79 O x = -6.79