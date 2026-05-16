### Loops (Bucles) ###

# While loop

my_condition = 0

while my_condition < 10:
    print(f"my_condition: {my_condition}")
    my_condition += 1
#el else se puede usar con e while pero no es tan comun
#else:
#    print("La condición es mayor o igual a 10\n")

print("Fin del programa\n")

while my_condition < 20:
    my_condition += 5
    if my_condition == 15:
        print(f"El numero es igual a {my_condition}\n")
        print("se detiene el bucle\n")
        break
    print(f"my condicion: {my_condition}")

### For Loop ###
my_list = [1, 2, 3, 4, 5, 6]

for element in my_list:
    print(f"El numero es: {element}")

print("\n")
for element in my_list:
    if element % 2 == 0:
        print(f"El numero {element} es par")
    else:
        print(f"El numero {element} es impar")


my_list = [1, 2, 3, 4, 5, 6]

for element in my_list:
    print(f"El numero es: {element}")

dictaa = {"nombre": "Jhon", "edad": 30, "ciudad": "New York"}

print("\n")

for element in dictaa.values():
    print(f"El valor es: {element}")
    if element == "edad":
        print("Se ha encontrado la edad\n")
        break
else:
    print("El bucle ha terminado\n")

print("\n")

setaa = {"Python", "JavaScript", "C++", "Java"}

for element in setaa:
    print(f"El elemento es: {element}")

for element in dictaa.values():
    if element == "Jhon":
        print("Se ha encontrado Jhon\n")
        continue
    print(f"El elemento es: {element}")
