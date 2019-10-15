from Hashing import *
import csv


def OpenCsv(csvArq):
    arquivo = open( csvArq )
    linhas = csv.reader(arquivo)
    aux = []
    for linha in linhas:
        aux.append(linha)

    size = len(aux[0])
    for i in range(1, len(aux)):
        for j in range(0, size - 1):
            aux[i][j] = float(aux[i][j])
    return aux

def CreateDataSet(csv, size):
    DataSet = []
    for i in range(1, len(csv)):
        object = Data(csv[i][:size - 1], csv[i][size - 1])
        DataSet.append(object)
    return DataSet

def TableHashing(DataSet, minHeaps):


    TableHash = Hashing(DataSet, minHeaps)
    TableHash.Insert()
    return TableHash

def InsertTree (TableHash, tree):
    keys = TableHash.HashKeys()  # cada linha [key, minheap]
    for i in keys:
        tree.insert(i[0], i[1])

def EnhancedKmeans (means, DataSet, tree):
    print( "\nEnhencedKmeans Loading...\n")
    while (means.GetStop() != 0):
        means.DirtyNull()
        minHeaps = means.MinHeapAll()
        size = len(DataSet[0].get_points())

        for i in range(0, len(DataSet)):
            node = tree.search(DataSet[i].getPrimaryKey())
            node.MinHeapAtt(minHeaps[i])

        for i in range(0, len(DataSet)):
            node = tree.search(DataSet[i].getPrimaryKey())
            if node.MinHeapPop()[size] != DataSet[i].getCentroid()[size]:
                means.setDirty(node.MinHeapPop()[size], DataSet[i].getCentroid()[size])
                DataSet[i].setCentroid(node.MinHeapPop())

        means.MediaSpecificCentroids(size)
        if means.getDirty().count(1) == 0:
            means.Setstop()

def printKmeans(DataSet, tree, size):
    size = size -1
    for i in range(0, len(DataSet)):
        node = tree.search(DataSet[i].getPrimaryKey())
        print("{} in  Cluster : {} ".format(DataSet[i].get_Key(),
                                                              node.MinHeapPop()[size]))
