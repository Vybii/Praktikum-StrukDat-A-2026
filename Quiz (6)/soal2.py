katalog = [
    {'nama': 'Belajar Python', 'harga': 75000, 'stok': 5},
    {'nama': 'Struktur Data', 'harga': 95000, 'stok': 3},
    {'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8},
]

daftar = []
kosong = []
def cari_buku(daftarbuku, keyword):
    keyword.lower()
    daftarbuku.lower()
    for x in katalog:
        if keyword in x['nama']:
            apaaja = daftar.append(x['nama'])
        else:
            print(kosong)
            print("Buku tidak ditemukan.")
kata = input("Masukan keyword: ")
cari_buku(katalog, kata)

cari_buku(katalog, kata)