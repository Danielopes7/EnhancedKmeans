import heapq
"""
IMPLEMENTAÇÕES BÁSICAS PARA O FUNCIONAMENTO DO ALGORITMO:

    1 - Essa é a interface da árvore que você irá implementar, ou seja um nó sempre terá um minHeap
    como atributo e os métodos minHeapPop/ minHeapAtt
    
    2 - o insert da árvore receberá 2 parâmetros sendo que o que você vai usar como valor na árvore 
    é o key
    
    3 - é preciso ter um método search que retorna o nó procurado
    
    embaixo está uma árvore rubro negra ainda não implementada, mas com o essencial para o funcinamento
    do algoritmo Kmeans
"""
class Node:

    RED = True
    BLACK = False

    def __init__(self, value, minHeap, color=RED):
        self.color = color
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.minHeap = minHeap

    def MinHeapPop(self):
        return self.minHeap[0][1]

    def MinHeapAtt(self, new):
        self.minHeap = new


class RedBlackTree:
    """ Implementation of Red Black Tree """

    def __init__(self):
        self.root = None

    def search(self, value):
        """ return a Node with given value """

    def insert(self, key, minHeap):
        heapq.heapify(minHeap)
        node = Node(key, minHeap)

