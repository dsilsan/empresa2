__author__ = 'David'


class Empleado():
    """
    Clase Empleado
    """
    def __init__(self, nombre, apellidos, dni, direccion, edad, email, salario):
        """
        constructor de la clase empleado

        :param nombre: nombre del empleado
        :param apellidos: apellidos del empleado
        :param dni: dni del empleado
        :param direccion: direccion del empleado
        :param edad: edad del empleado
        :param email: email del empleado
        :param salario: salario del empleado
        :return:
        """
        self.nom = nombre
        self.ape = apellidos
        self.dni = dni
        self.dir = direccion
        self.eda = edad
        self.email = email
        self.sal = salario

    def get_salario(self):
        return self.sal

    def get_dni(self):
        return self.dni

    def get_nombre_apellidos(self):
        return self.nom + " " + self.ape

    def get_edad(self):
        return self.eda

    def get_email(self):
        return self.email

    def get_direccion(self):
        return self.dir

    def get_salario_mensual(self):
        """
        salario mensual del empleado

        :return: devuelve el salario mensual del empleado
        """
        return self.sal/12
