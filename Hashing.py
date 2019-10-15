from data import Data


class Hashing:

    def __init__(self, data, minHeap):
        self.data = data
        self.size = len(data)  # tamanho da tabela
        self.table = [[False, None, None, None] for i in range(self.size)]
        self.minHeap = minHeap

    def CreateKey(self, word):
        chave = 0
        for i in range(0, len(word)):
            chave += ord(word[i])

        for i in range(0, len(self.table)):
            if chave == self.table[i][2]:
                chave = chave + 1

        return chave

    def Insert(self):
        i = 0
        key = 0
        for word in self.data:
            iteration = 0
            h = (key + iteration) % self.size

            while self.table[h][0] == True:
                iteration = iteration + 1
                h = (key + iteration) % self.size

            if iteration < self.size:
                self.table[h][0] = True
                self.table[h][1] = word.get_Key()
                self.table[h][2] = key
                self.table[h][3] = self.minHeap[i]
                self.data[i].setPrimaryKey(key)
                i = i + 1
            key = key + 1

    def Query(self, key):
        iteration = 0
        h = (key + iteration) % self.size

        while self.table[h][2] != key and iteration < self.size:
            iteration = iteration + 1
            h = (key + iteration) % self.size

        if iteration < self.size:
            return self.table[h][1]
        else:
            return -1

    def HashKeys(self):
        keys = []
        for i in range(0, self.size):
            keys.append([self.table[i][2], self.table[i][3]])
        return keys
