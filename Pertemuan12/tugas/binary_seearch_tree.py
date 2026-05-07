class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.kiri = None
        self.kanan = None

class BST:
    def __init__(self):
        self.root = None
        self.hitung = 1
        
    def insert(self, id_buku, judul):
        if self.root is None:
            self.root = Node(id_buku, judul)
            print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
            return
        
        simpul_sekarang = self.root
        while True:
            if id_buku < simpul_sekarang.id_buku:
                if simpul_sekarang.kiri is None:
                    simpul_sekarang.kiri = Node(id_buku, judul)
                    print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
                    break
                simpul_sekarang = simpul_sekarang.kiri
            elif id_buku > simpul_sekarang.id_buku:
                if simpul_sekarang.kanan is None:
                    simpul_sekarang.kanan = Node(id_buku, judul)
                    print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
                    break
                simpul_sekarang = simpul_sekarang.kanan
            else:
                break

    def search(self, id_buku):
        print(f"[SEARCH] Mencari ID {id_buku}... ", end="")
        simpul_sekarang = self.root
        while simpul_sekarang is not None:
            if id_buku == simpul_sekarang.id_buku:
                print(f"Ditemukan! Judul: {simpul_sekarang.judul}")
                return True
            elif id_buku < simpul_sekarang.id_buku:
                simpul_sekarang = simpul_sekarang.kiri
            else:
                simpul_sekarang = simpul_sekarang.kanan
        print("Data tidak ditemukan.")
        return False

    def _inorder_helper(self, simpul):
        if simpul is not None:
            self._inorder_helper(simpul.kiri)
            print(f"{self.hitung}. {simpul.id_buku} - {simpul.judul}")
            self.hitung += 1
            self._inorder_helper(simpul.kanan)

    def traversal_inorder(self):
        self.hitung = 1
        self._inorder_helper(self.root)

    def get_min(self):
        if self.root is None: 
            return None
        simpul_sekarang = self.root
        while simpul_sekarang.kiri is not None:
            simpul_sekarang = simpul_sekarang.kiri
        return simpul_sekarang.id_buku

    def get_max(self):
        if self.root is None: 
            return None
        simpul_sekarang = self.root
        while simpul_sekarang.kanan is not None:
            simpul_sekarang = simpul_sekarang.kanan
        return simpul_sekarang.id_buku

    def _height_helper(self, simpul):
        if simpul is None:
            return -1
        tinggi_kiri = self._height_helper(simpul.kiri)
        tinggi_kanan = self._height_helper(simpul.kanan)
        return max(tinggi_kiri, tinggi_kanan) + 1

    def height(self):
        return self._height_helper(self.root)

if __name__ == "__main__":
    katalog = BST()
    
    katalog.insert(50, "Dasar Pemrograman")
    katalog.insert(30, "Struktur Data")
    katalog.insert(70, "Kecerdasan Buatan")
    katalog.insert(20, "Matematika Diskrit")
    katalog.insert(40, "Basis Data")
    katalog.insert(60, "Jaringan Komputer")
    katalog.insert(80, "Sistem Operasi")
    
    print('\n[INFO] Koleksi Buku (In-Order Traversal):')
    katalog.traversal_inorder()
    
    print()
    katalog.search(60)
    katalog.search(100)
    
    print(f'\n[STATISTIK] ID Terkecil: {katalog.get_min()}')
    print(f'[STATISTIK] ID Terbesar: {katalog.get_max()}')
    print(f'[INFO] Tinggi (Height) Tree: {katalog.height()}')
    
    print('=========================================')
    print('Simulasi Selesai!')