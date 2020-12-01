class quickfind:
    def __init__(self, N):
        """ initiate list of unconnected nodes """
        self.id = []
        for val in range(N):
            self.id.append(val)

    def find(self, p, q):
        """ check if two nodes are connected """
        return self.id[p] == self.id[q]

    def union(self, p, q):
        """ union two nodes """
        pid = self.id[p]
        qid = self.id[q]
        for val, i in enumerate(self.id):
            if val == pid:
                self.id[i] = qid

    def print(self):
        """ print id list """
        for val in self.id:
            print(val, end=' ')
        print()
        
qf = quickfind(10)

qf.find(0,1) # false
qf.union(0,1) # None
qf.find(0,1) # true

qf.print() # outputs node list id

class quickunion:
    """ initiate list of unconnected nodes """
    def __init__(self, N):
        self.id = []
        for i in range(N):
            self.id.append(i)

    def root(self, i):
        """ utility that returns the root of the component """
        while i != self.id[i]:
            i = self.id[i]
        return i  

    def find(self, p, q):
        """ check if two nodes are connected """ 
        return self.root(p) == self.root(q)

    def union(self, p, q):
        """ union/connect two nodes """
        i = self.root(p)
        j = self.root(q)
        self.id[i] = j 

    def print(self):
        """ print id list """
        for val in self.id:
            print(val, end=' ')
        print()

uf = quickunion(10)

uf.find(0,1) # false
uf.union(0,1) # None
uf.find(0,1) # true

uf.print() # outputs node list id

