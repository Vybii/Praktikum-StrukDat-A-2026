from tabulate import tabulate
import kurs
import konverter

print("=== KONVERTER MATA UANG ===")

tabel = []
for kode, nilai in kurs.output.items():
    tabel.append([kode, nilai])

print(tabulate(tabel, headers=["Kode", "Kurs"], tablefmt="psql"))
print("\n")

awal = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper()
tujuan = input("Tujuan (IDR/USE/EUR/SGD/JPY): ").upper()
jumlah = float(input("Jumlah: "))

total = konverter.konversiUang(awal, tujuan, jumlah)

if tujuan == 'IDR':
    print(f"{jumlah:.2f} {awal} = Rp {total}")
elif awal == 'IDR':
    print(f"Rp {jumlah:.2f} = {total:.2f} {tujuan}")
else:
    print(f"{jumlah:.2f} {awal} = {total:.2f} {tujuan}")