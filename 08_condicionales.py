### Condicionales ###

my_condition = True
print("\n")

if my_condition:
    print("La condición es verdadera")
else:
    print("La condición es falsa")

print("Fin del programa \n")

my_condition = False

if my_condition:
    print("La condición es verdadera")
else:
    print("La condición es falsa")

print("Fin del programa \n")

my_dict = dict({"nombre": "Jhon", "edad": 30})

if "Jhon" in my_dict.values():
    print("El nombre está en el diccionario\n")

my_condition = 5 * 5

if my_condition > 20:
    print("La condición es verdadera\n")

if my_condition > 30:
    print("La condición es verdadera\n")
elif my_condition == 25:
    print("La condición es igual a 25\n")
else:
    print("La condición es falsa\n")

if "Jhon" in my_dict.values() and 32 in my_dict.values():
    print("Usuario encontrado\n")
else:
    print("Usuario no encontrado\n")



