def sqrt(n, err):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    l = 0 # Lower bound
    r = n # Upper bound
    while l <= r:
        mid = (l + r) / 2
        if abs(mid * mid - n) < err:
            print("Convergence reached")
            return mid 
        if mid * mid < n:
            l = mid
        elif mid * mid > n:
            r = mid
    return l
print(sqrt(10, 10**-5))
