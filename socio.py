from funcionarios import Funcionario
class Socio(Funcionario):
    def __init__(self, codigo, nome, salario, porcentagemEmpresa):
        super().__init__(codigo, nome, salario)
        self.porcentagemEmpresa = porcentagemEmpresa