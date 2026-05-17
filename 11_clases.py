### Clases ###

class MyEmptyPerson: #una buena practica es utilizar camel case para definir el nombre de una clase
    pass

class Person:
    def __init__(self, name, surname): #el "init" es una palabra reservada de python que sirve para iniciar un constructor
        #hay que almacenar los datos utilizando self(nombredeparametro) = variable con el parametro
        #esto crea las propiedades del objeto
        self.name = name
        self.surname = surname

class Person2:
    def __init__(self, name, surname): 
        self.fullname = f"{name} {surname}"
        self.__name = name
        self.__surname = surname #de esta manera se definen variables privadas para no poder modificarse

    def walk (self): #se debe se pasar self siempre que se quieran usar parametros de la misma clase
        print(f"{self.fullname} Esta caminando")
    
    def get_name (self):
        return self.__name

       

my_person = Person("juan","perez")
print(f"{my_person.name} {my_person.surname}") #podemos crear propiedades con la concatenacion de nuestros parametros recibidos

my_person2 = Person2("Luis", "Valentino")
print(my_person2.fullname)
my_person2.walk()
my_person2.get_name()

my_person2.fullname = "Alice M. la CEO"
print(my_person2.fullname)
my_person2.walk()