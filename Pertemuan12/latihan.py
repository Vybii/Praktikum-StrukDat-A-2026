class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None


class Antrian:
    def __init__(self):
        self.head = None
        self.tail = None
        self.jumlah = 0

    def enqueue(self, nama, keluhan):
        baru = Node(nama, keluhan)

        if self.head == None:
            self.head = baru
            self.tail = baru
        else:
            self.tail.next = baru
            self.tail = baru

        self.jumlah += 1
        print("Pasien", nama, "masuk antrian, keluhan:", keluhan)

    def dequeue(self):
        if self.head == None:
            print("Antrian kosong")
            return

        keluar = self.head
        self.head = self.head.next

        if self.head == None:
            self.tail = None

        self.jumlah -= 1
        print("Dipanggil:", keluar.nama, "-", keluar.keluhan)

    def peek(self):
        if self.head == None:
            print("Tidak ada pasien")
        else:
            print("Selanjutnya:", self.head.nama, "-", self.head.keluhan)

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def size(self):
        return self.jumlah

    def clear(self):
        self.head = None
        self.tail = None
        self.jumlah = 0
        print("Antrian dikosongkan")

    def tampil(self):
        if self.head == None:
            print("Kosong")
            return

        sekarang = self.head
        no = 1
        while sekarang != None:
            print(no, ".", sekarang.nama, "-", sekarang.keluhan)
            sekarang = sekarang.next
            no += 1



a = Antrian()
print("Cek kosong:", a.is_empty())

a.enqueue("BUDI", "demam tinggi")
a.enqueue("ANI", "batuk pilek")
a.enqueue("CITRA", "sakit kepala")
print("Jumlah:", a.size())
a.peek()
a.dequeue()
a.enqueue("DODI", "nyeri perut")
a.tampil()
a.dequeue()

print("Sisa:", a.size())
a.clear()
print("Cek lagi:", a.is_empty())