class Horario:
    def __init__(self, hora = None, dia, mes, ano):
        self.hora = hora
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def returnHorario(self):
        return str(self.hora)+' - '+str(self.dia)+'dia '+str(self.mes)+'mês '+str(self.ano)+'Ano'
    
    def comparar(self, horario):
        if self.ano == horario.ano:
            if self.mes == horario.mes:
                if self.dia == horario.dia:
                    if self.hora == horario.hora:
                        return True
        return False

    def compararDiaMesANo(self, horario):
        if self.ano == horario.ano:
            if self.mes == horario.mes:
                    if self.dia == horario.dia:
                        return True
        return False
