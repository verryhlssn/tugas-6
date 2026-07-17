class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next  # simpan next
            current.next = prev       # balik arah
            prev = current            # geser prev
            current = next_node       # geser current

        self.head = prev

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Contoh penggunaan
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)

print("Sebelum reverse:")
sll.display()

sll.reverse()

print("Sesudah reverse:")
sll.display()