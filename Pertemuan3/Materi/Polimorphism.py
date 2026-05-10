class Transaksi:
    def __init__(self, total, keterangan):
        self.total = total
        self.keterangan = keterangan

    def proses(self):
        pass

class Pemasukan(Transaksi):
    def proses(self):
        print(f"Uang masuk: Rp{self.total} ({self.keterangan})")

class Pengeluaran(Transaksi):
    def proses(self):
        print(f"Uang keluar: Rp{self.total} ({self.keterangan})")

def catat_keuangan(item_transaksi):
    item_transaksi.proses()

masuk = Pemasukan(5000000, "Gaji bulanan")
keluar = Pengeluaran(100000, "Pulang kedumai")

catat_keuangan(masuk)
catat_keuangan(keluar)