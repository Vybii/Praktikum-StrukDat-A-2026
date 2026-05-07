def tambah_buku(nama, harga, stok):
    if harga <= 0:
        return None
    if stok < 0:
        return None
    data = {
        "nama" : nama,
        "harga" : harga,
        "stok" : stok
    }
    return data

list = []
for x in range (3):
    msknama = input("nama buku yang dicari: ")
    mskharga  = float(input("harga dari buku: "))
    mskstok = int(input("Jumlah stok buku:" ))
    
    hasil = tambah_buku(msknama, mskharga, mskstok)

    if hasil is not None:
        list.append(hasil)

for nama in list:
    print(nama)

if hasil is None:
    print("Buku tidak ada")