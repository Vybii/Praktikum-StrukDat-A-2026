from tabulate import tabulate
ngunjung_hari_ini = [
    {"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi","kembali": False},
    {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains","kembali": True},
    {"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi","kembali": False},
    {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum","kembali": True},
    {"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains","kembali": False},
    {"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum","kembali": False}
]

#=======Soal nomor 1=======
def tampilkan_pengunjung():
    print("===== DATA PENGUNJUNG PERPUSTAKAAN =====")
    print("No | ID   | Nama   | Usia | Kategori | Status Kembali")
    print("---+------+--------+------+----------+---------------")
    
    for i, p in enumerate(ngunjung_hari_ini, 1):
        status = "Sudah Kembali" if p["kembali"] else "Belum Kembali"
        print(f"{i:<3}| {p['id']:<4} | {p['nama']:<6} | {p['usia']:<4} | {p['kategori']:<8} | {status}")
satu = tampilkan_pengunjung()
print(satu)


NoDua = []
def filter_belum_kembali(jmlh):
    d = len(jmlh)
    for b in range(d):
        NoDua.append(jmlh[b]["nama"])
        NoDua.sort()
    for e in range(d):
        print(f"{e+1}. {NoDua[e]}")
dua = filter_belum_kembali(ngunjung_hari_ini)
print(dua)

#=======Soal nomor 2=======
def info_perpustakaan():
    tpl = (
        {"Nama": "Perpustakaan Kampus Terpadu",
        "Alamat": "Jl. Pendidikan No. 5, Pekanbaru",
        "Telp": "0761-54321"}
    )
    print(tpl)
tiga = info_perpustakaan()
print(tiga)

def rekap_kategori(yes) :
    kategoriBukuunik = []
    g = len(ngunjung_hari_ini)
    for t in range(g):
        kategoriBukuunik.append(yes[t]["kategori"])
    buku = set(kategoriBukuunik)
    k = len(buku)
    print(buku)
    print(f'Jumlah kategori: {k}')
empat = rekap_kategori(ngunjung_hari_ini)
print(empat)

#=======Soal nomor 3=======
class Pengunjung:
    def __init__(self, id, nama, kategori):
        pass

    def tampilkan_info():
        pass

    def hitung_pengunjung():
        pass

class PengunjungPrioritas:
    def __init__(self, prioritas):
        pass

    def info():
        pass

#=======Soal nomor 4=======
class Node:
    def __init__(self, data):
        self.head = data
        self.next = None

class AntrianPeminjaman:
    def __init__(self):
        pass


# antrian = AntrianPeminjaman()
# antrian.tambah({"id": "M001", "nama": "Rina", "kategori": "Fiksi"})
# antrian.tambah({"id": "M002", "nama": "Hendra", "kategori": "Sains"})
# antrian.tambah({"id": "M003", "nama": "Siti", "kategori": "Fiksi"})
# antrian.tambah({"id": "M004", "nama": "Taufik", "kategori": "Hukum"})
# antrian.tampilkan()
# antrian.panggil_berikutnya()
# antrian.tampilkan()
# antrian.hapus_berdasarkan_id("M003")
# antrian.tampilkan()
# antrian.cari("Taufik")
# print("Total antrian:", antrian.hitung())