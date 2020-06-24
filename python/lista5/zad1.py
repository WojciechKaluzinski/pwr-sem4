#!/usr/bin/python3
import numpy as np
import csv
from sklearn import linear_model
import matplotlib.pyplot as plt


def get_data(users, m_func):
    toy_story_id = 1
    dates = [[0 for _ in range(m_func)] for _ in range(len(users))]
    ts_scores = [0 for _ in range(len(users))]
    lines = None
    with open("ml-latest-small/ratings.csv",
              mode="r", encoding="utf-8") as f:
        lines = f.readlines()
    if lines is not None:
        for line in lines[1:]:
            data = line.rstrip().split(",")
            if int(data[0]) in users and int(data[1]) <= m_func:
                counter = 0
                while users[counter] != int(data[0]):
                    counter += 1
                if int(data[1]) != toy_story_id:
                    dates[counter][int(data[1]) - 2] = float(data[2])
                else:
                    ts_scores[counter] = float(data[2])
    for i in range(len(ts_scores)):
        ts_scores[i] = [ts_scores[i]]
    X_func = np.array(dates, float)
    y_func = np.array(ts_scores, float)

    return X_func, y_func


persons = []
with open('ml-latest-small/ratings.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[1] == '1':
            persons.append(int(row[0]))


def hypothesis_function(L_func, x_func):
    return sum([L_func[i] * x_func[i] for i in range(len(L_func))])


if __name__ == "__main__":
    m = 10
    X, y = get_data(persons, m)

    model = linear_model.LinearRegression()
    model.fit(X, y)
    plt.plot(X, 'ro')
    plt.plot(model.predict(X), 'bo', label="błędy")
    plt.ylabel("ocena")
    plt.xlabel("osoby")
    plt.title("podpunkt 1, m = %i" % m)
    plt.legend()
    plt.show()

    K = []
    L = np.linalg.lstsq(X[:200], y[:200], rcond=None)[0]
    for x in range(200, 215):
        K.append(hypothesis_function(L, X[x]))

    plt.plot(K, 'ro', label='dane przewidziane')
    plt.plot(y[200:], 'bo', label='dane prawidłowe')
    plt.ylabel("oceny")
    plt.xlabel("osoby")
    plt.title("podpunkt 2, m = %i" % m)
    plt.legend()
    plt.show()
