from math import atan
def arctan (x : float, n : int = 10, fun : float = 0) -> float:
    for i in range (0, n + 1): # planteamiento del rango (0, n) para la sumatoria
        fun += (-1) ** i * ((x ** (2 * i + 1)) / (2 * i + 1)) # sumatoria de serie de mclaurin para aproximacion del arcotangente 
    return fun
if __name__ == "__main__":
    try:
        x : float = float(input("Ingrese a x, recuerde que este debe estar en un rango de -1 a 1: ")) # Ingreso de valor para la arcotangente
        while x < -1 or x > 1 or x == 0:
            x = float(input("El x ingresado no corresponde al rango establecido, intentelo de nuevo: "))
        n : int = int(input("Ingrese a n: ")) # ingreso de numero de sumas
        arctan_real = atan(x) # funcion arcotangente importada
        arctan_aprox = arctan(x, n) # funcion arcotangente aproximada
        print(arctan_aprox) 
        print(arctan_real) 
        error : float = abs(arctan_real - arctan_aprox) / arctan_real * 100 # porcentaje de error entre funcion real y aproximacion
        print(f"{error}%")
    except ValueError:
        print("El valor ingresado no se trata de un numero real / entero")

    # con 10 sumas, el valor a partir del que el margen de error es de 0.1% es con una x = 0.855 O x = -0.855