level_diskon = (
    (500000, 15),
    (300000, 10),
    (100000, 5),
    (0, 0)
)

tuple = ()
def hitung_diskon(total_belanja, level_diskon, index = 0):
    if total_belanja >= level_diskon[index][0]:
        persen_diskon = level_diskon[index][1]
    else:
        index += 1

    nominal_diskon = level_diskon[index][0] * (level_diskon[index][1] / 100)
    total_bayar = level_diskon[index][0] - nominal_diskon
    yes = hitung_diskon(persen_diskon, nominal_diskon, total_bayar)
    masukin = tuple.append(yes)
    return masukin

nama = input("Masukan nama: ")
total = float(input("total belanja: "))

mau_diskon = hitung_diskon(total, level_diskon)

if total < 100000:
    print("Tidak ada diskon")
else:
    print(mau_diskon)