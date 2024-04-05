exp : int = 1   # constante de potencia neutro
if __name__ == "__main__":
    try:
        x : int = int(input("Ingrese la base de la potencia: "))    # ingreso de la base
        n : int = int(input("Ingrese el exponente para la base: "))     # ingreso del exponente
        if n >= 0 or n <= 0:    # inicio de secuencia con potencia neutro
            print(f"{x} ** 0 = {exp}")
        if n > 0:   # exponente positivo
            for i in range (1, n + 1):  # planteamiento del rango (1, n) para el numero de multiplicaciones por si mismo para la base
                exp *= x     # multiplicacion de base por si mismo
                print(f"{x} ** {i} = {exp}")  # impresion de cada exponente hasta n
        if n < 0:   # exponente negativo
            n *= -1     # cambio de signo para el exponente
            for i in range (1, n + 1):  # planteamiento del rango (1, n) para el numero de multiplicaciones por si mismo para la base
                exp *= x    # multiplicacion de base por si mismo
                print(f"{x} ** -{i} = 1/{exp} ({1/exp})")     # reexpresion de exponente negativo x ^ -n = 1 / x ^ n e impresion de cada exponente hasta n
    except ValueError:
        print("El valor ingresado no se trata de un numero entero")