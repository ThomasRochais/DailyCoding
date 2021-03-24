from math import inf
def sol(L, k):
    N = len(L)
    profit = - inf
    for i in range(N-2*k+1):
        tmprofit = -L[i] + L[i+1]
        if k > 1:
            for j in range(i+2, i+2+k, 2):
                tmprofit = tmprofit - L[j] + L[j+1]
        profit = max(profit, tmprofit)
    print(profit)
sol([5, 2, 4, 0, 1], 2)
sol([5, 2, 4, 0, 1], 1)
sol([5, 2, 4, 0, 1], 3)
sol([5, 2, 4, 0, 1, 5], 3)
sol([5, 2, 4, 0, 1, 5, 10], 3)
sol([5, 2, 4, 0, 1, 5, 10], 1)