#!/usr/bin/python3
import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy


def my_matrix_generator():  # generowaine losowej (symetrycznej) macierzy natężeń
    tab = [[random.randint(1, matrix_max) for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                tab[i][j] = 0
    # for i in range(n):   #fragment odpowiedzailny za symetrię
    #   for j in range(n):
    #      tab[i][j] = tab[j][i]
    return tab


def find_path(graph, attrs, start, end):  # generowanie grafu, szukanie najkrótrzej scieżki
    s_path = None
    G = nx.Graph()
    G.add_edges_from(graph)
    nx.set_edge_attributes(G, attrs)
    try:
        s_path = nx.shortest_path(G, start, end)
    except Exception as e:
        print(e)
    return s_path


def draw_my_graph(graph):  # rysowanie głównego grafu
    MG = nx.Graph()
    MG.add_edges_from(graph)
    pos = nx.spring_layout(MG)
    nx.draw_networkx(MG, pos, node_color='red')
    plt.show()


def a_func_generator(matrix, graph, nodes):
    a_list = []
    for x in range(len(list(graph.keys()))):
        a = a_func(x, matrix, graph, nodes)
        a_list.append(a)
        print("a(", x + 1, ") = ", a)
        print("-----------")
    return a_list


def a_func(e, matrix, graph, nodes):  # tworzenie funkcji a(e)
    print(e + 1)
    suma = 0
    for i in range(n):
        for j in range(i, n):
            if i != j:
                my_path = find_path(graph_edges, graph1, nodes[i], nodes[j])
                if my_path is not None:
                    if list(graph.keys())[e][0] in my_path and list(graph.keys())[e][1] in my_path:
                        # print(my_path)
                        suma += matrix[i][j]
                else:
                    print("brak ścieżki z ", nodes[i], "do", nodes[j])
                    return 0
    return suma


def count_matrix(tab):  # obliczanie G_sum
    suma = 0
    for i in range(n):
        for j in range(n):
            suma += tab[i][j]
    return suma


def count_T(matrix, graph, m, a_list):  # obliczanie wartości T
    my_sum = 0
    g = count_matrix(matrix)
    for x in range(len(graph)):
        my_sum += (a_list[x] / ((war / m) - a_list[x]))
    return (1 / g) * my_sum


def action(tested_graph):  # funkcja, w której dokonuje się próbkowanie mojej sieci (MonteCarlo)
    edges_list = []
    for key in tested_graph.keys():
        edges_list.append(key)
    for x in range(len(tested_graph)):
        if 0 == numpy.random.choice(a=(0, 1), p=[1 - prob, prob]):
            del tested_graph[edges_list[x]]
    print(tested_graph)
    # draw_my_graph(tested_graph)
    return tested_graph


if __name__ == "__main__":

    n = 20
    matrix_max = 9

    print("macierz natęzeń: ")
    matrix = my_matrix_generator()
    for record in matrix:
        print(record)

    m = 1
    prob = 0.9
    G_sum = count_matrix(matrix)
    war = 8 * n * matrix_max
    t_max = 0.009
    repeats = 100

    t_sum = 0
    t_error = 0
    effective = 0
    nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't']

    graph = {('a', 'b'): {1: war},
             ('a', 'e'): {2: war},
             ('b', 'f'): {3: war},
             ('e', 'f'): {4: war},
             ('d', 'e'): {5: war},
             ('c', 'd'): {6: war},
             ('f', 'g'): {7: war},
             ('g', 'h'): {8: war},
             ('c', 'i'): {9: war},
             ('i', 'j'): {10: war},
             ('d', 'j'): {11: war},
             ('h', 'l'): {12: war},
             ('g', 'k'): {13: war},
             ('k', 'l'): {14: war},
             ('j', 'm'): {15: war},
             ('k', 'p'): {16: war},
             ('m', 'q'): {17: war},
             ('m', 'n'): {18: war},
             ('n', 'r'): {19: war},
             ('q', 'r'): {20: war},
             ('n', 'o'): {21: war},
             ('o', 'p'): {22: war},
             ('o', 's'): {23: war},
             ('s', 't'): {24: war},
             ('d', 'p'): {25: war},
             ('f', 'n'): {26: war},
             ('g', 'm'): {27: war},
             ('j', 'k'): {28: war},
             ('t', 'p'): {29: war},
             ('i', 'd'): {30: war},
             ('k', 'h'): {31: war},
             ('e', 'b'): {32: war},
             ('q', 'n'): {33: war},
             ('s', 'p'): {34: war},
             ('c', 'j'): {35: war},
             ('g', 'l'): {36: war},
             ('a', 'f'): {37: war},
             ('m', 'r'): {38: war},
             ('o', 't'): {39: war},
             ('t', 'q'): {40: war},
             ('a', 'l'): {41: war},
             ('i', 'b'): {42: war},
             ('t', 'c'): {43: war},
             ('h', 'q'): {44: war}
             }

    draw_my_graph(graph)

    for i in range(repeats):

        gr = {('a', 'b'): {1: war},
              ('a', 'e'): {2: war},
              ('b', 'f'): {3: war},
              ('e', 'f'): {4: war},
              ('d', 'e'): {5: war},
              ('c', 'd'): {6: war},
              ('f', 'g'): {7: war},
              ('g', 'h'): {8: war},
              ('c', 'i'): {9: war},
              ('i', 'j'): {10: war},
              ('d', 'j'): {11: war},
              ('h', 'l'): {12: war},
              ('g', 'k'): {13: war},
              ('k', 'l'): {14: war},
              ('j', 'm'): {15: war},
              ('k', 'p'): {16: war},
              ('m', 'q'): {17: war},
              ('m', 'n'): {18: war},
              ('n', 'r'): {19: war},
              ('q', 'r'): {20: war},
              ('n', 'o'): {21: war},
              ('o', 'p'): {22: war},
              ('o', 's'): {23: war},
              ('s', 't'): {24: war},
              ('d', 'p'): {25: war},
              ('f', 'n'): {26: war},
              ('g', 'm'): {27: war},
              ('j', 'k'): {28: war},
              ('t', 'p'): {29: war},
              ('i', 'd'): {30: war},
              ('k', 'h'): {31: war},
              ('e', 'b'): {32: war},
              ('q', 'n'): {33: war},
              ('s', 'p'): {34: war}
              }

        graph1 = action(gr)
        print("-----------")
        graph_edges = list(graph1.keys())
        print("Generowanie funkcji a(e): ")
        a_list = a_func_generator(matrix, graph1, nodes)
        print(a_list)
        t = count_T(matrix, graph1, m, a_list)
        print("moje T jest równe: ", t)
        t_sum += t
        if t >= t_max:
            t_error += 1
        if t != 0 and t < t_max:
            effective += 1
    print("-------------")
    print("PODSUMOWANIE")
    print("wielkość macierzy natężeń = ", n, " , T_max = ", t_max, " , wytrzymałość krawędzi: ",
          prob * 100, "% ,\n m = ", m, " , maksymalna wartość w macierzy ntężeń: ", matrix_max,
          " ,przepustowość krawędzi = ", war)
    print("liczba powodzeń: ", effective, " na: ", repeats, " powtórzeń")
    print("T errors: ", t_error)
    print("średnie t: ", t_sum / repeats)
    print("liczba zepsutych grafów: ", repeats - effective - t_error)
    print("skuteczność sieci to: ", (effective / repeats) * 100, "%")

