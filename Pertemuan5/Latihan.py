#list, set, tuple, dictionary
print("No.1")
stok_barang = [15, 40, 30, 10, 25]
index = stok_barang.index(10)
print("cari index")
print(index)
nosatuubah = stok_barang[index] = 50
print("ganti 10 jadi 50")
print(stok_barang)

stok_barang.append(5)
print("tambah 5 di akhir")
print(stok_barang)
stok_barang.sort(reverse=True)
print("sort dari besar ke kecil")
print(stok_barang)

print("rata-rata")
x = sum(stok_barang)
print(x)

print("stok")
rata = x / 5
if rata > 20:
    print("Stok aman")
else:
    print("Waspada")

print("=============")
print("No.2")
data_aktifitas = [
    ("Diki", 88),
    ("Aqul", 45),
    ("Abid", 92),
    ("Rehan", 70)
]

for x in data_aktifitas:
    a, b = x
    if b > 80:
        print(f"{a} mendapatkan predikat Gold")
    elif b > 50:
        print(f"{a} mendapatkan predikat Silver")
    else:
        print(f"{a} mendapatkan predikat Bronze")

print("==================")
print("No.3")
ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}
ukmcodingdoang = ukm_coding - ukm_robotik
print(ukmcodingdoang)
totalsemua = ukm_coding | ukm_robotik
print(totalsemua)

yagak = "Andi" in ukm_robotik
print(yagak)

print("======================")
print("No.4")
gudang_pc = [
    {"item": "Monitor", "harga": 1500000, "stok": 5},
    {"item": "Keyboard", "harga": 400000, "stok": 12},
    {"item": "Mouse", "harga": 250000, "stok": 20}
]

for x in gudang_pc:
    if x["item"] == "Keyboard":
        x["kategori"] = "Aksesoris"

gudang_pc.append({"item": "Headset", "harga": 350000, "stok": 8})
print(gudang_pc)

for x in gudang_pc:
    total = x["harga"] * x["stok"]
    print(f"item: {x["item"]} | Total Aset: Rp. {total}")