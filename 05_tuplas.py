### Tuplas ###

my_tuple = tuple() # Creamos una tupla vacia
my_other_tuple = (60, 1.80, 'Maria', 'Gomez') # Creamos una tupla con elementos

my_tuple = (35, 1.77, 'Juan', 'Perez') # Creamos una tupla con elementos
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

try:
    print(my_tuple[4]) # IndexError: tuple index out of range
except IndexError as e:
    print("Error: " + str(e) + "\n")

print(my_tuple.count(35)) #.count cuenta el numero de veces que aparece un elemento en la tupla
print(my_tuple.index('Juan')) #.index devuelve la posición del primer elemento que coincida con el valor que se le indique

my_sum_tuple = my_tuple + my_other_tuple # La concatenación de tuplas crea una nueva tupla con los elementos de ambas tuplas
print(my_sum_tuple)

print(my_sum_tuple[3:6]) # Podemos acceder a un rango de elementos de la tupla utilizando slicing, al igual que con las listas 
# el 3 es el indice de inicio y el 6 es el indice de fin (no incluido)

my_tuple = list(my_tuple) # Convertimos la tupla en una lista para poder modificarla
my_tuple[0] = 30 # Modificamos el primer elemento de la lista
my_tuple = tuple(my_tuple) # Convertimos la lista de nuevo en una tupla
print(my_tuple)

del my_tuple # Eliminamos la tupla, no es recomendable eliminar una tupla, ya que no se pueden modificar sus elementos, pero es posible eliminarla completamente de la memoria

try:
    print(my_tuple) # NameError: name 'my_tuple' is not defined
except NameError as e:
    print("Error: " + str(e) + "\n")