### Listas ###

#Formas de crear una lista
my_list = list()
my_other_list = []

# Comprobando el tipo de dato
print(type(my_list))
print(len(my_list))

my_list = [4, 6, 22, 22, 54, 12, 22]

my_list.append(22)

print(len(my_list))
print(my_list)

my_other_list = [34, 1.44, 'Juan', 'luis']

# Si quieres desempaquetar una lista, el numero de variables debe ser igual al numero de elementos de la lista y deben estar en el mismo orden
age, height, name, surname = my_other_list
print(my_other_list)

print(type(my_other_list))

# Accediendo a los elementos de la lista
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[2])
print(my_other_list[3])
print(my_other_list[-1])
print(my_other_list[-2])
print(f"{my_other_list[-3]} \n")
print(my_other_list.count('Juan'))
print(f"El numero 22 aparece {my_list.count(22)} veces en la lista")


try:
    print(my_other_list[-5]) # IndexError: list index out of range
except IndexError as e:
    print("Error: " + str(e) + "\n\n")

print(my_list + my_other_list)

my_other_list.append("Python") #.append agrega un elemento al final de la lista
print(my_other_list)

my_other_list.insert(2, 18) #.insert agrega un elemento en la posición que se le indique
print(my_other_list)

my_other_list.remove("Juan") #.remove elimina el primer elemento que coincida con el valor que se le indique
print(my_other_list)

my_list.remove(22) #.remove elimina el primer elemento que coincida con el valor que se le indique
print(my_list)

my_list.pop() #.pop elimina el ultimo elemento de la lista
print(my_list)

print(my_list.pop(1)) #.pop elimina el elemento en la posición que se le indique y lo devuelve 
reserva = my_list.pop(1)
print(reserva)

print(my_list)
del my_list[3] #del elimina el elemento en la posición que se le indique
print(my_list)

my_new_list = my_list.copy()
my_list.clear() #.clear elimina todos los elementos de la lista
print(my_list)

print(my_new_list)
my_new_list.reverse() #.reverse invierte el orden de los elementos de la lista
print(my_new_list)

my_new_list.sort() #.sort ordena los elementos de la lista de menor a mayor
print(my_new_list)