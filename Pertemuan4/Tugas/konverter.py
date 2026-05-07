import kurs

def konversiUang(awal, tujuan, jumlah):
    if awal in kurs.mataUang and tujuan in kurs.mataUang:
        return jumlah * kurs.mataUang[awal] / kurs.mataUang[tujuan]
    else:
        return "Mata uang gak terdaftar di list"

