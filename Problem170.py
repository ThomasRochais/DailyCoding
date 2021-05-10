# Not what the question asked, but still had fun playing with a linked list
class Node:
    def __init__(self, lst = None):
        self.data = None
        self.child = None
        self.parent = None
        self.last = None
        self.add(lst)

    def add_data(self, data):
        if self.data:
            node = self.last
            node.child = Node(data)
            node.child.parent = node
            self.last = node.child
        else:
            self.data = data
            self.last = self

    def add(self, lst):
        if isinstance(lst, list):
            for element in lst:
                self.add_data(element)
        elif isinstance(lst, Node):
            node = lst
            self.add_data(node.data)
        else:
            self.add_data(lst)
    
    def pop(self, n = 0):
        node = self
        for i in range(n):
            if node.child:
                node = node.child
            else:
                raise ValueError("Out of range")
        val = node.data
        if node.parent:
            if node.child:
                node.child.parent = node.parent
                node.parent.child = node.child
            else:
                node.parent.child = None
                node.parent.last = node.parent
        else:
            if node.child:
                node.data = node.child.data
                node.child = node.child.child
                if node.child:
                    node.child.parent = node
            else:
                node.data = None
                node.last = None
        return val

    def print(self):
        print(self.data, end="")
        node = self
        while node.child:
            print(" ->", node.child.data, end = "")
            node = node.child
        print()

# Return a sorted list from two sorted lists
def merge(lst1, lst2):
    lst = Node()
    pt1 = lst1
    pt2 = lst2
    while pt1 and pt2:
        if pt1.data < pt2.data:
            lst.add(pt1.data)
            pt1 = pt1.child
        else:
            lst.add(pt2.data)
            pt2 = pt2.child
    if pt1:
        lst.add(pt1)
    elif pt2:
        lst.add(pt2)
    return lst

L = Node([1,2,3,4])
L.print()
print(L.pop(0))
L.print()
print(L.pop(1))
L.print()
print(L.pop())
L.print()
print(L.pop())
L.print()
# N = Node([7,8,9])
# merge(L,N).print()
