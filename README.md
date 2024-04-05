# pdc_reto_8
### Soy Rafael Santiago Chirivi Peña y pertenezco al grupo de "Fenomenoides", adelante se muestra nuestro logo 

<details><summary>Preparense para ver el grandioso logo: </summary><p>
<div align='center'>
<figure> <img src="https://i.postimg.cc/NFbwf57S/logo-def.png" alt="Defensa Civil" width="400" height="auto"/></br>
<figcaption><b> "somos programadores, no diseñadores" </b></figcaption></figure>
</div>
</p></details><br>

### A continuacion, se muestran las soluciones propuestas a los distintos puntos de este reto
## 1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

```python
if __name__ == "__main__":
    for i in range (1, 101): #planteamiento del rango especificado (1 a 100)
        i_cuadrado = i ** 2 # calculo del cuadrado para cada numero dentro del rango
        print(f"El cuadrado de {i} es {i_cuadrado}") # impresion del numero y su cuadrado
```

## 2.  Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

```python
if __name__ == "__main__":
    print("Numeros impares")
    for i in range (1, 1000, 2): # planteamiento del rango especificado para impares (1 a 999) con escalado de 2 para saltar pares
        print(f"{i}") # impresion del impar
    print("")
    print("Numeros pares")
    for i in range (2, 1001, 2): # planteamiento del rango especificado para pares (2 a 1000) con escalado de 2 para saltar impares
        print(f"{i}") # impresion del par
```

## 3.  Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

```python
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
```

## 4. Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial

```python
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
```

## 5. Calcular el valor de 2 elevado a la potencia n usando ciclos for.

```python
exp : int = 1   # constante de potencia neutro
if __name__ == "__main__":
    try:
        n : int = int(input("Ingrese el exponente para la base 2: "))   # ingreso del exponente
        if n >= 0 or n <= 0:    # inicio de secuencia con potencia neutro
            print(f"2 ** 0 = {exp}")
        if n > 0:   # exponente positivo
            for i in range (1, n + 1):  # planteamiento del rango (1, n) para el numero de multiplicaciones por si mismo para la base
                exp *= 2    # multiplicacion de base por si mismo
                print(f"2 ** {i} = {exp}")  # impresion de cada exponente hasta n
        if n < 0:   # exponente negativo
            n *= -1     # cambio de signo para el exponente
            for i in range (1, n + 1):  # planteamiento del rango (1, n) para el numero de multiplicaciones por si mismo para la base
                exp *= 2    # multiplicacion de base por si mismo
                print(f"2 ** -{i} = 1/{exp} ({1/exp})")     # reexpresion de exponente negativo 2 ^ -n = 1 / 2 ^ n e impresion de cada exponente hasta n
    except ValueError:
        print("El valor ingresado no se trata de un numero entero")
```

## 6. Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. **Disclaimer:** Trate de no utilizar el operador de potencia (**).

```python
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
```

## 7. Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

```python
if __name__ == "__main__":
    for i in range (1, 10): # planteamiento del rango (1, 9) para las tablas
        print(f"tabla del {i}") 
        for n in range (1,11): # planteamiento del rango (1, 10) para la multiplicacion de cada tabla
            mult = i * n # resultado de la multiplicacion 
            print(f"{i} * {n} = {mult}") # impresion de la multiplicacion
        print("")
```

## 8. Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. **Nota:** use *math* para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.
$$e^x \approx exp(x,n) \approx \sum_{i=0}^{n}\frac{x^i}{i!}$$

```python
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
```

## 9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. **Nota:** use *math* para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
$$sin(x) \approx sin(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)!}$$

```python
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
```

## 10. Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. **Nota:** use *math* para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.
$$arctan(x) \approx arctan(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)}$$


```python
from math import atan # importacion de funcion arcotangente 
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
```
