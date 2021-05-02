import itertools
sample = [i for i in range(10)]
N = 8
for subset in itertools.combinations(sample[1:-1], N-2):
    print(subset)