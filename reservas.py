from horario import Horario
class Reserva(Horario):
    def __init__(self, horario, socio):
        self.horario = horario
        self.socio = socio

    def comparar(self, horario):
        return self.horario.comparar(horario) 
    
    def imprimir(self):
        return (f'{self.horario.returnHorario()} - {self.socio}')