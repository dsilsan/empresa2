from unittest import TestCase
from src.Departamento import *
from src.Empleado import *
from mockito import *
from src.Empresa import *
__author__ = 'David'


class TestDepartamento(TestCase):
    """
    Clase TestDepartamento
    """

    emp=Empleado( "david", "silva","49028333s", "calle catania n15", 24, "david@msn.es", 2500)
    dep=Departamento("Informatica", 1)
    dep.intro_empleado(emp)
    emp=Empresa("Epd7","492015764p","SA")
    emp.nuevoDept(dep)
    def test_get_salario_total(self):
        """
        test realizados mediante mocks sobre el metodo get_salario_total()

        :return:
        """
        res = Departamento("Informatica", 1)
        # Generate a mock from a class
        emp1 = mock(Empleado)
        emp2 = mock(Empleado)
        emp3 = mock(Empleado)
        # Mock method calls
        when(emp1).get_salario().thenReturn(4000)
        when(emp2).get_salario().thenReturn(4000)
        when(emp3).get_salario().thenReturn(4000)
        res.intro_empleado(emp1)
        res.intro_empleado(emp2)
        res.intro_empleado(emp3)
        print(res.get_salario_total())
        self.assertNotEqual(res, 12000)

    def test_get_salario_total_mensual(self):
        """
        test realizados mediante mocks sobre la clase get_salario_total_mensual()

        :return:
        """
        res = Departamento("Informatica", 1)
        # Generate a mock from a class
        emp1 = mock(Empleado)
        emp2 = mock(Empleado)
        emp3 = mock(Empleado)
        # Mock method calls
        when(emp1).get_salario().thenReturn(4000)
        when(emp2).get_salario().thenReturn(4000)
        when(emp3).get_salario().thenReturn(4000)
        res.intro_empleado(emp1)
        res.intro_empleado(emp2)
        res.intro_empleado(emp3)
        print(res.get_salario_total())
        print(res.get_salario_total_mensual())
        self.assertNotEqual(res, 1000)