import nBandit
import numpy as np

class greedy:

    def __init__(self, bandit):
        self.setBandit(bandit)

    def setBandit(self,bandit):
        default_reward = 0
        self.bandit = bandit
        self.sums = [] # Sum of all rewards for each action
        self.counts = [] # Count of rewards for each action
        for i in range(bandit.n):
            self.sums.append( default_reward )
            self.counts.append( 0 )

    def estimate(self):
        max_r = -10000
        max_a = None
        for i in range(self.bandit.n):
            if self.counts[i] is not 0:
                r = self.sums[i] / self.counts[i]
            else:
                r = self.sums[i]
            if r > max_r:
                max_r = r
                max_a = i
        return max_a

    def update(self, a, r):
        self.sums[a] += r
        self.counts[a] += 1

    def play(self):
        a = self.estimate()
        r = self.bandit.value(a)
        self.update(a,r)
        return (a,r)

    def label(self):
        return 'greedy'

    def __str__(self):
        r = '['
        for i in range(self.bandit.n):
            r += "{:0.4f}/{} ".format(self.sums[i],self.counts[i])
        r += ']'
        return "%s %d armed bandit: %s" % (self.label(), self.bandit.n, r)

if __name__ == "__main__":
    b = nBandit.nBandit(10)
    g = greedy(b)
    for p in range(100):
        g.play()
    print b
    print g
