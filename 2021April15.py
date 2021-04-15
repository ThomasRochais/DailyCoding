def smaller_right(lst):
    N = len(lst)
    counters = [0] * N
    for i in range(N-1):
        current = lst[i]
        counter = 0
        for j in range(i+1, N):
            if lst[j] < current:
                counter += 1
        counters[i] = counter
    print(counters)
    return counters
smaller_right([3, 4, 9, 6, 1])
smaller_right([4, 0, 0, 5, 1])