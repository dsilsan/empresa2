__author__ = 'David'

from Empleado import *
from Departamento import *
class Empresa():
    def __init__(self, nombre_empresa, cif, razon_social):
        """
        constructor de la clase empresa

        :param nombre_empresa: nombre de la empresa
        :param cif: identificador de la empresa
        :param razon_social: razon social de la empresa
        :return:
        """
        self.nom = nombre_empresa
        self.cif = cif
        self.rs = razon_social
        self.lDepartamentos = []
    def nuevoDept(self, dep):
        self.lDepartamentos.append(dep)

emp=Empleado( "david", "silva","49028333s", "c/catania nº15", 24, "david@msn.es", 2500)
dep=Departamento("Informatica", 1)
dep.intro_empleado(emp)
emp=Empresa("Epd7","492015764p","SA")
emp.nuevoDept(dep)