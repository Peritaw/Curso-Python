class Persona():
    __nombre = None
    __edad = None

    def __init__(self, nombre, edad) -> None:
       self.__nombre = nombre
       self.__edad = edad

    def __metodo_privado(self):
        print('Soy un metodo privado')

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        self.__edad = edad
        
    def __str__(self) -> str:
        return f'Nombre: {self.__nombre} \nEdad: {self.__edad}'
