class Hanoi:
    def __init__(self, n):
        self.n = n # Number of rings
        self.s1 = list(range(n,0,-1))
        self.s2 = []
        self.s3 = []
        self.l = [self.s1, self.s2, self.s3]
        self.moves = []

    def move(self, i, j):
        if len(self.l[i-1]) != 0:
            ring = self.l[i-1].pop()
            self.l[j-1].append(ring)
            print("Move ring", ring, "from rod", i, "to rod", j)
        else:
            print("Invalid move")

    def legalMove(self, i, j):
        if len(self.l[i-1]) == 0 and len(self.l[j-1]) == 0:
            return []
        elif len(self.l[i-1]) != 0 and len(self.l[j-1]) == 0:
            self.move(i, j)
            return (i, j)
        elif len(self.l[i-1]) == 0 and len(self.l[j-1]) != 0:
            self.move(j, i)
            return (j, i)
        elif self.l[i-1][-1] < self.l[j-1][-1]:
            self.move(i, j)
            return (i, j)
        else:
            self.move(j, i)
            return (j, i)

    def getStatus(self):
        print("Rod 1:", self.s1)
        print("Rod 2:", self.s2)
        print("Rod 3:", self.s3)

    def GameOver(self):
        if len(self.s1) == 0 and len(self.s2) == 0 and self.s3 == list(range(self.n,0,-1)):
            return True
        else:
            return False

    def solve(self):
        if not self.GameOver():
            moves = []
            disks = self.n
            source = 1
            spare = 2
            target = 3
            if disks == 0:
                return []
            if disks % 2 == 0: # Swap target and spare
                target = 2
                spare = 3
            for i in range(2**disks - 1):
                if i % 3 == 0:
                    moves.append(self.legalMove(source, target))
                if i % 3 == 1:
                    moves.append(self.legalMove(source, spare))
                if i % 3 == 2:
                    moves.append(self.legalMove(spare, target))
            return moves
        else:
            return("Already solved")
        

# game = Hanoi(3)
# game.getStatus()
# game.move(1,3)
# game.move(1,2)
# game.move(3,2)
# game.move(1,3)
# game.move(2,1)
# game.move(2,3)
# game.move(1,3)
# game.getStatus()

def hanoi_recursive(disks, source, target, spare):
    if disks == 0:
        return []
    moves = hanoi_recursive(disks - 1, source, spare, target)
    moves.append((source, target))
    moves.extend(hanoi_recursive(disks - 1, spare, target, source))
    return moves

moves = hanoi_recursive(4, 1, 3, 2)
for i in moves:
    print("Move from Rod", i[0], "to Rod", i[1])


game = Hanoi(4)
game.getStatus()
print(game.GameOver())
game.solve()
game.getStatus()
print(game.GameOver())
print(game.solve())