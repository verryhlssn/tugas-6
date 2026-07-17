class Node: # Node class untuk menyimpan data dan pointer ke node berikutnya
    def __init__(self, value=None): # Konstruktor untuk inisialisasi nilai dan pointer next
        self.value = value # Menyimpan nilai dari node
        self.next = None # Pointer ke node berikutnya, diinisialisasi dengan None

class SLinkedList: # Kelas untuk mengelola linked list, menyimpan head dan tail
    def __init__(self): # Konstruktor untuk inisialisasi head dan tail
        self.head = None # Pointer ke node pertama dalam linked list, diinisialisasi dengan None
        self.tail = None # Pointer ke node terakhir dalam linked list, diinisialisasi dengan None
    def __iter__(self): # Fungsi iterasi untuk memungkinkan iterasi melalui linked list menggunakan for loop atau list comprehension
        node = self.head # Mulai iterasi dari head
        while node: # Selama node tidak None, terus iterasi
            yield node # Menghasilkan node saat ini untuk iterasi
            node = node.next # Pindah ke node berikutnya dalam linked list
   
    # insert in Linked List #

    def insertSLL(self, value, location): # Fungsi untuk menyisipkan node baru ke dalam linked list pada lokasi tertentu
        newNode = Node(value) # Membuat node baru dengan nilai yang diberikan
        if self.head is None: # Jika linked list kosong, set head dan tail ke node baru
            self.head = newNode # Set head ke node baru
            self.tail = newNode # Set tail ke node baru
        else: # Jika linked list tidak kosong, tentukan lokasi penyisipan
            if location == 0: # Jika lokasi adalah 0, sisipkan node baru di awal linked list
                newNode.next = self.head # Set pointer next dari node baru ke head saat ini
                self.head = newNode # Update head ke node baru
            elif location == 1: # Jika lokasi adalah 1, sisipkan node baru di akhir linked list
                newNode.next = None # Set pointer next dari node baru ke None karena akan menjadi node terakhir
                self.tail.next = newNode # Set pointer next dari tail saat ini ke node baru
                self.tail = newNode # Update tail ke node baru
            else: # Jika lokasi adalah selain 0 atau 1, sisipkan node baru di posisi tertentu dalam linked list
                tempNode = self.head # Mulai dari head untuk mencari posisi penyisipan
                index = 0 # Inisialisasi index untuk melacak posisi saat iterasi
                while index < location - 1: # Iterasi untuk menemukan node sebelum posisi penyisipan
                    if tempNode.next is None: # Jika mencapai akhir linked list sebelum menemukan posisi, keluar dari loop
                        break # Keluar dari loop jika posisi penyisipan melebihi panjang linked list
                    tempNode = tempNode.next # Pindah ke node berikutnya
                    index += 1 # Increment index untuk melacak posisi
                nextNode = tempNode.next # Simpan pointer next dari node sebelum posisi penyisipan untuk menghubungkan ke node baru
                tempNode.next = newNode # Set pointer next dari node sebelum posisi penyisipan ke node baru
                newNode.next = nextNode # Set pointer next dari node baru ke node yang sebelumnya berada di posisi penyisipan

    # Traverse Singly Linked List
    
    def traverseList(self): # Fungsi untuk menampilkan semua nilai dalam linked list dengan traversing dari head ke tail
        if self.head is None: # Jika linked list kosong, tampilkan pesan bahwa linked list tidak ada
            print("The Singly Linked List does not exist") # Pesan untuk linked list yang tidak ada
        else: # Jika linked list tidak kosong, iterasi melalui linked list dan tampilkan nilai setiap node
            node = self.head # Mulai dari head untuk traversing
            while node is not None: # Selama node tidak None, terus traversing
                print(node.value) # Tampilkan nilai dari node saat ini
                node = node.next # Pindah ke node berikutnya untuk melanjutkan traversing

 # Search for a node in Singly Linked List

    def searchSLL(self, nodeValue): # Fungsi untuk mencari nilai tertentu dalam linked list, mengembalikan nilai jika ditemukan atau pesan jika tidak ditemukan
        if self.head is None: # Jika linked list kosong, tampilkan pesan bahwa linked list tidak ada
            print("The Singly Linked List does not exist") # Pesan untuk linked list yang tidak ada
        else: # Jika linked list tidak kosong, iterasi melalui linked list dan cari nilai yang dicari
            node = self.head # Mulai dari head untuk mencari nilai
            while node is not None: # Selama node tidak None, terus mencari
                if node.value == nodeValue: # Jika nilai dari node saat ini sama dengan nilai yang dicari, kembalikan nilai tersebut
                    return node.value # Kembalikan nilai yang ditemukan
                node = node.next # Pindah ke node berikutnya untuk melanjutkan pencarian
            return "The node does not exist in this SLL" # Jika mencapai akhir linked list tanpa menemukan nilai, kembalikan pesan bahwa node tidak ada dalam linked list

    # Delete a node from Singly Linked List
 
    def deleteNode(self, location): # Fungsi untuk menghapus node dari linked list berdasarkan lokasi tertentu, memperbarui head atau tail jika diperlukan
        if self.head is None: # Jika linked list kosong, tampilkan pesan bahwa linked list tidak ada
            return "The Singly Linked List does not exist" # Pesan untuk linked list yang tidak ada
        else: # Jika linked list tidak kosong, tentukan lokasi penghapusan
            if location == 0: # Jika lokasi adalah 0, hapus node pertama (head) dari linked list
                if self.head == self.tail: # Jika head dan tail adalah node yang sama, berarti hanya ada satu node dalam linked list, set head dan tail ke None
                    self.head = None # Set head ke None karena linked list akan menjadi kosong setelah penghapusan
                    self.tail = None # Set tail ke None karena linked list akan menjadi kosong setelah penghapusan
                else: # Jika ada lebih dari satu node, update head ke node berikutnya untuk menghapus node pertama
                    self.head = self.head.next # Update head ke node berikutnya untuk menghapus node pertama
            elif location == 1: # Jika lokasi adalah 1, hapus node terakhir (tail) dari linked list
                if self.head == self.tail: # Jika head dan tail adalah node yang sama, berarti hanya ada satu node dalam linked list, set head dan tail ke None
                    self.head = None # Set head ke None karena linked list akan menjadi kosong setelah penghapusan
                    self.tail = None # Set tail ke None karena linked list akan menjadi kosong setelah penghapusan
                else: # Jika ada lebih dari satu node, iterasi melalui linked list untuk menemukan node sebelum tail, update pointer next dari node tersebut ke None dan update tail ke node tersebut
                    node = self.head # Mulai dari head untuk mencari node sebelum tail
                    while node is not None: # Selama node tidak None, terus mencari
                        if node.next == self.tail: # Jika pointer next dari node saat ini adalah tail, berarti node saat ini adalah node sebelum tail
                            break # Keluar dari loop jika node sebelum tail ditemukan
                        node = node.next # Pindah ke node berikutnya untuk melanjutkan pencarian
                    node.next = None # Set pointer next dari node sebelum tail ke None untuk menghapus tail
                    self.tail = node # Update tail ke node sebelum tail yang sekarang menjadi node terakhir setelah penghapusan
            else: # Jika lokasi adalah selain 0 atau 1, hapus node di posisi tertentu dalam linked list
                tempNode = self.head # Mulai dari head untuk mencari node sebelum posisi penghapusan
                index = 0 # Inisialisasi index untuk melacak posisi saat iterasi
                while index < location-1: # Iterasi untuk menemukan node sebelum posisi penghapusan
                    if tempNode.next is None: # Jika mencapai akhir linked list sebelum menemukan posisi, keluar dari loop
                        break # Keluar dari loop jika posisi penghapusan melebihi panjang linked list
                    tempNode = tempNode.next # Pindah ke node berikutnya
                    index += 1 # Increment index untuk melacak posisi
                nextNode = tempNode.next # Simpan pointer next dari node sebelum posisi penghapusan untuk menghubungkan ke node setelah posisi penghapusan
                tempNode.next = nextNode.next # Set pointer next dari node sebelum posisi penghapusan ke node setelah posisi penghapusan untuk menghapus node di posisi tersebut
    
    # Delete entire SLL

    def deleteEntireSLL(self): # Fungsi untuk menghapus seluruh linked list dengan mengatur head dan tail ke None
        if self.head is None: # Jika linked list kosong, tampilkan pesan bahwa linked list tidak ada
            print("SLL does not exist") # Pesan untuk linked list yang tidak ada
        else: # Jika linked list tidak kosong, set head dan tail ke None untuk menghapus seluruh linked list
            self.head = None # Set head ke None untuk menghapus seluruh linked list
            self.tail = None # Set tail ke None untuk menghapus seluruh linked list

singlyLinkedList = SLinkedList() # Membuat instance dari SLinkedList untuk mengelola linked list
singlyLinkedList.insertSLL(44,6) # Menyisipkan nilai 44 ke dalam linked list pada lokasi 6 (karena linked list masih kosong, nilai ini akan menjadi head dan tail)
print([node.value for node in singlyLinkedList])  # Menampilkan nilai dari semua node dalam linked list menggunakan list comprehension untuk iterasi melalui linked list
class Node: # Node class untuk menyimpan data dan pointer ke node berikutnya
    def __init__(self, value=None): # Konstruktor untuk inisialisasi nilai dan pointer next
        self.value = value # Menyimpan nilai dari node
        self.next = None # Pointer ke node berikutnya, diinisialisasi dengan None

class SLinkedList: # Kelas untuk mengelola linked list, menyimpan head dan tail
    def __init__(self): # Konstruktor untuk inisialisasi head dan tail
        self.head = None # Pointer ke node pertama dalam linked list, diinisialisasi dengan None
        self.tail = None # Pointer ke node terakhir dalam linked list, diinisialisasi dengan None
    def __iter__(self): # Fungsi iterasi untuk memungkinkan iterasi melalui linked list menggunakan for loop atau list comprehension
        node = self.head # Mulai iterasi dari head
        while node: # Selama node tidak None, terus iterasi
            yield node # Menghasilkan node saat ini untuk iterasi
            node = node.next # Pindah ke node berikutnya dalam linked list
    
    # insert in Linked List
      
    def insertSLL(self, value, location): # Fungsi untuk menyisipkan node baru ke dalam linked list pada lokasi tertentu
        newNode = Node(value) # Membuat node baru dengan nilai yang diberikan
        if self.head is None: # Jika linked list kosong, set head dan tail ke node baru
            self.head = newNode # Set head ke node baru
            self.tail = newNode # Set tail ke node baru
        else: # Jika linked list tidak kosong, tentukan lokasi penyisipan
            if location == 0: # Jika lokasi adalah 0, sisipkan node baru di awal linked list
                newNode.next = self.head # Set pointer next dari node baru ke head saat ini
                self.head = newNode # Update head ke node baru
            elif location == 1: # Jika lokasi adalah 1, sisipkan node baru di akhir linked list
                newNode.next = None # Set pointer next dari node baru ke None karena akan menjadi node terakhir
                self.tail.next = newNode # Set pointer next dari tail saat ini ke node baru
                self.tail = newNode # Update tail ke node baru
            else: # Jika lokasi adalah selain 0 atau 1, sisipkan node baru di posisi tertentu dalam linked list
                tempNode = self.head # Mulai dari head untuk mencari posisi penyisipan
                index = 0 # Inisialisasi index untuk melacak posisi saat iterasi
                while index < location - 1: # Iterasi untuk menemukan posisi penyisipan
                    if tempNode.next is None: # Jika mencapai akhir linked list sebelum menemukan posisi, keluar dari loop
                        break # Keluar dari loop jika posisi penyisipan melebihi panjang linked list
                    tempNode = tempNode.next # Pindah ke node berikutnya
                    index += 1 # Increment index untuk melacak posisi
                nextNode = tempNode.next # Simpan pointer next dari node sebelum posisi penyisipan untuk menghubungkan ke node baru
                tempNode.next = newNode # Set pointer next dari node sebelum posisi penyisipan ke node baru
                newNode.next = nextNode # Set pointer next dari node baru ke node yang sebelumnya berada di posisi penyisipan

    # Traverse Singly Linked List
    
    def traverseList(self): # Fungsi untuk menampilkan semua nilai dalam linked list dengan traversing dari head ke tail
        if self.head is None: # Jika linked list kosong, tampilkan pesan bahwa linked list tidak ada
            print("The Singly Linked List does not exist") # Pesan untuk linked list yang tidak ada
        else: # Jika linked list tidak kosong, iterasi melalui linked list dan tampilkan nilai setiap node
            node = self.head # Mulai dari head untuk traversing
            while node is not None: # Selama node tidak None, terus traversing
                print(node.value) # Tampilkan nilai dari node saat ini
                node = node.next # Pindah ke node berikutnya untuk melanjutkan traversing

 # Search for a node in Singly Linked List

    def searchSLL(self, nodeValue): # Fungsi untuk mencari nilai tertentu dalam linked list, mengembalikan nilai jika ditemukan atau pesan jika tidak ditemukan
        if self.head is None: # Jika linked list kosong, tampilkan pesan bahwa linked list tidak ada
            print("The Singly Linked List does not exist") # Pesan untuk linked list yang tidak ada
        else: # Jika linked list tidak kosong, iterasi melalui linked list dan cari nilai yang dicari
            node = self.head # Mulai dari head untuk pencarian
            while node is not None: # Selama node tidak None, terus pencarian
                if node.value == nodeValue: # Jika nilai dari node saat ini sama dengan nilai yang dicari
                    return node.value # Kembalikan nilai dari node saat ini
                node = node.next # Pindah ke node berikutnya untuk melanjutkan pencarian
            return "The node does not exist in this SLL" # Kembalikan pesan jika nilai tidak ditemukan

    # Delete a node from Singly Linked List

    def deleteNode(self, location): # Fungsi untuk menghapus node dari linked list berdasarkan lokasi tertentu, memperbarui head atau tail jika diperlukan
        if self.head is None: # Jika linked list kosong, tampilkan pesan bahwa linked list tidak ada
            return "The Singly Linked List does not exist" # Pesan untuk linked list yang tidak ada
        else: # Jika linked list tidak kosong, tentukan lokasi penghapusan
            if location == 0: # Jika lokasi adalah 0, hapus node pertama (head) dari linked list
                if self.head == self.tail: # Jika head dan tail adalah node yang sama, berarti hanya ada satu node dalam linked list, set head dan tail ke None
                    return self.head.value # Kembalikan nilai dari node yang dihapus sebelum menghapusnya
                self.head = self.head.next # Update head ke node berikutnya untuk menghapus node pertama
            return "The node does not exist in this SLL" 
    # Delete a node from Singly Linked List

    def deleteNode(self, location): 
        if self.head is None:
            return "The Singly Linked List does not exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    if tempNode.next is None:
                        break
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    # Delete entire SLL
    def deleteEntireSLL(self):
        if self.head is None:
            print("SLL does not exist")
        else:
            self.head = None
            self.tail = None

singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(44,6)
print([node.value for node in singlyLinkedList])


node1 = Node(1)
node2 = Node(2)

singlyLinkedList.head = node1
singlyLinkedList.head.next = node2
singlyLinkedList.tail = node2

class Node: # Node class untuk menyimpan data dan pointer ke node berikutnya
    def __init__(self, value=None): # Konstruktor untuk inisialisasi nilai dan pointer next
        self.value = value # Menyimpan nilai dari node
        self.next = None # Pointer ke node berikutnya, diinisialisasi dengan None

class SLinkedList: # Kelas untuk mengelola linked list, menyimpan head dan tail
    def __init__(self): # Konstruktor untuk inisialisasi head dan tail
        self.head = None # Pointer ke node pertama dalam linked list, diinisialisasi dengan None
        self.tail = None # Pointer ke node terakhir dalam linked list, diinisialisasi dengan None
    def __iter__(self): # Fungsi iterasi untuk memungkinkan iterasi melalui linked list menggunakan for loop atau list comprehension
        node = self.head # Mulai iterasi dari head
        while node: # Selama node tidak None, terus iterasi
            yield node # Menghasilkan node saat ini untuk iterasi
            node = node.next # Pindah ke node berikutnya dalam linked list
   
    # insert in Linked List #

    def insertSLL(self, value, location): # Fungsi untuk menyisipkan node baru ke dalam linked list pada lokasi tertentu
        newNode = Node(value) # Membuat node baru dengan nilai yang diberikan
        if self.head is None: # Jika linked list kosong, set head dan tail ke node baru
            self.head = newNode # Set head ke node baru
            self.tail = newNode # Set tail ke node baru
        else: # Jika linked list tidak kosong, tentukan lokasi penyisipan
            if location == 0: # Jika lokasi adalah 0, sisipkan node baru di awal linked list
                newNode.next = self.head # Set pointer next dari node baru ke head saat ini
                self.head = newNode # Update head ke node baru
            elif location == 1: # Jika lokasi adalah 1, sisipkan node baru di akhir linked list
                newNode.next = None # Set pointer next dari node baru ke None karena akan menjadi node terakhir
                self.tail.next = newNode # Set pointer next dari tail saat ini ke node baru
                self.tail = newNode # Update tail ke node baru
            else: # Jika lokasi adalah selain 0 atau 1, sisipkan node baru di posisi tertentu dalam linked list
                tempNode = self.head # Mulai dari head untuk mencari posisi penyisipan
                index = 0 # Inisialisasi index untuk melacak posisi saat iterasi
                while index < location - 1: # Iterasi untuk menemukan node sebelum posisi penyisipan
                    if tempNode.next is None: # Jika mencapai akhir linked list sebelum menemukan posisi, keluar dari loop
                        break # Keluar dari loop jika posisi penyisipan melebihi panjang linked list
                    tempNode = tempNode.next # Pindah ke node berikutnya
                    index += 1 # Increment index untuk melacak posisi
                nextNode = tempNode.next # Simpan pointer next dari node sebelum posisi penyisipan untuk menghubungkan ke node baru
                tempNode.next = newNode # Set pointer next dari node sebelum posisi penyisipan ke node baru
                newNode.next = nextNode # Set pointer next dari node baru ke node yang sebelumnya berada di posisi penyisipan

    # Traverse Singly Linked List
    
    def traverseList(self): # Fungsi untuk menampilkan semua nilai dalam linked list dengan traversing dari head ke tail
        if self.head is None: # Jika linked list kosong, tampilkan pesan bahwa linked list tidak ada
            print("The Singly Linked List does not exist") # Pesan untuk linked list yang tidak ada
        else: # Jika linked list tidak kosong, iterasi melalui linked list dan tampilkan nilai setiap node
            node = self.head # Mulai dari head untuk traversing
            while node is not None: # Selama node tidak None, terus traversing
                print(node.value) # Tampilkan nilai dari node saat ini
                node = node.next # Pindah ke node berikutnya untuk melanjutkan traversing

 # Search for a node in Singly Linked List

    def searchSLL(self, nodeValue): # Fungsi untuk mencari nilai tertentu dalam linked list, mengembalikan nilai jika ditemukan atau pesan jika tidak ditemukan
        if self.head is None: # Jika linked list kosong, tampilkan pesan bahwa linked list tidak ada
            print("The Singly Linked List does not exist") # Pesan untuk linked list yang tidak ada
        else: # Jika linked list tidak kosong, iterasi melalui linked list dan cari nilai yang dicari
            node = self.head # Mulai dari head untuk mencari nilai
            while node is not None: # Selama node tidak None, terus mencari
                if node.value == nodeValue: # Jika nilai dari node saat ini sama dengan nilai yang dicari, kembalikan nilai tersebut
                    return node.value # Kembalikan nilai yang ditemukan
                node = node.next # Pindah ke node berikutnya untuk melanjutkan pencarian
            return "The node does not exist in this SLL" # Jika mencapai akhir linked list tanpa menemukan nilai, kembalikan pesan bahwa node tidak ada dalam linked list

    # Delete a node from Singly Linked List
 
    def deleteNode(self, location): # Fungsi untuk menghapus node dari linked list berdasarkan lokasi tertentu, memperbarui head atau tail jika diperlukan
        if self.head is None: # Jika linked list kosong, tampilkan pesan bahwa linked list tidak ada
            return "The Singly Linked List does not exist" # Pesan untuk linked list yang tidak ada
        else: # Jika linked list tidak kosong, tentukan lokasi penghapusan
            if location == 0: # Jika lokasi adalah 0, hapus node pertama (head) dari linked list
                if self.head == self.tail: # Jika head dan tail adalah node yang sama, berarti hanya ada satu node dalam linked list, set head dan tail ke None
                    self.head = None # Set head ke None karena linked list akan menjadi kosong setelah penghapusan
                    self.tail = None # Set tail ke None karena linked list akan menjadi kosong setelah penghapusan
                else: # Jika ada lebih dari satu node, update head ke node berikutnya untuk menghapus node pertama
                    self.head = self.head.next # Update head ke node berikutnya untuk menghapus node pertama
            elif location == 1: # Jika lokasi adalah 1, hapus node terakhir (tail) dari linked list
                if self.head == self.tail: # Jika head dan tail adalah node yang sama, berarti hanya ada satu node dalam linked list, set head dan tail ke None
                    self.head = None # Set head ke None karena linked list akan menjadi kosong setelah penghapusan
                    self.tail = None # Set tail ke None karena linked list akan menjadi kosong setelah penghapusan
                else: # Jika ada lebih dari satu node, iterasi melalui linked list untuk menemukan node sebelum tail, update pointer next dari node tersebut ke None dan update tail ke node tersebut
                    node = self.head # Mulai dari head untuk mencari node sebelum tail
                    while node is not None: # Selama node tidak None, terus mencari
                        if node.next == self.tail: # Jika pointer next dari node saat ini adalah tail, berarti node saat ini adalah node sebelum tail
                            break # Keluar dari loop jika node sebelum tail ditemukan
                        node = node.next # Pindah ke node berikutnya untuk melanjutkan pencarian
                    node.next = None # Set pointer next dari node sebelum tail ke None untuk menghapus tail
                    self.tail = node # Update tail ke node sebelum tail yang sekarang menjadi node terakhir setelah penghapusan
            else: # Jika lokasi adalah selain 0 atau 1, hapus node di posisi tertentu dalam linked list
                tempNode = self.head # Mulai dari head untuk mencari node sebelum posisi penghapusan
                index = 0 # Inisialisasi index untuk melacak posisi saat iterasi
                while index < location-1: # Iterasi untuk menemukan node sebelum posisi penghapusan
                    if tempNode.next is None: # Jika mencapai akhir linked list sebelum menemukan posisi, keluar dari loop
                        break # Keluar dari loop jika posisi penghapusan melebihi panjang linked list
                    tempNode = tempNode.next # Pindah ke node berikutnya
                    index += 1 # Increment index untuk melacak posisi
                nextNode = tempNode.next # Simpan pointer next dari node sebelum posisi penghapusan untuk menghubungkan ke node setelah posisi penghapusan
                tempNode.next = nextNode.next # Set pointer next dari node sebelum posisi penghapusan ke node setelah posisi penghapusan untuk menghapus node di posisi tersebut
    
    # Delete entire SLL

    def deleteEntireSLL(self): # Fungsi untuk menghapus seluruh linked list dengan mengatur head dan tail ke None
        if self.head is None: # Jika linked list kosong, tampilkan pesan bahwa linked list tidak ada
            print("SLL does not exist") # Pesan untuk linked list yang tidak ada
        else: # Jika linked list tidak kosong, set head dan tail ke None untuk menghapus seluruh linked list
            self.head = None # Set head ke None untuk menghapus seluruh linked list
            self.tail = None # Set tail ke None untuk menghapus seluruh linked list

singlyLinkedList = SLinkedList() # Membuat instance dari SLinkedList untuk mengelola linked list
singlyLinkedList.insertSLL(44,6) # Menyisipkan nilai 44 ke dalam linked list pada lokasi 6 (karena linked list masih kosong, nilai ini akan menjadi head dan tail)
print([node.value for node in singlyLinkedList])  # Menampilkan nilai dari semua node dalam linked list menggunakan list comprehension untuk iterasi melalui linked list

node1 = Node(1) # buat node 1
node2 = Node(2) # buat node 2

singlyLinkedList.head = node1 # set head ke node1
singlyLinkedList.head.next = node2 # hubungkan node1 ke node2
singlyLinkedList.tail = node2 # set tail ke node2

singlyLinkedList.insertSLL(3,1) # Menambahkan nilai 3 ke posisi "akhir" (karena di kode, location==1 dianggap append)
singlyLinkedList.insertSLL(4,1) # Menambahkan nilai 4 lagi ke akhir linked list
print([node.value for node in singlyLinkedList])  # Menampilkan seluruh isi list setelah penambahan (hasil: [1, 2, 3, 4])
singlyLinkedList.insertSLL(5,3) # Menyisipkan nilai 5 di index ke-3 (di tengah list, sebelum elemen index 3 lama)
print([node.value for node in singlyLinkedList]) # Menampilkan hasil akhir (hasil: [1, 2, 3, 5, 4])

# output :
# [44]
# [1,2,3,4]
# [1,2,3,5,4]