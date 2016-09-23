from __future__ import print_function
import nBandit
import greedy
import egreedy
import softmax
import matplotlib.pyplot as plt
import sys

def test( num_tasks, num_plays, arms=10 ):
    pols = []
    b = nBandit.nBandit(arms)
    pols.append( [greedy.greedy(b), [0]*num_plays, [0]*num_plays] )
    pols.append( [egreedy.egreedy(b,0.1), [0]*num_plays, [0]*num_plays] )
    #pols.append( [egreedy.egreedy(b,0.01), [0]*num_plays, [0]*num_plays] )
    pols.append( [softmax.softmax(b,0.1), [0]*num_plays, [0]*num_plays] )
    pols.append( [softmax.softmax(b,0.5), [0]*num_plays, [0]*num_plays] )
    pols.append( [softmax.softmax(b,1.0), [0]*num_plays, [0]*num_plays] )

    for task in range(num_tasks):
        if (task % 100) == 0:
            print( ("%d" % task), end=" " )
            sys.stdout.flush()
        b = nBandit.nBandit(arms)
        for apol in pols:
            apol[0].setBandit(b)
        for play in range(num_plays):
            for apol in pols:
                (a,r) = apol[0].play()
                apol[1][play] += r
                if a is b.optimal:
                    apol[2][play] += 1

    for apol in pols:
        apol[1] = [x / num_tasks for x in apol[1]]
        apol[2] = [ (100 * x) / num_tasks for x in apol[2]]

    print( "\n" )
    return pols

def plot( pols ):
    plt.figure(1,figsize=(16,12))
    plt.subplot(211)
    hdls = []
    for apol in pols:
        line, = plt.plot(apol[1], label=apol[0].label())
        hdls.append(line)

    plt.ylabel('Average reward')
    plt.xlabel('Plays')
    plt.legend(handles=hdls, loc='best')

    plt.subplot(212)
    hdls = []
    for apol in pols:
        line, = plt.plot(apol[2], label=apol[0].label())
        hdls.append(line)
    plt.ylabel('% Optimal action')
    plt.xlabel('Plays')
    plt.legend(handles=hdls, loc='best')

    plt.show()
    #plt.savefig('fig2_1.png', bbox_inches='tight')


if __name__ == "__main__":
    #pols = test(200,4000) # for answering Exercise 2.1
    pols = test(2000,1000)
    plot(pols)
