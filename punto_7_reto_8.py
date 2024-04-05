if __name__ == "__main__":
    for i in range (1, 10): # planteamiento del rango (1, 9) para las tablas
        print(f"tabla del {i}") 
        for n in range (1,11): # planteamiento del rango (1, 10) para la multiplicacion de cada tabla
            mult = i * n # resultado de la multiplicacion 
            print(f"{i} * {n} = {mult}") # impresion de la multiplicacion
        print("")