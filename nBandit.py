import numpy as np

class nBandit:

    def __init__(self, n, walk=False):
        self.n = n
        self.qstar = [] # True reward
        self.optimal = None
        self.walker = walk
        if walk:
            self.qstar = [np.random.normal( 0.0, 1.0 )] * n
            self.optimal = 0
        else:
            maxr = -10000
            for i in range(n):
                r = np.random.normal( 0.0, 1.0 ) # Gaussian with mean 0 and variance 1
                self.qstar.append(r)
                if r > maxr:
                    maxr = r
                    self.optimal = i

    def walk(self):
        if self.walker:
            maxr = -10000
            for i in range(self.n):
                r = np.random.normal( 0.0, 0.1 ) # Gaussian with mean 0 and variance 0.1
                self.qstar[i] += r
                r = self.qstar[i]
                if r > maxr:
                    maxr = r
                    self.optimal = i

    def value(self, a):
        # return a Gaussian value with mean of qstar[a] and variance 1
        return np.random.normal( self.qstar[a], 1.0 )

    def __str__(self):
        r = '['
        for i in self.qstar:
            r += "{0:0.4f} ".format(i)
        r += ']'
        if self.walker:
            return "%d armed bandit walking (%d): %s" % (self.n, self.optimal, r)
        else:
            return "%d armed bandit (%d): %s" % (self.n, self.optimal, r)

if __name__ == "__main__":
    b = nBandit(10)
    print b

    w = nBandit(10, walk=True)
    print w
    print "walking..."
    for i in range(100):
        w.walk()
    print w
