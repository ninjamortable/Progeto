from salas import Salas
from horario import Horario
from socio import Socio
def main():
    # Lista Pre-Pronta de socios
    # socios = input('Socios separados por ", ": ').split(', ')
    socios = ['pedro', 'afonso', 'João']
    sociosList = []
    codigo = 0
    salario = 999
    for i in socios:
        codigo += 1
        salario += 1
        sociosList.append(Socio(codigo, i, salario, 25))

    salas = Salas()
    salas.reserva(0, Horario('2:00', 14, 4, 2000), sociosList[0].nome)
    salas.reserva(1, Horario('3:00', 14, 4, 2000), sociosList[0].nome)
    salas.getAllReservas()
    salas.removerAllReservaSocio(sociosList[0].nome)
    salas.getAllReservas()

    salas.reserva(0, Horario('2:00', 14, 4, 2000), sociosList[0].nome)
    salas.reserva(1, Horario('3:00', 14, 4, 2000), sociosList[0].nome)
    salas.getAllReservasSocioDia(sociosList[0].nome, Horario('3:00', 14, 4, 2000))
    salas.trocarNomeSocio(1, Horario('3:00', 14, 4, 2000), sociosList[0].nome)
    salas.getAllReservas()

    salas.trocarHorario(0, Horario('2:00', 14, 4, 2000), Horario("15:00", 30, 2, 2077))
    salas.getAllReservas()
main()