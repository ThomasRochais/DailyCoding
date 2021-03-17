import math

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insertLeft(self, data):
        self.left = Node(data)
    
    def insertRight(self, data):
        self.right = Node(data)

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

class NodeTree:
    def __init__(self, data):
        self.root = Node(data)
        self.path = []
        self.minLeaf = Node(math.inf)

    def minPathSum(self, tmp, node):
        if node.left:
            #node.left.data += node.data
            tmpLeft = Node(node.data + node.left.data)
            tmpLeft.left = node.left.left
            tmpLeft.right = node.left.right
            self.minPathSum(tmpLeft, node.left)
        if node.right:
            #node.right.data += node.data
            tmpRight = Node(node.data + node.right.data)
            tmpRight.left = node.right.left
            tmpRight.right = node.right.right
            self.minPathSum(tmpRight, node.right)
        if not node.left and not node.right:
            if node.data < self.minLeaf.data:
                self.minLeaf = node
        return self.minLeaf

    def pathToNode(self, root, node):
        if root is None:
            return False
        if root == node or self.pathToNode(root.left, node) or self.pathToNode(root.right, node):
            self.path.append(root.data)
            return True
        return False

N = NodeTree(10)
N.root.insertLeft(5)
N.root.insertRight(5)
N.root.left.insertRight(2)
N.root.right.insertRight(1)
N.root.right.right.insertRight(-1)
print("Tree: ")
N.root.PrintTree()
print("Min path sum: ")
print(N.minPathSum(N.root, N.root).data)
print("Tree: ")
N.root.PrintTree()
print("Min path: ")
N.pathToNode(N.root, N.minLeaf)
print(N.path)