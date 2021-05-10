class SparseArray:
    def __init__(self, arr, size):
        self.arr = {}
        j = 0
        for i in range(size):
            if arr[i]:
                self.arr[j] = arr[i]
                j += 1

    def set(self, i, val):
        self.arr[i] = val

    def get(self, i):
        return self.arr[i]

arr = [2,1,0,0,0,4,5,3,0,0,0,2]
S = SparseArray(arr, len(arr))
print(S.get(4))
print(S.get(3))
S.set(3,12)
print(S.get(3))
print(S.arr)