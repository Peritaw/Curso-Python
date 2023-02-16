class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def detallePersona(self):
        print(f'Nombre: {self.nombre} \nEdad: {self.edad}')

    def __str__(self) -> str:
        return f'Nombre: {self.nombre} \nEdad: {self.edad}'

class Cliente(Persona):
    pass

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo) -> None:
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def detalleEmpleado(self):
        super().detallePersona()
        print('Sueldo: ', self.sueldo)

    def __str__(self) -> str:
        return super().__str__() + f'Sueldo: {self.sueldo}'