class Data:
    def __init__(self, points, key):
        self.points = points
        self.key = key
        self.centroid = None
        self.PrimaryKey = None

    def setPrimaryKey(self, pk):
        self.PrimaryKey = pk

    def getPrimaryKey(self):
        return self.PrimaryKey

    def get_points(self):
        return self.points[:]

    def get_Key(self):
        return self.key

    def setCentroid(self, distance):
        self.centroid = distance

    def getCentroid(self):
        return self.centroid

    def NameCentroid(self):
        last = len(self.centroid) - 1
        return self.centroid

    def getCentAndPoints(self):
        return self.centroid, self.key
