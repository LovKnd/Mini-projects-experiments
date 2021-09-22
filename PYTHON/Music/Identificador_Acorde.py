import Gerador_escala as ge

notas_all = ge.notas_all


def complemento(notas, acorde):
    return acorde


def maior_menor(notas, acorde):
    return acorde


def main(notas, enarmonics=False):
    for i in notas:
        notas[notas.index(i)] = ge.except_fundametal(i)

    acorde = []
    acorde = check_attributes(notas, acorde, enarmonics)

    return acorde


class check_attributes:
    def __init__(self, notas, acorde, enarmonics):
        if enarmonics == True:
            for i in enarmonics(notas, acorde):
                acorde.append(i)
            return acorde
        else:
            return maior_menor(notas, acorde)

    def enarmonics(self, notas, acorde):
        cont = 0
        while cont < len(notas):
            yield maior_menor(notas, acorde)
            cont += 1
            notas = notas[1:] + notas[:1]
