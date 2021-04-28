def sqrt(n):
    f = lambda x: x*x - n
    fp = lambda x: 2*x
    iterate = lambda x: x - f(x) / fp(x)
    MAX_ITER = 10**5
    EPSILON = 10**(-10)
    x0 = 1
    x1 = iterate(x0)
    i = 1
    while abs(x1-x0) > EPSILON and i < MAX_ITER:
        x0 = x1
        x1 = iterate(x0)
        i += 1
    print("Number of steps:", i)
    return x1

print(sqrt(20))
print(sqrt(100))
print(sqrt(98765))