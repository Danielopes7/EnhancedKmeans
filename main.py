from kmeans import Kmeans
from trees import *
import utilities as ut
'''
    instruções do algoritmo em trees.py
'''
csv = ut.OpenCsv('test/wc2018.csv')
size = len(csv[0])
DataSet = ut.CreateDataSet(csv, size)

means = Kmeans(3, DataSet)
means.ChooseCentroids()
minHeaps = means.EuclideanAll()

tree = RedBlackTree() # Escolha qual árvore irá usar

TableHash = ut.TableHashing(DataSet, minHeaps)
ut.InsertTree(TableHash, tree)
means.MediaCentroids()

ut.EnhencedKmeans(means, DataSet, tree)
ut.printKmeans(DataSet, tree, size)

