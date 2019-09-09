import timeit
from random import randint
import matplotlib.pyplot as plt
import sys
from random import shuffle

sys.setrecursionlimit(10 ** 6)


def desenhaGrafico(x, y, xl="Entradas", yl="Saidas", name="out"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(name)


def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista


def gnomeSort(arr):
    n = len(lista)
    index = 0
    while index < n:
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index = index - 1

    return arr


size = [10000, 20000, 40000, 50000, 100000]
time = []

for s in size:
    lista = geraLista(s)

    time.append(timeit.timeit("gnomeSort({})".format(lista),
                              setup="from __main__ import gnomeSort", number=1))
    print(s)

desenhaGrafico(size, time, "Tamanho", "Tempo",
               "gnomeSort.png")