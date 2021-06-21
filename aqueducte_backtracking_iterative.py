#!/usr/bin/env python3
'''Practica Aqueducte 2. David Castro i Catalin Doja'''
# encoding: utf-8
from __future__ import print_function
import aux_functions


def backtrack_iterative(data_x, data_y, data_header):
    '''Algorisme itratiu backtracking. Imlpementa una pila que passa per diferents estats
       de forma que aconseguim la mateixa pila que el algorisme recursiu'''
    stack = []
    stack.append(aux_functions.Contextv2(0, 0, "call", len(data_x) - 1, 1))
    top = 0
    temp_cost = 0
    while stack:
        top = stack[-1]
        if top.entry == "call":
            # Si es el cas simple, retornem directament la columna anterior
            if top.pos == len(data_x) - 1:

                temp_cost = int(data_header[2]) * (int(data_header[1]) - data_y[top.pos])
                stack.pop()
            else:
                # Si no es el cas simple, el marquem com a resume (Fara els calculs) i creem la trucada del seguent
                top.entry = "resume"
                stack.append(aux_functions.Contextv2(top.pos + 1, 0, "call", (len(data_x) - 1) - (top.pos + 1), top.pos + 2))
        elif top.entry == "resume":
            # Realitzem les comprobacions (Si la trucada anterior es nula, comprobacions de x i y...)
            top.impossibles[top.next - (top.pos + 1)] = \
                aux_functions.checks(data_x, data_y, data_header, top.pos, top.next, temp_cost)
            if top.impossibles[top.next - (top.pos + 1)] is False:
                # El resultat el guardem amb una variable, que servira com el resultat de la crida anterior
                temp_cost = aux_functions.calcul_total(data_x, data_y, data_header, top.pos, top.next, temp_cost)
                if temp_cost < top.cost or top.cost == 0:
                    top.cost = temp_cost
            # Si li queden mes fills, realitzem una crida recursiva adicional fins que no li queden
            if top.children > 1:
                top.children -= 1
                stack.append(aux_functions.Contextv2(top.next + 1, 0, "call", (len(data_x) - 1) - (top.next + 1), top.next + 2))
                top.next += 1
            else:
                # Al no tindre mes fills, el cost sera el mes petit de totes les possibles opcions
                temp_cost = top.cost
                stack.pop()

    return top.cost




if __name__ == "__main__":
    DATA_HEADER = []
    DATA_X = []
    DATA_Y = []

    aux_functions.load_file(DATA_HEADER, DATA_X, DATA_Y)
    TEMP = backtrack_iterative(DATA_X, DATA_Y, DATA_HEADER)
    # print(TEMP)
    if TEMP is None or TEMP == 0:
        print("impossible")
    else:
        print(TEMP)
