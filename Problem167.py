class Iterator2D:
    def __init__(self, array):
        self.array = array # Should be an array of arrays
        self.size = len(array)
        self.i = 0
        self.j = -1

    def next(self):
        if not self.has_next():
            raise ValueError("No more elements")
        else:
            return self.array[self.i][self.j]

    def has_next(self):
        if self.i >= self.size:
            return False
        if self.j + 1 < len(self.array[self.i]):
            self.j += 1
            return True
        self.i += 1
        self.j = -1
        return self.has_next()

IT = Iterator2D([[1, 2], [3], [], [4, 5, 6]])
print(IT.next())
print(IT.next())
print(IT.next())
print(IT.next())
print(IT.next())
print(IT.next())
print(IT.has_next())
IT = Iterator2D([[10]])
print(IT.next())
print(IT.has_next())