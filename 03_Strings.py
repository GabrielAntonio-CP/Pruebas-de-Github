### Strings ###

my_string = "Mi string"
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "este es un string\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un string \n escapado"
print(my_scape_string)

# Formateo ###
name, surname, age = "Pedro", "Perez", 23

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))

print(f"Mi nombre es {name} {surname} y mi edad es {age}, tercera prueba")

#Desempaquetado de caracteres 
language = "Python"
a,b, c, d, e, f = language
print(a)
print(f)

# Division de strings

language_slice = language[2:5]
print(language_slice)

# Reverso de un string
reversed_language = language[::-1]
print(reversed_language)

#Funciones del sistema

print(language.capitalize())
print(language.upper())
print(language.count("h"))
print(language.isnumeric())
print(language.isalpha())
print(language.split("t"))
print(language.lower().count("o"))
print(language.startswith("Pyt"))