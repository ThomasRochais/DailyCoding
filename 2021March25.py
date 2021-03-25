class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def push_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Swap the current and current.next nodes that follow prev
    def swap(self, current, prev):
        if current.next is None:
            return
        next = current.next
        if prev is None:
            self.head = current.next
            current.next = next.next
            next.next = current
        else:
            prev.next = next
            current.next = next.next
            next.next = current

    def swap_pairs(self):
        if self.head is None:
            return
        current = self.head
        prev = None
        while current.next:
            self.swap(current, prev)
            prev = current
            current = current.next
            if current is None:
                break

    def print_list(self):
        if self.head is None:
            print("")
            return
        current = self.head
        print(current.data, end="")
        while current.next:
            current = current.next
            print(" -> ", current.data, end="")
        print()

L = LinkedList(1)
L.append_node(2)
L.append_node(3)
L.append_node(4)
L.push_node(0)
L.append_node(5)
L.print_list()
L.swap_pairs()
# L.swap(L.head, None)
# L.swap(L.head.next.next, L.head.next)
L.print_list()
M = LinkedList(1)
M.append_node(2)
M.print_list()
M.swap_pairs()
M.print_list()
N = LinkedList(1)
N.append_node(2)
N.push_node(0)
N.print_list()
N.swap_pairs()
N.print_list()