import nBandit
import numpy as np

class softmax:

    def __init__(self, bandit, temp):
        self.setBandit(bandit)
        self.temp = temp

    def setBandit(self, bandit):
        default_reward = 0
        self.bandit = bandit
        self.sums = [] # Sum of all rewards for each action
        self.counts = [] # Count of rewards for each action
        for i in range(bandit.n):
            self.sums.append( default_reward )
            self.counts.append( 0 )

    def choose(self):
        exps = []
        for i in range(self.bandit.n):
            if self.counts[i] is not 0:
                r = self.sums[i] / self.counts[i]
            else:
                r = self.sums[i]
            exps.append( np.exp( r / self.temp ) )
        denom = np.sum( exps )
        exps = [a / denom for a in exps]
        accum = 0
        ch = np.random.random()
        for i in range(len(exps)):
            accum += exps[i]
            if ch < accum:
                return i
        print "Error"
        return self.bandit.n - 1

    def update(self, a, r):
        self.sums[a] += r
        self.counts[a] += 1

    def play(self):
        a = self.choose()
        r = self.bandit.value(a)
        self.update(a,r)
        return (a,r)

    def label(self):
        return "t = {:0.2f}".format(self.temp)

    def __str__(self):
        r = '['
        for i in range(self.bandit.n):
            r += "{:0.4f}/{} ".format(self.sums[i],self.counts[i])
        r += ']'
        return "%s %d armed bandit: %s" % (self.label(),self.bandit.n, r)

if __name__ == "__main__":
    b = nBandit.nBandit(10)
    g = softmax(b,1.5)
    for p in range(100):
        g.play()
    print b
    print g
