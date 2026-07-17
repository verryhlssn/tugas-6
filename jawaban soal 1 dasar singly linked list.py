class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = node(data)

        if self.head is None:
           self.head = new_node
           return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("none")

# contoh penggunaan
sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.display()