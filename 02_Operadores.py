### Operadores ###

print(2 + 3) # Suma
print(5 - 1) # Resta
print(4 * 2) # Multiplicacion 
print(10 / 2) # Division
print(10 // 3) # Division entera
print(10 % 3) # Modulo (resto de la division)
print(2 ** 3) # Potencia (2 elevado a la 3)

print("Hola" + " " + "Amigos") # Concatenacion de strings
print("Hola " + str(5)) # Concatenacion de string con un numero, se convierte el numero a string con str()
print("Hola \n" * 5) # Repeticion de string

#\n es un salto de linea, se utiliza para separar el texto en varias lineas.

x = True
print(str(x)) # Convertir un booleano a string con str() para poder concatenarlo con otros strings.

### Operadores de comparacion ###

print(5 > 2) # Mayor que
print(5 < 2) # Menor que
print(4 <= 2) # Menor o igual que
print(4 >= 2) # Mayor o igual que
print(5 == 5) # Igual a
print(5 != 5) # Distinto de
print(2 < 1 == 1) # Operadores de comparacion encadenados, se evalua de izquierda a derecha, primero se evalua 2 < 1, luego el resultado se compara con 1

print("Hola" == "iman") # Comparacion de strings, devuelve True si son iguales, False si son diferentes
print("Hola" != "iman") # Comparacion de strings, devuelve True porque las mayusculas y minusculas son diferentes
print("hola" <= "iman") # Comparacion de strings, devuelve True porque "hola" es menor que "iman" en orden alfabetico
print("hola" >= "iman") # Comparacion de strings, devuelve False porque "hola" es menor que "iman" en orden alfabetico
print("hola" < "iman") # Comparacion de strings, devuelve True porque "hola" es menor que "iman" en orden alfabetico
print("hola" > "iman") # Comparacion de strings, devuelve False porque "hola" es menor que "iman" en orden alfabetico

### Operadores logicos ###

print(True and False) # Operador AND, devuelve True si ambos operandos son True, de lo contrario devuelve False
print(True or False) # Operador OR, devuelve True si al menos uno de los operandos es True, de lo contrario devuelve False
print(not True) # Operador NOT, devuelve el valor contrario del operando, en este caso devuelve False
print(True and not False) # Combinacion de operadores logicos, devuelve True porque not False es True, entonces True and True es True

print(5 > 2 and "Hola" == "Hola") # Combinacion de operadores de comparacion y logicos, devuelve True porque 5 > 2 es True y "Hola" == "Hola" es True, entonces True and True es True
print(5 > 2 or "Hola" == "iman") # Combinacion de operadores de comparacion y logicos, devuelve True porque 5 > 2 es True, entonces True or False es True
print(not (5 > 2)) # Combinacion de operadores de comparacion y logicos, devuelve False porque 5 > 2 es True, entonces not True es False