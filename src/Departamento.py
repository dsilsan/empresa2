__author__ = 'David'


class Departamento():
    """
    clase Departamento

    """
    def __init__(self, nombre_depto, id_depto):
        """
        constructor de la clase

        :param nombre_depto: nombre del departamento
        :param id_depto: identificador del departamento
        :return:
        """
        self.nomDpt = nombre_depto
        self.idDpt = id_depto
        self.lEmpleados = []

    def intro_empleado(self, Emp):
        """
        inserta un empleado a la lista de empleados del departamento

        :param Emp: empleado nuevo
        :return:
        """
        self.lEmpleados.append(Emp)

    def get_nombre_dpto(self):
        return self.nomDpt

    def get_salario_total_mensual(self):
        """
        salario total del departamento por meses

        :return: devuelve el salario mensual del departamento
        """
        total = 0
        for emp in self.lEmpleados:
            total += emp.get_salario()
        return total/12

    def get_salario_total(self):
        """
        salario total del departamento

        :return: devuelve el salario total anual del departamento
        """
        total = 0
        for emp in self.lEmpleados:
            total += emp.get_salario()
        return total
