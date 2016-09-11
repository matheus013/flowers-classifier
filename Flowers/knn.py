# coding=utf-8
import json
import math
import random
import copy

mark = []
no_mark = []


def normalize(base):
    for i in base:
        if i[4] == 'I. setosa':
            i[4] = 1
        elif i[4] == 'I. virginica':
            i[4] = 2
        elif i[4] == 'I. versicolor':
            i[4] = 3


# calcula distancia
def dist(a, b):
    aux = 0
    for i in range(0, 4):
        aux += (a[i] - b[i]) ** 2
    # print math.sqrt(aux)

    return math.sqrt(aux)


# gera lista de treino
def training_base(base):
    trained = []
    while len(trained) < 0.75 * len(base):
        aux = random.randint(0, len(base) - 1)
        if aux in mark:
            continue
        mark.append(aux)
        trained.append(base[aux])
    return trained


# busca k mais proximos
def get_best(k, base):
    top = []
    base.sort()
    for i in range(0, k):
        top.append(base[i])
    return top


# votação
def voting(top):
    ranking = [0, 0, 0]
    for i in top:
        ranking[i[1][4] - 1] += 1
    # print ranking
    return ranking


# retorna tipo mais votado
def bigger(vote):
    big = 0
    for i in range(0, 3):
        if vote[i] > big:
            big = i + 1
    return big


def knn(k, item, base):
    dists = []
    # gera n tuple distancia e node
    for j in base:
        dists.append((dist(item, j), copy.deepcopy(j)))
    vote = voting(get_best(k, copy.deepcopy(dists)))
    return bigger(vote)


# gera uma lista para avaliação
def available(base):
    for i in range(0, 150):
        if i not in mark:
            no_mark.append(i)


if __name__ == '__main__':
    result = [0, 0]
    base = json.loads(file("flowers.json").read())
    normalize(base)
    table = training_base(copy.deepcopy(base))
    available(base)
    # print no_mark
    for i in no_mark:
        if base[i][4] == knn(11, base[i], table):
            result[0] += 1
        else:
            result[1] += 1
    print result[0] / float(len(no_mark))
