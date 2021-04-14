def find_duplicate(lst):
    n = len(lst)
    # Assume the element of lst all belong to the set {1, 2, ..., n-1}
    count = [0] * (n-1)
    for i in range(n):
        count[lst[i]-1] += 1
        if count[lst[i]-1] > 1:
            print(lst[i])
            return lst[i]

find_duplicate([1,2,3,3])
find_duplicate([1,2,3,4,2])
find_duplicate([1,2,1,3,4,5])