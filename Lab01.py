def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data, '--->', end=' ')
                n = n.next

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node


LL1 = LinkedList()
LL1.insert_at_head(100)
LL1.insert_at_end(200)
LL1.insert_at_end(450)
LL1.insert_at_head(300)
LL1.insert_at_end(500)
LL1.print_LL()
