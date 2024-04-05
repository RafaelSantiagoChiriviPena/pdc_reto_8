fact : int = 1 # constante de factorial base
if __name__ == "__main__":
    try:
        n : int = int(input("Ingrese un numero entero positivo al que obtener el factorial: ")) # ingreso de n para n!
        while n < 0:
            n = int(input("El numero ingresado no se trataba de un entero positivo, por favor intentelo de nuevo: "))
        if n == 0: # condicion para factorial base = 1
            print(f"el factorial de {n} es {fact}")
        for i in range (fact , n+1): # planteamiento del rango especificado (1, n) 
            fact = fact * i # operacion de factorial desde 1 hasta n
            print(f"el factorial de {i} es {fact}") # impresion de cada factorial hasta n!
    except ValueError:
        print("El numero ingresado no se trata de un numero entero positivo")