
class HashTable:
    
    def __init__(self):
        
        self.ukuran = 10
        
        # buat bucket kosong
        self.tabel = []
        
        for i in range(self.ukuran):
            self.tabel.append([])

    # bikin fungsi hash
    def hash(self, kode):
        
        jumlah = 0
        
        for huruf in kode:
            jumlah = jumlah + ord(huruf)
            
        index = jumlah % self.ukuran
        
        return index

    # nambah data
    def insert(self, kode, judul):
        
        index = self.hash(kode)

        # cek apakah kode sudah ada
        for data in self.tabel[index]:
            
            if data[0] == kode:
                data[1] = judul
                print("Data berhasil diupdate")
                return

        # tambah data baru
        self.tabel[index].append([kode, judul])
        print("Data berhasil ditambahkan")

    # nyari data atau search
    def search(self, kode):
        
        index = self.hash(kode)

        for data in self.tabel[index]:
            
            if data[0] == kode:
                print("Judul Buku :", data[1])
                return

        print("Buku tidak ditemukan")

    # ngapus data atau delete
    def delete(self, kode):
        
        index = self.hash(kode)

        for data in self.tabel[index]:
            
            if data[0] == kode:
                self.tabel[index].remove(data)
                print("Data berhasil dihapus")
                return

        print("Buku tidak ditemukan")

    # nampilkan hash table atau ngedisplay
    def display(self):
        
        print("\nMenampilkan isi hash table:")

        for i in range(self.ukuran):
            
            print("Bucket", i, ":", end=" ")

            if len(self.tabel[i]) == 0:
                print("Kosong")

            else:
                for data in self.tabel[i]:
                    print(data, end=" ")
                    
                print()

        print("==========================\n")

# program utama

perpus = HashTable()

# insert atau nambah data awal
perpus.insert("BK111", "Mahir C++ Dalam Satu Jam")
perpus.insert("BK222", "Python Dasar")
perpus.insert("BK333", "Matematika Diskrit")
perpus.insert("BK444", "Atomic Habits")
perpus.insert("BK555", "Algoritma Dasar")

# tampilkan isi
perpus.display()

# insert atau nambah data baru
perpus.insert("BK045", "Mein Kampf")

# update data atau mempperbarui data
perpus.insert("BK111", "Bumi Manusia")

# display atautampilkan lagi
perpus.display()

# search atau mencari data
print("HASIL SEARCH")
perpus.search("BK222")
perpus.search("BK999")

# delete atau menghapus data
print("\nHASIL DELETE")
perpus.delete("BK333")

# display atau tampilkan akhir
perpus.display()