#!/usr/bin/env python3
'''Practica Aqueducte 1. David Castro i Catalin Doja'''
# encoding: utf-8
from __future__ import print_function
import aux_functions


def greedy_iterative(data_x, data_y, data_header):
    '''Algorisme iteratiu que implementa greedy'''
    total = 0
    cost_mes_baix = 0
    index_cost_baix = 0
    for pos, _ in enumerate(data_x):
        pos = index_cost_baix
        for index, _ in enumerate(data_x):
            # Si index > pos sabem que son els fills que s'han de visitar al arbre.
            if index > pos:
                if aux_functions.checks(data_x, data_y, data_header, pos, index, 1) is False:
                    # calculs dels costos.
                    cost_x = abs(data_x[pos] - data_x[index])
                    cost_y = (int(data_header[1]) - data_y[index])
                    cost_punt = int(data_header[3]) * cost_x * cost_x + cost_y * int(data_header[2])
                    # comprovacio cost mes baix
                    if cost_mes_baix > cost_punt or cost_mes_baix == 0:
                        cost_mes_baix = cost_punt
                        index_cost_baix = index
        # suma dels costos i resetejar el cost mes baix per la seguent volta
        if cost_mes_baix == 0 and pos != (len(data_x)-1):
            return None
        total = total + cost_mes_baix
        cost_mes_baix = 0
    cost_y = (int(data_header[1]) - data_y[0])
    cost_primera_columna = cost_y * int(data_header[2])
    total = cost_primera_columna + total
    return total


if __name__ == "__main__":
    DATA_HEADER = []
    DATA_X = []
    DATA_Y = []

    aux_functions.load_file(DATA_HEADER, DATA_X, DATA_Y)

    TEMP = greedy_iterative(DATA_X, DATA_Y, DATA_HEADER)
    if TEMP is None:
        print("impossible")
    else:
        print(TEMP)
