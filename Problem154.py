class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def push(self, data):
        if self.data == None:
            self.data = data
        elif data < self.data:
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.push(data)
        else:
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.push(data)

    def pop(self):
        def _pop(self):
            if self == None:
                return None
            if self.right == None:
                poped = self
                if self.left:
                    return self.left
                else:
                    return None
            self.right = _pop(self.right)
            return self
        if self.right:
            return _pop(self)
        elif self.left:
            node = self
            self.data = self.left.data
            self.right = self.left.right
            self.left = self.left.left
            return node
        else:
            self.data = None
            return None
        
    def print(self):
        def _print(self):
            if self.left:
                _print(self.left)
            print(self.data, end = " ")
            if self.right:
                _print(self.right)
        _print(self)
        print()

H = Node(21)
H.push(1)
H.push(45)
H.push(78)
H.push(3)
H.push(5)
H.print()
H.pop()
H.print()
H.pop()
H.print()
H.pop()
H.print()
H.pop()
H.print()
H.pop()
H.print()
H.pop()
H.print()
H.pop()
H.print()
H.push(0)
H.push(-1)
H.push(2)
H.print()