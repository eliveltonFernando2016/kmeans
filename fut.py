import numpy as np
import os
import re
from dsrc import Dsrc
from scipy.spatial import distance
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
import csv

def readFile():
    data = []
    with open("New_100OBU.txt", "r") as f:
        for line in f:
            d1 = re.search("TXnid = (\d+)", line)
            d2 = re.search("RXnid = (\d+)", line)
            d3 = re.search("RSS = ([+-]?\d+\.\d*)", line)
            d4 = re.search("SNR = ([+-]?\d+\.\d*)", line)
            if d1 and d2 and d3 and d4:
                data.append([d1.group(1), d2.group(1), d3.group(1), d4.group(1)])

    originalData = data[:]
    pca = PCA(n_components=2)
    projected = pca.fit_transform(data)
   
    
    with open('data.csv', mode='w') as f:
        writer = csv.DictWriter(f, fieldnames = ['valor1','valor2'], delimiter = ',')
        for i in projected:
            dh = dict(valor1=i[0], valor2=i[1])
            writer.writerow(dh)  

    return projected, originalData

def compute_euclidean_distance(point, centroid):
    return np.sqrt(np.sum((point - centroid)**2))

def assign_label_cluster(distance, data_point, centroids):
    index_of_minimum = min(distance, key=distance.get)
    return [index_of_minimum, data_point, centroids[index_of_minimum]]

def compute_new_centroids(cluster_label, centroids):
    return np.array(cluster_label + centroids)/2

def iterate_k_means(data_points, centroids, total_iteration):
    label = []
    cluster_label = []
    total_points = len(data_points)
    k = len(centroids)
    
    for iteration in range(0, total_iteration):
        for index_point in range(0, total_points):
            distance = {}
            for index_centroid in range(0, k):
                distance[index_centroid] = compute_euclidean_distance(data_points[index_point], centroids[index_centroid])
            label = assign_label_cluster(distance, data_points[index_point], centroids)
            centroids[label[0]] = compute_new_centroids(label[1], centroids[label[0]])

            if iteration == (total_iteration - 1):
                cluster_label.append(label)

    return [cluster_label, centroids]

def print_label_data(result):
    print("Result of k-Means Clustering: \n")
    for data in result[0]:
        print("data point: {}".format(data[1]))
        print("cluster number: {} \n".format(data[0]))
    print("Last centroids position: \n {}".format(result[1]))

def create_centroids(X, Y, k):
    centroids = []
    i = 0
    while i < 4:
        centroids.append([X[i],Y[i]])
        i = i + 1
    return np.array(centroids)

if __name__ == "__main__":
    k = 4
    data, originalData = readFile()
    centroids = np.random.randint(0, len(originalData), size=k)
    centroids_ordenadas = sorted(centroids)
    pontos_reais_centroidsX = []
    pontos_reais_centroidsY = []
    for i in centroids_ordenadas:
        pontos_reais_centroidsX.append(data[0][0])
        pontos_reais_centroidsY.append(data[0][1])

    filename = os.path.dirname(__file__) + "data.csv"
    data_points = np.genfromtxt(filename, delimiter=",")
    centroids = create_centroids(pontos_reais_centroidsX, pontos_reais_centroidsY,k)
    total_iteration = 100
    
    [cluster_label, new_centroids] = iterate_k_means(data_points, centroids, total_iteration)
    print_label_data([cluster_label, new_centroids])
    
    plt.scatter(new_centroids, new_centroids, edgecolor='none', alpha=0.5, cmap=plt.cm.get_cmap('nipy_spectral_r', 10))
    plt.xlabel('Classe A')
    plt.ylabel('Classe B')
    plt.show()
 