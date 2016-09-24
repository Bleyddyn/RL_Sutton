import nBandit
import numpy as np

class greedy_inc:

    def __init__(self, bandit):
        self.setBandit(bandit)

    def setBandit(self,bandit):
        default_reward = 0
        self.bandit = bandit
        self.old_estimates = [] # Sum of all rewards for each action
        self.counts = [] # Count of rewards for each action
        for i in range(bandit.n):
            self.old_estimates.append( default_reward )
            self.counts.append( 0 )

    def estimate(self):
        max_r = -10000
        max_a = None
        for i in range(self.bandit.n):
            new_estimate = self.old_estimates[i] + ((1 / (self.counts[i] + 1) ) * (self.bandit.value(i) - self.old_estimates[i]) )
            if new_estimate > max_r:
                max_r = new_estimate
                max_a = i
        return (max_a, max_r)

    def update(self, a, r):
        self.old_estimates[a] = r
        self.counts[a] += 1

    def play(self):
        (a, est) = self.estimate()
        r = self.bandit.value(a)
        self.update(a,est)
        return (a,r)

    def label(self):
        return 'greedy (inc)'

    def __str__(self):
        r = '['
        for i in range(self.bandit.n):
            r += "{:0.4f}/{} ".format(self.old_estimates[i],self.counts[i])
        r += ']'
        return "%s %d armed bandit: %s" % (self.label(), self.bandit.n, r)

if __name__ == "__main__":
    b = nBandit.nBandit(10)
    g = greedy_inc(b)
    for p in range(100):
        g.play()
    print b
    print g
