### Diccionarios ###

my_dict = dict() # Para crear un diccionario vacío, se puede usar la función "dict()"
print(type(my_dict))

my_other_dict = {} # Para crear un diccionario vacío, se puede usar la sintaxis de llaves vacías
print(type(my_other_dict))

my_other_dict = {"nombre": "Tony", "apellido": "Stark", "edad": 48, 1: "Python"} # Para crear un diccionario con elementos, se puede usar la sintaxis de llaves con pares clave-valor
print(my_other_dict)

my_dict = {"nombre": "Bruce", "apellido": "Wayne", "edad": 35, "lenguajes": {"Python", "Java", "C++"}} # Un diccionario puede contener otros diccionarios o estructuras de datos como valores
print(my_dict)
print(my_dict["lenguajes"])
print(my_other_dict["nombre"]) # Para acceder a un valor en un diccionario, se puede usar su clave entre corchetes

my_other_dict["nombre"] = "Juan" # Para modificar el valor de una clave en un diccionario, se puede asignar un nuevo valor a esa clave
print(my_other_dict["nombre"])
print(my_other_dict[1]) # Para acceder a un valor en un diccionario, se puede usar su clave entre corchetes, incluso si la clave es un número

my_other_dict["Profesion"] = "Programador" # Para agregar una nueva clave-valor a un diccionario, se puede asignar un valor a una nueva clave
print(my_other_dict)

del my_other_dict[1] # Para eliminar una clave-valor de un diccionario, se puede usar la palabra clave "del" seguida del nombre del diccionario y la clave entre corchetes
print(my_other_dict)

print("nombre" in my_other_dict) # Para verificar si una clave está en un diccionario, se puede usar el operador "in"

print(my_other_dict.items())
print(my_other_dict.keys())
print(my_other_dict.values())

my_new_dict = dict.fromkeys(("nombre", 1)) # Para crear un nuevo diccionario con claves específicas y valores predeterminados, se puede usar el método "fromkeys()"
print(my_new_dict)

my_list = ["nombre", "apellido", "edad"] 
my_new_dict = dict.fromkeys((my_list)) # se pueden usar listas como argumento para el método "fromkeys()"
print(my_new_dict)

my_new_dict = dict.fromkeys(my_list, [3,2,1]) # se pueden usar listas como argumento para el método "fromkeys()"
print(my_new_dict)

print(list(my_dict.keys())) # Para obtener una lista de las claves de un diccionario, se puede usar el método "keys()"
print(list(my_dict.values())) # Para obtener una lista de los valores de un diccionario, se puede usar el método "values()"