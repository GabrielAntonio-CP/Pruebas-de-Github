### Funciones ###

def my_function():
    print("Esto es una funcion\n")

my_function()

def sum_two_numbers(num1, num2):
    print(f"La suma es {num1 + num2}\n")

sum_two_numbers(5, 10)
sum_two_numbers("3", "7")
sum_two_numbers(5.4, 10.432)

def sum_two_numbers_return(num1, num2):
    return num1 + num2

#si no asignamos a una varable la funcion, despues no podremos acceder al resultado devuelto por la misma
resultado = sum_two_numbers_return(4,5)
print(resultado)

#tambien podemos usarlo directamente desde la funcion
print(sum_two_numbers_return(3,2) + sum_two_numbers_return(54,6))

def print_name (name,surname):
    print(f"{name} {surname}")

print_name("Jesus","Lopez")
print_name(surname="Perez",name="Many")#se pueden ordenar los parametros en cualquier orden siempre y cuando se especifique

def print_name_whit_default (name,surname,alias = "sin alias"): #en caso de no colocar un parametro se puede elegir un parametro por defecto
    print(f"{name} {surname} {alias}")

print_name_whit_default("brais","moure","mouredev")
print_name_whit_default("Jesus","Perez",)

def print_texts(*text):
    for texts in text:
        print(texts.upper())

print_texts("hola","amarillo","hello")
