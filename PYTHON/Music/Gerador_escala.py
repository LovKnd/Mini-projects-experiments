global notas_all
# A# == Bb and so on
notas_all = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']


# replaces notes such as 'C' and 'C#' for 'C' and 'Db'
def overriding_notas(escala):
    for i in escala:
        if i[0] == escala[escala.index(i) - 1][0]:
            if notas_all.index(i) + 1 == len(notas_all):
                escala[escala.index(i)] = notas_all[0] + 'b'
            else:
                escala[escala.index(i)] = notas_all[notas_all.index(i) + 1] + 'b'
    return escala


# If have a 'flat' as input
def except_fundametal(nota):
    if nota in notas_all:
        return nota
    else:
        return notas_all[notas_all.index(nota[0][0]) - 1]


def maker_escala(nota, escala_n):
    nota = except_fundametal(nota)
    escala = []
    i = notas_all.index(nota)
    n = 0

    # Append the fundamental note
    escala.append(notas_all[i])

    # Append the others notes
    while n < len(escala_n):
        i += escala_n[n]
        # Make sure the next range of notes is not off the list (notas_all)
        if i >= len(notas_all):
            i -= len(notas_all)

            if i >= len(notas_all):
                while i >= len(notas_all):
                    i -= len(notas_all)

        escala.append(notas_all[i])
        n += 1

    escala = overriding_notas(escala)
    return escala


# escala_n defines to sequence of semitones of a scale
def escala_m(nota):
    escala_n = [2, 1, 2, 2, 1, 2]
    return maker_escala(nota, escala_n)


def escala_M(nota):
    escala_n = [2, 2, 1, 2, 2, 2]
    return maker_escala(nota, escala_n)
