import math

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next
        
    def getval(self):
        total = 0
        counter = 0
        current = self.head
        while(current):
            total += current.data*10**counter
            counter += 1
            current = current.next
        return total  

def mkList(n):
    llist = LinkedList()
    llist.head = Node(n % 10)
    current = llist.head
    n = math.floor(n / 10)
    while n != 0:
        current.next = Node( n % 10)
        current = current.next
        n = math.floor(n / 10)
    return llist

l1 = LinkedList()
l1.head = Node(9)
l1.head.next = Node(9)
l2 = LinkedList()
l2.head = Node(5)
l2.head.next = Node(2)
print(l1.getval())
print(l2.getval())
l3 = mkList(798)
print(l3.getval())
l4 = mkList(l1.getval() + l2.getval())
l4.printLL()
print(l4.getval())