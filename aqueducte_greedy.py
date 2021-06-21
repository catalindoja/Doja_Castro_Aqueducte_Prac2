#!/usr/bin/env python3
'''Practica Aqueducte 1. David Castro i Catalin Doja'''
# encoding: utf-8
from __future__ import print_function

import aux_functions



def greedy(data_x, data_y, data_header, pos):
    '''Algorisme recursiu que implementa greedy'''
    index_cost_mes_baix = pos
    cost_mes_baix = 0
    if pos == len(data_x)-1:
        return 0
    for index, _ in enumerate(data_x):
        # Si index > pos sabem que son els fills que s'han de visitar al arbre.
        if index > pos:
            # Realitzem les comprovacions de x i y
            if aux_functions.checks(data_x, data_y, data_header, pos, index, 1) is False:
                cost_x = abs(data_x[pos] - data_x[index])
                cost_y = (int(data_header[1]) - data_y[index])
                cost_punt = int(data_header[3]) * cost_x * cost_x + cost_y * int(data_header[2])
                if cost_mes_baix > cost_punt or cost_mes_baix == 0:
                    cost_mes_baix = cost_punt
                    index_cost_mes_baix = index
    cost_primera_columna = 0
    # si es la primera posicio calculem adicionalment la primera columna
    if pos == 0:
        cost_y = (int(data_header[1]) - data_y[pos])
        cost_primera_columna = cost_y * int(data_header[2])
    # si no hi ha hagut cap resultat es impossible.
    if cost_mes_baix == 0 or index_cost_mes_baix == pos:
        return None
    # crida recursiva del greedy donant-li el index del cost mes baix
    greedy_temp = greedy(data_x, data_y, data_header, index_cost_mes_baix)

    if greedy_temp is None or cost_mes_baix == 0:
        return None
    result = cost_primera_columna + greedy_temp
    return cost_mes_baix+result


if __name__ == "__main__":
    DATA_HEADER = []
    DATA_X = []
    DATA_Y = []
    aux_functions.load_file(DATA_HEADER, DATA_X, DATA_Y)
    TEMP = greedy(DATA_X, DATA_Y, DATA_HEADER, 0)
    if TEMP is None:
        print("impossible")
    else:
        print(TEMP)
