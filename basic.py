class Node:
    def __init__(self, data: int):
        self.prev = None
        self.data = data
        self.next = None 

class DoublyLinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
    
    def add_node(self, node: Node):
        if not self.head:
            self.head = self.tail = node
            return

        node.prev = self.tail
        self.tail.next = node
        self.tail = self.tail.next
    
    def backward(self):
        current = self.tail
        while current:
            print(current.data)
            current = current.prev
    
    def forward(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

dl = DoublyLinkedList()

for i in range(5):
    node = Node(data=i)
    dl.add_node(node)

print('Print data in backward')
dl.backward()
print('Print data in forward')
dl.forward()