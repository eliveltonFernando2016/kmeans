import re
from dsrc import Dsrc
import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits

def readFile():
    data = []
    with open('/home/elivelton/Downloads/dataset/Normal/1OBU.txt', 'r') as f:
        for line in f:
            d1 = re.search('TXnid = (\d+)', line)
            d2 = re.search('RXnid = (\d+)', line)
            d3 = re.search('RSS = ([+-]?\d+\.\d*)', line)
            d4 = re.search('SNR = ([+-]?\d+\.\d*)', line)
            if d1 and d2 and d3 and d4:
                data.append(Dsrc(d1.group(1), d2.group(1), d3.group(1), d4.group(1)))

    return data

def euclidian(a, b):
    return distance.euclidean(a, b)

def mapeia_aux(prototypes, posicao, listaDistancia):
    cont = 0
    cont2 = 0
    matriz = []
    aux = []

    while cont2 < len(prototypes):
        for i in posicao:
            if cont2 == i[1]:
                aux.append(listaDistancia[i[1]][i[0]])
        matriz.append(aux)
        aux = []
        cont2 += 1

    return matriz

def adicionaZeros(matriz):
    maior = len(max(matriz, key=len))

    for i in matriz:
        cont = 0
        while(cont < maior):
            if(len(i) < maior):
                i.append(0)
            cont += 1

    return matriz

def kmeans(data, k):
    posicoes = np.random.randint(0, len(data), size=k)
    prototypes = []
    for i in posicoes:
        prototypes.append(data[i])

    listaDistancia = []

    for i in prototypes:
        linha = []
        for j in data:
            if(i != j):
                linha.append(euclidian(float(i.snr), float(j.snr)))
        listaDistancia.append(linha)

    matriz = np.array(listaDistancia)
    posicao = [(i, linha.argmin()) for i, linha in enumerate(matriz.T)]

    m = np.array(adicionaZeros(mapeia_aux(prototypes, posicao, listaDistancia)))

    pca = PCA(n_components=2)
    projected = pca.fit_transform(m)

    return projected

def plotarGrafico(listaDistancia, k):
    rng = np.random.RandomState(0)
    colors = rng.rand(k)

    plt.scatter(listaDistancia[:, 0], listaDistancia[:, 1], c=colors, edgecolor='none', alpha=0.5, cmap=plt.cm.get_cmap('nipy_spectral_r', 10))
    plt.xlabel('Componente 1')
    plt.ylabel('Componente 2')
    plt.show()

if __name__ == '__main__':
    data = readFile()
    plotarGrafico(kmeans(data, 10), 10)