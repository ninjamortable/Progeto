from reservas import Reserva
from horario import Horario
class Salas:
    def __init__(self):
        self.salas = []
        for i in range(4):
            self.salas.append([])
    
    def reserva(self, sala, horario, socio):
        if len(self.salas[sala]) == 0:
            for h in range(len(self.salas)):
                    for j in self.salas[h]:
                        if j.comparar(horario):
                            if j.socio == socio:
                                print(f'Socio ja tem reserva na Sala{h} neste mesmo horario')
                                return
                            else:
                                break
            self.salas[sala].append(Reserva(horario, socio))
            return
            

        for i in range(len(self.salas[sala])):
            if self.salas[sala][i].comparar(horario):
                for h in range(len(self.salas)):
                    for j in self.salas[h]:
                        if j.comparar(horario):
                            if j.socio == socio:
                                print(f'Socio ja tem reserva na Sala{h} neste mesmo horario')
                                return
                            else:
                                break
                self.salas[sala].append(Reserva(horario, socio))
            else:
                print('Horario Indisponivel')

    def removerAllReservaSocio(self, socio):
        for i in range(len(self.salas)):
            for j in range(len(self.salas[i])):
                if self.salas[i][j].socio == socio:
                    self.salas[i].pop(j)

    def getAllReservas(self): 
        for i in range(len(self.salas)):
            print(f'sala {i+1}:')
            if len(self.salas[i]) == 0:
                print(f'    não tem reservas')
            else:
                for j in self.salas[i]:
                    print(j.imprimir())

    def getAllReservasSocio(self, socio):
        print(f'Reservas de {socio}: ')
        for i in range(len(self.salas)):
            for j in self.salas[i]:
                if j.socio == socio:
                    print(f'    sala {i+1}: {j.imprimir()}')
                
    def getAllReservasSocioDia(self, socio, horario):
        print(f'Reservas de {socio} no dia {horario.dia} de {horario.mes}: ')
        for i in range(len(self.salas)):
            for j in self.salas[i]:
                if j.socio == socio and horario.compararDiaMesANo(j.horario):
                    print(f'    sala {i+1}: {j.imprimir()}')

    def trocarNomeSocio(self, sala, horario, novoNome):
        for i in self.salas[sala]:
            if i.comparar(horario):
                i.socio = novoNome
            

    def trocarHorario(self, sala, horario, novoHorario):
        for i in self.salas[sala]:
            if i.comparar(novoHorario):
                print('horario indisponivel')
                return 
        for i in self.salas[sala]:
            if i.comparar(horario):
                i.horario = novoHorario
                return
        print('Horario Não Encontrado')

    def adicionarSalas(self):
        self.salas.append([])
