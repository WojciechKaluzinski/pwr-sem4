#!/usr/bin/python3
import numpy as np
import csv
import operator


def get_x(m_func):
    n_func = 0
    for lines in open('ml-latest-small/ratings.csv'):
        try:
            if (int(lines.split(',')[
                        0]) > n_func):
                n_func = int(lines.split(',')[0])
        except:
            print("", end="")

    results = []
    for j_func in range(n_func):
        results.append([])
        for i_func in range(m_func + 1):
            results[j_func].append(0)

    for lines in open('ml-latest-small/ratings.csv'):
        try:
            if int(lines.split(',')[1]) <= m_func:
                results[
                    int(lines.split(',')[0])
                ][
                    int(lines.split(',')[1])
                ] = float(lines.split(',')[2])
        except:
            print("", end="")

    x_matrix = np.array(results, float)

    return x_matrix


if __name__ == "__main__":
    persons = []
    with open("ml-latest-small/ratings.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == '1':
                persons.append(int(row[0]))

    n = 0
    for line in open("ml-latest-small/movies.csv"):
        try:
            if int(line.split(',')[0]) > n:
                n = int(line.split(',')[0])
        except:
            print("", end="")

    movies = []
    for j in range(n):
        movies.append("NULL")

    for line in open("ml-latest-small/movies.csv"):
        try:
            tmp = line.split(',', 1)[1:]
            tmp = tmp[0][::-1]
            tmp = tmp.split(',', 1)[1:]
            tmp = tmp[0][::-1]
            movies[int(line.split(',')[0])] = tmp
        except:
            print("", end="")

    m = 10000
    x = get_x(m)
    my_ratings = np.zeros((m + 1, 1))
    my_ratings[2571] = 5
    my_ratings[32] = 4
    my_ratings[260] = 5
    my_ratings[1097] = 4

    y = my_ratings

    np.linalg.norm(x, axis=0)
    z = np.dot(np.nan_to_num(x / np.linalg.norm(x, axis=0)),
               np.nan_to_num(np.array(y) / np.linalg.norm(y)))
    X = np.nan_to_num(x / np.linalg.norm(x, axis=0))
    Z = np.nan_to_num(z / np.linalg.norm(z))

    result_dic = {}
    result = np.dot(X.T, Z)
    for b in range(len(result)):
        result_dic[b] = result[b]

    sort = sorted(result_dic.items(), key=operator.itemgetter(1), reverse=True)
    for i in range(len(sort)):
        try:
            if movies[sort[i][0]] != "NULL":
                print(sort[i], movies[sort[i][0]])
        except:
            print("a", end="")
