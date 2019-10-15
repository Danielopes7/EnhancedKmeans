import random
import math
import heapq


class Kmeans:  # recebe o k numeros de centroides, e data que é um conjunto de dados que serão agrupados
    def __init__(self, k, data):
        self.k = k
        self.data = data
        self.Centroids = None
        self.dirty = [0 for i in range(k)]
        self.stop = 1

    def GetStop(self):
        return self.stop

    def setDirty(self, cluster1, cluster2):
        for i in range(0, len(self.dirty)):
            if i == int(cluster1[1:]) - 1:
                self.dirty[i] = 1
            elif i == int(cluster2[1:]) - 1:
                self.dirty[i] = 1

    def DirtyNull(self):
        self.dirty = [0 for i in range(self.k)]

    def getDirty(self):
        return self.dirty

    def Setstop(self):
        self.stop = 0

    def getCentroidsMeans(self):
        return self.Centroids

    def ChooseCentroids(self):  # funcao para pegar aleatoriamente os primeiros k centroides
        num = 1
        randomCentroids = []
        randomCentroids.append(
            random.choice(self.data))  # adiciono o primeiro objeto que foi escolhido aleatoriamente como centroide
        while (num != self.k):
            aux = random.choice(self.data)
            if (aux not in randomCentroids):  # verifico se o objeto ja foi escolhido
                randomCentroids.append(aux)
                num = num + 1

        for i in range(0, len(randomCentroids)):
            randomCentroids[i] = randomCentroids[i].get_points()

        self.Centroids = randomCentroids
        for i in range(0, len(self.Centroids)):
            self.Centroids[i].append(str('C') + str(i + 1))

        return self.Centroids[:]

    def Euclidean(self, point, centroid):
        soma = 0

        for i in range(len(point)):
            soma += math.pow(point[i] - centroid[i], 2)
        return math.sqrt(soma)

    '''
        de cada objeto pego a distância euclidiana para cada centroide, a menor distância 
        é atribuida como centroide do objeto, ao mesmo tempo pego todos as distâncias para
        todos os centroides e coloco no minheap
        
    '''

    def EuclideanAll(self):
        minHeap = [None for i in range(len(self.data))]  # nessa lista cada posição é como se fosse um min heap
        for i in range(0, len(self.data)):
            aux = (self.Euclidean(self.data[i].get_points(),
                                  self.Centroids[0]))  # primeiro pego a distancia do objeto a um primeiro centroide
            menor = aux
            self.data[i].setCentroid(self.Centroids[0][:])
            minHeap[i] = [[aux, self.Centroids[0][:]]]
            for j in range(1, len(self.Centroids)):
                aux = (self.Euclidean(self.data[i].get_points(), self.Centroids[j]))
                if (aux < menor):  # atualizo em que centroide o objeto esta mais proximo
                    menor = aux
                    self.data[i].setCentroid(self.Centroids[j][:])
                    minHeap[i].append([aux, self.Centroids[j][:]])
                else:
                    minHeap[i].append([aux, self.Centroids[j][:]])
        return minHeap

    def MinHeapAll(self):
        minHeap = [None for i in range(len(self.data))]  # nessa lista cada posição é como se fosse um min heap
        for i in range(0, len(self.data)):
            aux = (self.Euclidean(self.data[i].get_points(),
                                  self.Centroids[0]))
            minHeap[i] = [[aux, self.Centroids[0]]]
            for j in range(1, len(self.Centroids)):
                aux = (self.Euclidean(self.data[i].get_points(), self.Centroids[j]))

                minHeap[i].append([aux, self.Centroids[j]])
            heapq.heapify(minHeap[i])
        return minHeap

    def Media(self, aux, cont):  # cont = quantos elementos estão no grupo
        if cont == 0:
            return aux
        for i in range(0, len(aux)):
            aux[i] = aux[i] / cont

        return aux

    """
        Função que percorre todos os objetos em um grupo para pegar a media dos pontos e atribuir aos pontos do centroide do grupo
    """

    def MediaCentroids(self):
        for i in range(0, len(self.Centroids)):
            aux = [0 for i in range(len(self.Centroids[0]))]  # lista com uma quantidade de pontos
            cont = 0
            for data in self.data:
                if data.getCentroid() == self.Centroids[i]:
                    points = data.get_points()
                    aux = [(a + b) for a, b in zip(aux, points)]
                    cont = cont + 1

            self.Centroids[i][:len(self.Centroids[i]) - 1] = self.Media(aux, cont)

    def MediaSpecificCentroids(self, size):
        for i in range(0, len(self.Centroids)):
            if self.dirty[i] == 1:
                aux = [0 for i in range(len(self.Centroids[0]))]  # lista com uma quantidade de pontos
                cont = 0
                for data in self.data:
                    if data.getCentroid()[size] == self.Centroids[i][size]:
                        points = data.get_points()
                        aux = [(a + b) for a, b in zip(aux, points)]
                        cont = cont + 1

                self.Centroids[i][:len(self.Centroids[i]) - 1] = self.Media(aux, cont)
