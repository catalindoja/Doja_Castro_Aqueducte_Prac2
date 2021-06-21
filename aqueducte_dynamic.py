#!/usr/bin/env python3
'''Practica Aqueducte 2. David Castro i Catalin Doja'''
# encoding: utf-8
from __future__ import print_function
import aux_functions


def dynamic(data_x, data_y, data_header, pos, results):
    '''Funcio que fa el backtrack'''
    minimum = 0
    impossibles = [False] * (len(data_x) - (pos + 1))

    # cas simple que retorna el cost del pilar
    if pos == len(data_x) - 1:
        return int(data_header[2]) * (int(data_header[1]) - data_y[pos])

    # bucle per tractar els calculs del aqueducte.
    for index, _ in enumerate(data_x):
        if pos < index:
            # crida recursiva per fer el backtrack
            if results[pos][index] != 0:#Si existex el resultat, ens ahorrem la trucada
                temp = results[pos][index]
            else:
                temp = dynamic(data_x, data_y, data_header, index, results)
                results[pos][index] = temp #Guardem el resultat
            #Fem les comprobacions (Si la trucada anterior es nula, si se pot per x i y...)
            impossibles[index - (pos + 1)] = aux_functions.checks(data_x, data_y, data_header, pos, index, temp)

            # calculs de costos minims en cas de que hi han cassos possibles.
            if not impossibles[index - (pos+1)]:
                total = aux_functions.calcul_total(data_x, data_y, data_header, pos, index, temp)
                if total < minimum or minimum == 0:
                    minimum = total
    # si existeix algun cas possible retornem el cost minim, en cas contrari retornem None
    for value in impossibles:
        if value != True:
            return minimum
    return None


if __name__ == "__main__":
    DATA_HEADER = []
    DATA_X = []
    DATA_Y = []
    aux_functions.load_file(DATA_HEADER, DATA_X, DATA_Y)

    # comprovacio abans de crear el array bidimnesional de resultats
    if len(DATA_X) != len(DATA_Y):
        print("impossible")
        exit(-1)

    # creaccio del array bidimensional de resultats.
    ROWS, COLS = (len(DATA_X), len(DATA_X))
    RESULTS = []
    for fila in range(ROWS):
        col = []
        for columna in range(COLS):
            col.append(0)
        RESULTS.append(col)
    TEMP = dynamic(DATA_X, DATA_Y, DATA_HEADER, 0, RESULTS)

    if TEMP is None:
        print("impossible")
    else:
        print(TEMP)
