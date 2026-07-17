class Node:    # Kelas untuk membuat node (elemen) pada linked list
    def __init__(self, value=None):    # Konstruktor untuk inisialisasi node
        self.value = value    # Menyimpan nilai/data node
        self.next = None    # Pointer ke node berikutnya

class CircularSinglyLinkedList:    # Kelas untuk Circular Singly Linked List
    def __init__(self):    # Konstruktor untuk inisialisasi list
        self.head = None    # Pointer ke node pertama
        self.tail = None    # Pointer ke node terakhir

    def __iter__(self):    # Method agar object bisa di-iterasi (loop)
        if self.head is None:    # Jika list kosong
            return    # Hentikan iterasi
        node = self.head    # Mulai dari head
        while True:    # Loop tak hingga
            yield node    # Kembalikan node saat ini
            node = node.next    # Pindah ke node berikutnya
            if node == self.head:    # Jika kembali ke head
                break    # Hentikan loop

    #  Creation of circular singly linked list   
    #  
    def createCSLL(self, nodeValue):    # Method untuk membuat CSLL pertama kali
        node = Node(nodeValue)    # Buat node baru
        node.next = node    # Node menunjuk ke dirinya sendiri (circular)
        self.head = node    # Set head ke node
        self.tail = node    # Set tail ke node
        return "The CSLL has been created"    # Return pesan sukses
        
    #  Insertion of a node in circular singly linked list 
    #    
    def insertCSLL(self, value, location):    # Method untuk insert node
        if self.head is None:    # Jika list kosong
            return "The head reference is None"    # Tidak bisa insert
        else:    # jika list tidak kosong
            newNode = Node(value)    # Buat node baru
            if location == 0:    # Insert di awal
                newNode.next = self.head    # Node baru menunjuk ke head lama
                self.head = newNode    # Update head ke node baru
                self.tail.next = newNode    # Tail menunjuk ke head baru
            elif location == 1:    # Insert di akhir
                newNode.next = self.tail.next    # Node baru menunjuk ke head
                self.tail.next = newNode    # Tail lama menunjuk ke node baru
                self.tail = newNode    # Update tail
            else:    # Insert di tengah
                tempNode = self.head    # Mulai dari head
                index = 0    # Index awal
                while index < location - 1:    # Loop sampai posisi sebelum target
                    tempNode = tempNode.next    # Pindah ke node berikutnya
                    index += 1    # Increment index
                    if tempNode == self.tail:    # Jika sampai tail
                        break    # Hentikan loop
                nextNode = tempNode.next    # Simpan node berikutnya
                tempNode.next = newNode    # Hubungkan node sebelumnya ke node baru
                newNode.next = nextNode    # Hubungkan node baru ke node berikutnya
            return "The node has been successfully inserted"    # Return sukses
        
    # Traversal of a node in circular singly linked list    

    def traversalCSLL(self):    # Method untuk menampilkan semua node
        if self.head is None:    # Jika kosong
            print("There is not any element for traversal")    # Tampilkan pesan
        else:    # jika ada isi
            tempNode = self.head    # Mulai dari head
            while tempNode:    # Loop
                print(tempNode.value)    # Cetak nilai node
                tempNode = tempNode.next    # Pindah ke node berikutnya
                if tempNode == self.head:    # Jika kembali ke head
                    break    # Hentikan loop
        
    # Searching for a node in circular singly linked list    
    def searchCSLL(self, nodeValue):    # Method untuk mencari node
        if self.head is None:    # Jika kosong
            return "There is not any node in this CSLL"    # Pesan error
        else:    # jika ada node
            tempNode = self.head    # Mulai dari head
            while tempNode:    # Loop
                if tempNode.value == nodeValue:    # Jika ditemukan
                    return tempNode.value    # Return nilai
                tempNode = tempNode.next    # Pindah ke node berikutnya
                if tempNode == self.head:    # Jika kembali ke head
                    return "The node does not exist in this CSLL"    # Tidak ditemukan
    
    # Delete a node from circular singly linked list 
       
    def deleteNode(self, location):    # Method untuk menghapus node
        if self.head is None:    # Jika kosong
            print("There is not any node in CSLL")    # Pesan error
        else:    # jika ada node
            if location == 0:    # Hapus node pertama
                if self.head == self.tail:    # Jika hanya satu node
                    self.head.next = None    # Putuskan link
                    self.head = None    # Kosongkan head
                    self.tail = None    # Kosongkan tail
                else:    # jika lebih dari 1 node
                    self.head = self.head.next    # Geser head
                    self.tail.next = self.head    # Hubungkan tail ke head baru
            elif location == 1:    # Hapus node terakhir
                if self.head == self.tail:    # Jika hanya satu node
                    self.head.next = None  # putus link  
                    self.head = None    # kosongkan head
                    self.tail = None    # kosongkan tail
                else:    # jika lebih dari 1 node
                    node = self.head    # Mulai dari head
                    while node.next != self.tail:    # Cari node sebelum tail
                        node = node.next    # geser
                    node.next = self.head    # Hubungkan ke head
                    self.tail = node    # Update tail
            else:    # Hapus node di tengah
                tempNode = self.head    # Mulai dari head
                index = 0    # counter posisi
                while index < location - 1:    # Cari node sebelum target
                    tempNode = tempNode.next    # geser node
                    index += 1    # tambah index
                    if tempNode.next == self.tail:    # Jika mendekati tail
                        break    # stop loop
                nextNode = tempNode.next    # Node yang akan dihapus
                tempNode.next = nextNode.next    # Lewati node tersebut
        
    # Delete entire circular sinlgy linked list    

    def deleteEntireCSLL(self):    # Method untuk menghapus seluruh list
        if self.head is None:    # Jika kosong
            return    # Tidak ada yang dihapus
        self.tail.next = None    # Putuskan circular link
        self.head = None    # Kosongkan head
        self.tail = None    # Kosongkan tail

circularSLL = CircularSinglyLinkedList()    # Buat objek CSLL    
circularSLL.createCSLL(0)    # Buat node pertama dengan nilai 0    
circularSLL.insertCSLL(1,1)    # Insert node 1 di akhir    
circularSLL.insertCSLL(2,1)    # Insert node 2 di akhir    
circularSLL.insertCSLL(3,1)    # Insert node 3 di akhir    

print([node.value for node in circularSLL])    # Cetak semua nilai node    
circularSLL.deleteEntireCSLL()    # Hapus seluruh list    
print([node.value for node in circularSLL])    # Cetak lagi (harus kosong)

# output :
# [0, 1, 2, 3]
# []