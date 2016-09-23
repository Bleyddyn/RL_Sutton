import numpy as np

class nBandit:

    def __init__(self, n):
        self.n = n
        self.qstar = [] # True reward
        maxr = -10000
        self.optimal = None
        for i in range(n):
            r = np.random.normal( 0.0, 1.0 ) # Gaussian with mean 0 and variance 1
            self.qstar.append(r)
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
        return "%d armed bandit (%d): %s" % (self.n, self.optimal, r)

if __name__ == "__main__":
    b = nBandit(10)
    print b
