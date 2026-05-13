### Sets ###

my_set = set()
print(type(my_set))

my_other_set = {} # Esto no es un set, es un diccionario vacío, pero asi es la sintaxis de un set vacío
print(type(my_other_set))

my_other_set = {"juan", "perez", 35} 
print(type(my_other_set))

# print(my_other_set[2]) # No se puede acceder a los elementos de un set por su índice, ya que no tienen un orden específico

my_other_set.add("programador")
print(my_other_set)

#Un set no es una estructura de datos ordenada, por lo que no se pueden acceder a sus elementos por su posición

my_other_set.add("juan") # No se pueden agregar elementos duplicados a un set, por lo que este elemento no se agregará
print(my_other_set)

print("juan" in my_other_set) # Para verificar si un elemento está en un set, se puede usar el operador "in"
print("maria" in my_other_set)

my_other_set.remove("perez") # Para eliminar un elemento de un set, se puede usar el método "remove()"
print(my_other_set)

my_other_set.clear() # Para eliminar todos los elementos de un set, se puede usar el método "clear()"
print(my_other_set)
print(len(my_other_set)) # Para obtener la cantidad de elementos de un set, se puede usar la función "len()"

my_other_set.update(["maria", "garcia", 28]) # Para agregar varios elementos a un set, se puede usar el método "update()"
print(my_other_set)

del my_other_set # Para eliminar un set completo, se puede usar la palabra clave "del"
#print(my_other_set) # Si intentamos imprimir un set que ha sido eliminado, obt

my_set = {"juan", "perez", 35}
my_list = list(my_set) # Para convertir un set a una lista, se puede usar la función "list()"
print(my_list)

my_other_set = {"maria", "garcia", 28}
my_new_set = my_set.union(my_other_set).union({"luis", "lopez"}) # Para unir dos sets, se puede usar el método "union()"
print(my_new_set)

print(my_new_set.difference(my_set)) # Para obtener los elementos que están en un set pero no en otro, se puede usar el método "difference()"
print(my_new_set.intersection(my_set)) # Para obtener los elementos que están en ambos sets
