#!/usr/bin/env python3
'''Practica Aqueducte 2. David Castro i Catalin Doja'''
# encoding: utf-8
from __future__ import print_function
import aux_functions


def backtrack(data_x, data_y, data_header, pos):
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
            temp = backtrack(data_x, data_y, data_header, index)

            #Fem les comprobacions (Si la trucada anterior es nula, si se pot per x i y...)
            impossibles[index - (pos + 1)] = aux_functions.checks(data_x, data_y, data_header, pos, index, temp)

            # calculs de costos minims en cas de que hi han cassos possibles.
            if impossibles[index - (pos+1)] is False:
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
    TEMP = backtrack(DATA_X, DATA_Y, DATA_HEADER, 0)

    if TEMP is None:
        print("impossible")
    else:
        print(TEMP)
