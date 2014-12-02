__author__ = 'David'

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
