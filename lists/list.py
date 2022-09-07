class Node:
    def __init__(self, data: int) -> None:
        self.next = None
        self.data = data
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    def print(self) -> str:
        if self.head == None:
            print('')
            pass
        n = self.head
        value = ''
        while n != None:
            value += str(n.data) + ', '
            n = n.next
        print(value)
        
    def insert_at_start(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            pass
        node.next = self.head
        self.head = node
        
if __name__ == "__main__":
    node_one = Node(7)
    list = LinkedList()
    
    list.head = node_one
    list.insert_at_start(5)
    list.print()
    