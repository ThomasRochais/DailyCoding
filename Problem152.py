import random
import matplotlib.pyplot as plt
def rand_dist(L, P):
    if len(L) != len(P) or sum(P) != 1:
        return "Improper input"
    else:
        r = random.random()
        i_min = 0
        i_max = P[0]
        for i in range(len(L)-1):
            if r >= i_min and r < i_max:
                return L[i]
            i_min = i_min + P[i]
            i_max = i_min + P[i+1]
        return L[-1]

def mk_hist(L, P, N):
    hist = []
    for i in range(N):
        hist.append(rand_dist(L, P))
    return hist

L = [1, 2, 3, 4]
P = [0.1, 0.5, 0.2, 0.2]
plt.hist(mk_hist(L, P, 1000), bins = len(L), rwidth = .2)
plt.xticks(ticks = L)
plt.show()