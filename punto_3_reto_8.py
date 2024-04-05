if __name__ == "__main__":
    try:
        n : int = int(input("Por favor, ingrese un numero entero mayor que dos para comenzar la sucesion: ")) # ingreso del entero n
        while n < 2: # condicion de ser mayor que 2
            n = int(input("EL numero ingresado no se encuentra dentro de la condicion establecida, intentelo de nuevo: "))
        if n%2 != 0: # si es impar, llevarlo al par mas cercano (n - 1)
            n -= 1
        if n%2 == 0: 
            for i in range (n, 1 ,-2): # planteamiento del rango especificado (n , 2) con escalado -2 para ir decreciendo en pares 
                print(i) # impresion del par
    except ValueError: 
        print("El numero ingresado no se trata de un numero entero")