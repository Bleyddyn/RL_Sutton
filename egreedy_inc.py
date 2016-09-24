import nBandit
import numpy as np

class egreedy_inc:

    def __init__(self, bandit, e, step_size=0):
        self.setBandit(bandit)
        self.e = e
        self.step_size = step_size

    def setBandit(self, bandit):
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
            if self.step_size > 0 and self.step_size <= 1.0:
                step = self.step_size
            else:
                step = (1 / (self.counts[i] + 1) )
            new_estimate = self.old_estimates[i] + (step * (self.bandit.value(i) - self.old_estimates[i]) )
            if new_estimate > max_r:
                max_r = new_estimate
                max_a = i
        return (max_a,max_r)

    def update(self, a, r):
        self.old_estimates[a] = r
        self.counts[a] += 1

    def play(self):
        if np.random.random() < self.e:
            a = np.random.randint(0,self.bandit.n)
            est = self.old_estimates[a] + ((1 / (self.counts[a] + 1) ) * (self.bandit.value(a) - self.old_estimates[a]) )
        else:
            (a,est) = self.estimate()
        r = self.bandit.value(a)
        self.update(a,est)
        return (a,r)

    def label(self):
        if self.step_size > 0 and self.step_size <= 1.0:
            return "e = {:0.2f}, a = {:0.2f}".format(self.e, self.step_size)
        else:
            return "e = {:0.2f}".format(self.e)

    def __str__(self):
        r = '['
        for i in range(self.bandit.n):
            r += "{:0.4f}/{} ".format(self.old_estimates[i],self.counts[i])
        r += ']'
        return "%s %d armed bandit: %s" % (self.label(),self.bandit.n, r)

if __name__ == "__main__":
    b = nBandit.nBandit(10)
    g = egreedy_inc(b,0.1)
    g2 = egreedy_inc(b,0.1,step_size=0.1)
    for p in range(1000):
        g.play()
        g2.play()
    print b
    print g
    print g2
