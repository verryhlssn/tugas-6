class Node:    # Kelas node untuk menyimpan data dan pointer (next & prev)
    def __init__(self, value=None):    # Konstruktor node
        self.value = value    # Menyimpan nilai/data node
        self.next = None    # Pointer ke node berikutnya
        self.prev = None    # Pointer ke node sebelumnya (doubly linked list)
    
    def __str__(self):    # Method untuk representasi string node
        return str(self.value)    # Mengembalikan nilai node dalam bentuk string

class LinkedList:    # Kelas Linked List (doubly linked list)
    def __init__(self, values = None):    # Konstruktor list
        self.head = None    # Pointer ke node pertama
        self.tail = None    # Pointer ke node terakhir

    def __iter__(self):    # Method agar bisa di-loop (iterable)
        curNode = self.head    # Mulai dari head
        while curNode:    # Selama node tidak None
            yield curNode    # Kembalikan node saat ini
            curNode = curNode.next    # Pindah ke node berikutnya
    
    def __str__(self):    # Method untuk menampilkan list sebagai string
        values = [str(x.value) for x in self]    # Ambil semua nilai node jadi list string
        return ' -> '.join(values)    # Gabungkan dengan panah sebagai pemisah
    
    def __len__(self):    # Method untuk menghitung jumlah node
        result = 0    # Variabel penghitung
        node = self.head    # Mulai dari head
        while node:    # Selama node ada
            result += 1    # Tambah counter
            node = node.next    # Pindah ke node berikutnya
        return result    # Kembalikan jumlah node
    
    def add(self, value):    # Method untuk menambahkan node di akhir
        newNode = Node(value)    # Buat node baru
        if self.head is None:    # Jika list kosong
            self.head = newNode    # Set sebagai head
            self.tail = newNode    # Set sebagai tail
        else:    # Jika sudah ada isi
            self.tail.next = newNode    # Tail lama menunjuk ke node baru
            newNode.prev = self.tail    # Node baru menunjuk balik ke tail lama
            self.tail = newNode    # Update tail ke node baru
        return self.tail    # Return node terakhir
    
    def generate(self, n, min_value, max_value):    # Method untuk generate n node random
        self.head = None    # Reset head (hapus list lama)
        self.tail = None    # Reset tail
        for i in range(n):    # Loop sebanyak n kali
            from random import randint    # Import fungsi random integer
            self.add(randint(min_value,max_value))    # Tambah node dengan nilai random
        return self    # Return object list

customLL = LinkedList()    # Membuat objek LinkedList
customLL.generate(10, 0, 99)    # Generate 10 node dengan nilai random 0-99
print(customLL)    # Cetak isi linked list (pakai __str__)
print(len(customLL))    # Cetak jumlah node (pakai __len__)

# output :
# 82 -> 96 -> 1 -> 75 -> 48 -> 13 -> 98 -> 45 -> 15 -> 15 -> 10

# (Output dari linked list bersifat random karena setiap node diisi dengan angka acak menggunakan randint(min_value, max_value), sehingga setiap eksekusi program kemungkinan besar menghasilkan nilai yang berbeda.Jika ingin hasil yang sama setiap kali dijalankan, bisa menggunakan :
# import random
# random.seed(1)
# sebelum di generate.