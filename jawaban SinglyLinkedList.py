class Node:    # Kelas untuk node (elemen) dalam linked list
    def __init__(self, value=None):    # Konstruktor node
        self.value = value    # Menyimpan nilai/data node
        self.next = None    # Pointer ke node berikutnya

class SLinkedList:    # Kelas Singly Linked List
    def __init__(self):    # Konstruktor list
        self.head = None    # Pointer ke node pertama
        self.tail = None    # Pointer ke node terakhir

    def __iter__(self):    # Membuat object bisa di-iterasi (loop)
        node = self.head    # Mulai dari head
        while node:    # Selama node tidak None
            yield node    # Kembalikan node saat ini
            node = node.next    # Pindah ke node berikutnya

# insert in linked list
                    
    def insertSLL(self, value, location):    # Method untuk insert node
            newNode = Node(value)    # Buat node baru
            if self.head is None:    # Jika list kosong
                self.head = newNode    # Node jadi head
                self.tail = newNode    # Node juga jadi tail
            else:    # Jika list sudah ada isi
                if location == 0:    # Insert di awal
                    newNode.next = self.head    # Node baru menunjuk head lama
                    self.head = newNode    # Update head
                elif location == -1:    # Insert di akhir
                    newNode.next = None    # Node terakhir tidak menunjuk ke mana-mana
                    self.tail.next = newNode    # Tail lama menunjuk node baru
                    self.tail = newNode    # Update tail
                else:    # Insert di posisi tengah
                    tempNode = self.head    # Mulai dari head
                    index = 0    # Counter posisi
                    while index < location - 1:    # Loop sampai posisi sebelum target
                        if tempNode.next is None:    # Jika sudah di akhir list
                            break    # Hentikan loop
                        tempNode = tempNode.next    # Pindah ke node berikutnya
                        index += 1    # Increment index
                    nextNode = tempNode.next    # Simpan node berikutnya
                    tempNode.next = newNode    # Hubungkan node sekarang ke node baru
                    newNode.next = nextNode    # Node baru menunjuk ke nextNode
                    if tempNode == self.tail:    # Jika insert di akhir sebenarnya
                        self.tail=newNode    # Update tail

    # Traverse Singly Linked List

    def traverseSLL(self):    # Method untuk menampilkan semua node
        if self.head is None:    # Jika list kosong
            print("The Singly Linked List does not exist")    # Tampilkan pesan
        else:    # Jika ada isi
            node = self.head    # Mulai dari head
            while node is not None:    # Selama node ada
                print(node.value)    # Cetak nilai node
                node = node.next    # Pindah ke node berikutnya

    # Search for a node in Singly Linked List
    def searchSLL(self, nodeValue):    # Method untuk mencari nilai
        if self.head is None:    # Jika list kosong
           return "The list does not exist"    # Return pesan
        else:    # Jika ada isi
            node = self.head    # Mulai dari head
            while node is not None:    # Loop traversal
                if node.value == nodeValue:    # Jika ditemukan
                    return node.value    # Return nilai
                node = node.next    # Pindah ke node berikutnya
            return "The value does not exist in this list"    # Jika tidak ditemukan

    #  Delete a node from Singly Linked List

    def deleteNode(self, location):    # Method untuk menghapus node
        if self.head is None:    # Jika list kosong
            print("The SLL does not exist")    # Pesan error
        else:    # Jika ada isi
            if location == 0:    # Hapus node pertama
                if self.head == self.tail:    # Jika hanya 1 node
                    self.head = None    # Kosongkan head
                    self.tail = None    # Kosongkan tail
                else:    # Jika lebih dari 1 node
                    self.head = self.head.next    # Geser head ke node berikutnya
            elif location == -1:    # Hapus node terakhir
                if self.head == self.tail:    # Jika hanya 1 node
                    self.head = None    # Kosongkan head
                    self.tail = None    # Kosongkan tail
                else:    # Jika lebih dari 1 node
                    node = self.head    # Mulai dari head
                    while node is not None:    # Loop traversal
                        if node.next == self.tail:    # Jika node sebelum tail
                            break    # Stop loop
                        node = node.next    # Pindah ke node berikutnya
                    node.next = None    # Putuskan link ke tail lama
                    self.tail = node    # Update tail
            else:    # Hapus node di tengah
                tempNode = self.head    # Mulai dari head
                index = 0    # Counter posisi
                while index < location - 1:    # Cari node sebelum target
                    if tempNode.next is None:    # Jika melebihi batas list
                        print("index di luar batas")    # Pesan error
                        return    # Hentikan fungsi
                    tempNode = tempNode.next    # Pindah ke node berikutnya
                    index += 1    # Tambah index
                nextNode = tempNode.next    # Node yang akan dihapus

                if nextNode is None:    # Jika node target tidak ada
                    print("index di luar batas")    # Pesan error
                    return    # Hentikan fungsi
                
                tempNode.next = nextNode.next    # Lewati node target (hapus)

    # Delete entire SLL

    def deleteEntireSLL(self):    # Method untuk hapus semua node
        if self.head is None:    # Jika sudah kosong
            print("The SLL does not exist")    # print dengan Pesan
        else:    # Jika ada isi
            self.head = None    # Hapus semua node dari head
            self.tail = None    # Hapus referensi tail


singlyLinkedList = SLinkedList()    # Membuat objek linked list
singlyLinkedList.insertSLL(1, 1)    # Insert nilai 1
singlyLinkedList.insertSLL(2, 3)    # Insert nilai 2
singlyLinkedList.insertSLL(3, 1)    # Insert nilai 3
singlyLinkedList.insertSLL(4, 1)    # Insert nilai 4
singlyLinkedList.insertSLL(0, 0)    # Insert di awal
singlyLinkedList.insertSLL(7, -1)    # Insert di akhir
singlyLinkedList.insertSLL(5, 6)    # Insert di posisi tertentu


singlyLinkedList.insertSLL(1,1)    # Insert lagi
singlyLinkedList.insertSLL(2,5)    # Insert lagi
singlyLinkedList.insertSLL(3,1)    # Insert lagi
singlyLinkedList.insertSLL(4,9)    # Insert lagi
singlyLinkedList.insertSLL(5,-1)    # Insert di akhir
singlyLinkedList.insertSLL(1, 1)    # Insert lagi
singlyLinkedList.insertSLL(2, 1)    # Insert lagi
singlyLinkedList.insertSLL(3, 1)    # Insert lagi
singlyLinkedList.insertSLL(4, 1)    # Insert lagi
singlyLinkedList.insertSLL(5,-1)    # Insert di akhir

print([node.value for node in singlyLinkedList])    # Cetak isi linked list
singlyLinkedList.deleteEntireSLL()    # Hapus seluruh list
print([node.value for node in singlyLinkedList])    # Cetak lagi (harus kosong)

# output :
# [0, 4, 3, 2, 1, 3, 1, 1, 4, 3, 2, 2, 7, 4, 5, 5, 5]
# []