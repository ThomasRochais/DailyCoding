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

class Tree:
    def __init__(self, data):
        self.root = Node(data)

    def inorderSuccessor(self, node):
        if node.parent is None:
            return node.right
        if node == node.parent.left:
            return node.parent
        elif node == node.parent.right:
            return node.right
        else:
            return False

T = Tree(10)
T.root.insertLeft(5)
T.root.insertRight(30)
T.root.right.insertRight(35)
T.root.right.insertLeft(22)
print("Tree")
T.root.PrintTree()
node1 = T.root.right.left
# node2 = T.root.right.right
node3 = T.root.right
node4 = T.root.left
node5 = T.root
print("Inorder successor of", node1.data, "is", T.inorderSuccessor(node1).data)
# print("Inorder successor of", node2.data, "is", T.inorderSuccessor(node2).data)
print("Inorder successor of", node3.data, "is", T.inorderSuccessor(node3).data)
print("Inorder successor of", node4.data, "is", T.inorderSuccessor(node4).data)
print("Inorder successor of", node5.data, "is", T.inorderSuccessor(node5).data)