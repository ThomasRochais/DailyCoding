class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.parent = None
        self.data = data

    def insertLeft(self, data):
        self.left = Node(data)
        self.left.parent = self
    
    def insertRight(self, data):
        self.right = Node(data)
        self.right.parent = self

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    def containsOne(self):
        if self.data == 1:
            return True
        if self.left:
            return self.left.containsOne()
        if self.right:
            return self.right.containsOne()
        return False

    def pruneTree(self):
        if self.left:
            if self.left.containsOne() == False:
                self.left = None
            else:
                self.left.pruneTree()
        if self.right:
            if self.right.containsOne() == False:
                self.right = None
            else:
                self.right.pruneTree()

T = Node(0)
T.insertLeft(1)
T.insertRight(0)
T.right.insertRight(0)
T.right.insertLeft(1)
T.right.left.insertRight(0)
T.right.left.insertLeft(0)
print("Tree")
T.PrintTree()
print(T.containsOne())
T.pruneTree()
print("Pruned Tree")
T.PrintTree()