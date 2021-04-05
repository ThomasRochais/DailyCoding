import math
# Assumes that n is a positive integer
def num_squares(n):
    r = n
    count = 0
    while r > 0:
        r = r - math.floor(math.sqrt(r))**2
        count += 1
    print(count)
    return count
# num_squares(13)
# num_squares(27)
# num_squares(12)

def getMinSquares_recursive(n):
    if n <= 3:
        return n
    res = math.floor(math.sqrt(n)) + 1
    for x in range(1, res):
        res = min(res, 1 + getMinSquares(n - x*x))
    return res

def getMinSquares(n):
    min_sqrs = [0, 1, 2, 3]
    for i in range(4, n + 1):
        res = math.floor(math.sqrt(i)) + 1
        min_sqrs.append(res)
        for x in range(1, res):
            min_sqrs[i] = min(min_sqrs[i], 1 + min_sqrs[i - x*x])
    print(min_sqrs[n])
    return min_sqrs[n]

getMinSquares(13)
getMinSquares(27)
getMinSquares(12)
getMinSquares(9)
