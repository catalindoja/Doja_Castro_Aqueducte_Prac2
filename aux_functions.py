import math
import sys


class Contextv2:
    '''Classe que ajuda la pila a canviar de entry points i
     que conte varialbes necessaries per fer el metode iteratiu'''
    def __init__(self, pos, cost, entry, children, next_pos):
        self.pos = pos
        self.cost = cost
        self.entry = entry
        self.children = children
        self.next = next_pos
        self.minimum = 0
        self.impossibles = [False] * children


def load_file(data_header, data_x_arr, data_y_arr):
    '''Carrega de la configuracio'''
    i = 1
    # comprovacio de arguments
    filename = "sample-1.in"

    if len(sys.argv[1]) > 1:
        filename = sys.argv[1]
    else:
        exit(-1)

    # lectura dels parametres del fitxer.
    arxiu = open(filename, "r")
    for line in arxiu:
        if i == 1:
            temp = line.rstrip("\n").split(" ")
            for value in temp:
                data_header.append(value)
            i = i + 1
        else:
            temp = line.rstrip("\n").split(" ")
            data_x_arr.append(int(temp[0]))
            data_y_arr.append(int(temp[1]))


def comprovacions_x(data_x, pos, index, data_header, data_y):
    '''Comprovacio punt per punt en el cas de saltar-nos pilars
    amb aixo podem veure si hi han casos impossibles'''
    position_x = 0
    radi = abs(data_x[pos] - data_x[index])
    radi = radi / 2
    for indexes in data_x:
        if indexes > data_x[pos] and indexes < data_x[index]:
            x_value = abs(abs(radi - data_x[index]) - data_x[position_x])
            x_value = math.sqrt(abs(pow(x_value, 2) - pow(radi, 2)))
            if data_y[position_x] > x_value + (float(data_header[1]) - radi):
                return True
        position_x = position_x + 1
    return False


def comprovacions_y(data_x, data_y, data_header, pos, index):
    '''Comprovacio de la y del arc'''
    radi = abs(data_x[pos] - data_x[index])
    radi = radi / 2
    yarc = int(data_header[1]) - radi

    y_value = math.sqrt(abs(radi * radi - pow((data_x[index] - radi), 2))) + yarc

    if data_y[index] > y_value or y_value < 0 or \
                        float(data_header[1]) < radi + data_y[pos] or \
                        float(data_header[1]) < radi + data_y[index]:
        return True
    return False


def calcul_total(data_x, data_y, data_header, pos, index, temp):
    '''Calcul del total del punt i el calcul temporal anterior'''
    cost_punt = abs(data_x[pos] - data_x[index])
    cost_punt = int(data_header[3]) * cost_punt * cost_punt +\
                (int(data_header[1]) - data_y[pos]) * int(data_header[2])
    total = cost_punt + temp
    return total


def checks(data_x, data_y, data_header, pos, next_pos, temp_cost):
    '''Comprovacio de casos impossibles per tal de popular el array
    de impossibles'''
    if temp_cost == 0 or temp_cost is None:
        return True
    if comprovacions_y(data_x, data_y, data_header, pos, next_pos):
        return True
    if comprovacions_x(data_x, pos, next_pos, data_header, data_y):
        return True
    return False
